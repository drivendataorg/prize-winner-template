from loguru import logger
import pandas as pd
from pathlib import Path
import pickle
import typer
from sklearn.ensemble import RandomForestClassifier

from src.make_dataset import make_dataset


def main(
    features_path: Path = typer.Option(
        "data/raw/train_values.csv",
        help="Path to the raw training dataset for processing",
    ),
    labels_path: Path = typer.Option(
        "data/raw/train_labels.csv", help="Path to the training labels"
    ),
    model_save_path: Path = typer.Option(
        "models/random_forest.pkl", help="Path to save the trained model weights"
    ),
    debug: bool = typer.Option(
        False, help="Run on a small subset of the data for debugging"
    ),
):
    nrows = None
    if debug:
        logger.info("Running in debug mode")
        nrows = 20

    logger.info(f"Loading data from {features_path}")
    features = pd.read_csv(features_path, index_col="sequence_id", nrows=nrows)
    labels = pd.read_csv(labels_path, index_col="sequence_id", nrows=nrows)

    logger.info(f"Processing data. Data shape: {features.shape}")
    X, y = make_dataset(features, labels=labels)

    # instantiate our RF Classifier
    rf = RandomForestClassifier(
        n_jobs=4,
        n_estimators=150,
        class_weight="balanced",  # balance classes
        max_depth=3,  # shallow tree depth to prevent overfitting
        random_state=0,  # set a seed for reproducibility
    )

    # fit our model
    logger.info("Training random forest model")
    rf.fit(X, y)

    # save model
    if not debug:
        with open(model_save_path, "wb") as file:
            pickle.dump(rf, file)
        logger.success(f"Trained model saved to {model_save_path}")


if __name__ == "__main__":
    typer.run(main)
