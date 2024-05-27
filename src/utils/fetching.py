from typing import Any, Generator

import pandas as pd
from dvc import api
from pandas import DataFrame


def fetch_all_datasets(repo: str, dataset_names: list) -> Generator[DataFrame, Any, None]:
    """
    Fetches all datasets from a given repository.

    Parameters:
    repo (str): The URL of the repository where the datasets are stored.
    dataset_names (list): A list of the names of the datasets to fetch.

    Returns:
    tuple: A tuple containing pandas DataFrames of the fetched datasets.
    """
    return (fetch_dataset(repo, dataset_name) for dataset_name in dataset_names)


def fetch_dataset(repo: str, dataset_name: str) -> pd.DataFrame:
    """
    Fetches a single dataset from a given repository.

    Parameters:
    repo (str): The URL of the repository where the dataset is stored.
    dataset_name (str): The name of the dataset to fetch.

    Returns:
    pd.DataFrame: A pandas DataFrame of the fetched dataset.
    """
    with api.open(repo=repo, path=f"dataset/{dataset_name}", mode='rb') as fd:
        return pd.read_csv(fd)
