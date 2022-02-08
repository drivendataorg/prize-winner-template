from loguru import logger
import pandas as pd
from pathlib import Path
import pickle
import typer
from sklearn.ensemble import RandomForestClassifier

from src.make_dataset import make_dataset


def main(
    model_path: Path = typer.Option(
        "models/random_forest.pkl", help="Path to the saved model weights"
    ),
    features_path: Path = typer.Option(
        "data/raw/test_values.csv", help="Path to the test features"
    ),
    submission_save_path: Path = typer.Option(
        "data/processed/submission.csv", help="Path to save the generated submission"
    ),
    submission_format_path: Path = typer.Option(
        "data/raw/submission_format.csv", help="Path to the submission format csv"
    ),
    debug: bool = typer.Option(
        False, help="Run on a small subset of the data for debugging"
    ),
):
    nrows = None
    if debug:
        logger.info("Running in debug mode")
        nrows = 20

    logger.info(f"Loading feature data from {features_path}")
    features = pd.read_csv(features_path, index_col="sequence_id", nrows=nrows)

    logger.info(f"Processing feature data. Shape: {features.shape}")
    X = make_dataset(features)

    logger.info(f"Loading trained model weights from {model_path}")
    with open(model_path, "rb") as file:
        loaded_model = pickle.load(file)

    logger.info(
        f"Predicting labels based on submission format at {submission_format_path}"
    )
    probas = loaded_model.predict_proba(X)

    # generate submission
    submission_format = pd.read_csv(
        submission_format_path, index_col="sequence_id", nrows=nrows
    )

    assert submission_format.shape == probas.shape
    assert (loaded_model.classes_ == submission_format.columns).all()

    my_submission = pd.DataFrame(
        data=probas, columns=loaded_model.classes_, index=submission_format.index
    )
    if not debug:
        my_submission.to_csv(submission_save_path, index=True)
        logger.success(f"Submission saved to {submission_save_path}")


if __name__ == "__main__":
    typer.run(main)
