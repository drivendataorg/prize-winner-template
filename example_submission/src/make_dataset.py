from itertools import permutations

from loguru import logger
import pandas as pd
from tqdm import tqdm
import typer
from typing import Optional


def get_ngram_features(data, subsequences=None):
    """Generates counts for each subsequence.

    Args:
        data (pd.DataFrame): The data you want to create features from. Must include a "sequence" column.
        subsequences (list): A list of subsequences to count.

    Returns:
        DataFrame: A DataFrame with one column for each subsequence.
    """
    if not subsequences:
        bases = set("".join(data.sequence.values))

        n = 4
        subsequences = [
            "".join(permutation) for permutation in permutations(bases, r=n)
        ]
    logger.info(f"Generating n-gram features using {len(subsequences)} sequences")

    sequence_counts = {}
    for subseq in tqdm(subsequences):
        sequence_counts[subseq] = data.sequence.str.count(subseq)
    features = pd.DataFrame(sequence_counts, index=data.index)
    features = features.join(data.drop(columns=["sequence"]))

    features = features.sort_index(axis=1)
    assert (features.index == data.index).all()

    return features


def make_dataset(features: pd.DataFrame, labels: Optional[pd.DataFrame] = None):
    """
    Process the raw features and labels (if provided). If labels are provided,
    returns tuple of (features: pd.DataFrame, labels: numpy.ndarray).
    If no labels are provided, returns the features as a pd.DataFrame.
    """
    features = get_ngram_features(features)

    if labels is not None:
        # get the column with the max value in each row
        labels = pd.DataFrame(labels.idxmax(axis=1), columns=["lab_id"])

        # make sure order matching the features
        labels = labels.loc[features.index]

        return features, labels.values.ravel()

    else:
        return features
