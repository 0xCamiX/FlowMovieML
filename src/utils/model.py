from joblib import dump
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def update_model(model: Pipeline) -> None:
    dump(model, "./model/model.joblib")


def update_scaler(scaler: StandardScaler) -> None:
    dump(scaler, "./model/scaler.joblib")


