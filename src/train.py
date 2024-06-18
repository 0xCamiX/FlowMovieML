import sys
import logging

import numpy as np
import pandas as pd

from utils.model import update_model
from utils.model import update_scaler
from utils.model import save_report
from utils.model import plot_model_results

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_validate

from xgboost import XGBRegressor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="$H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

# LOADING DATA
logger.info("Loading data...")
data = pd.read_csv("./dataset/clean_dataset.csv")

X = data.drop("worldwide_gross", axis=1)
y = data["worldwide_gross"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(X_train.shape, X_test.shape)
logger.info("Shape of X_train: %s", X_train.shape)
logger.info("Shape of X_test: %s", X_test.shape)

# PIPELINE

model = Pipeline([
    ("imputer", SimpleImputer(missing_values=np.nan, strategy="mean")),
    ("models", XGBRegressor(n_estimators=140))
])

results = cross_validate(model, X_train, y_train, cv=8, return_train_score=True)

train_score = np.mean(results['train_score'])
test_score = np.mean(results['test_score'])

assert train_score > 0.6
assert test_score > 0.6

logger.info("Train score: %s", train_score)
logger.info("Test score: %s", test_score)

model.fit(X_train, y_train)
model.score(X_test, y_test)

logger.info("Updating models")

update_model(model)
update_scaler(scaler)

logger.info("Generating models report...")

save_report(train_score, test_score, model)

logger.info("Training completed.")

y_true = y_test

plot_model_results(y_true, model.predict(X_test))
