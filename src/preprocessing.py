import sys
import logging

import pandas as pd

from utils.fetching import fetch_all_datasets

# CONFIGURATION LOGGING

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

# INIT PREPROCESSING

logger.info("Fetching all dataset...")

REPOSITORY = 'https://github.com/0xCamiX/FlowMovieML/'
DATASET_NAMES = ['financials.csv', 'movies.csv', 'opening_gross.csv']

financials, movies, opening_gross = fetch_all_datasets(REPOSITORY, DATASET_NAMES)

logger.info("Datasets fetched successfully.")

# PREPROCESSING

logger.info("Preprocessing datasets...")

df = pd.merge(financials, pd.merge(movies, opening_gross, on='movie_title'), on='movie_title')

numeric_columns_mask = (df.dtypes == float) | (df.dtypes == int)
numeric_columns = [column for column in numeric_columns_mask.index if numeric_columns_mask[column]]

df = df[numeric_columns].drop(columns=['gross'])

df = df.dropna()

df.to_csv('./dataset/clean_dataset.csv', index=False)

logger.info("Datasets preprocessed successfully.")

breakpoint()
