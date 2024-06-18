import os
import pandas as pd

from io import BytesIO
from joblib import load

from sklearn.pipeline import Pipeline
from api.models.movie import MoviePredictionRequest


def get_model() -> Pipeline:
    """Returns the model used for prediction.

    :return:
    """
    model_path = os.environ.get("MODEL_PATH", "model/model.pkl")
    with open(model_path, "rb") as file:
        model = load(BytesIO(file.read()))
    return model


def transform_dataframe(request: MoviePredictionRequest) -> pd.DataFrame:
    """Transforms the request data into a DataFrame.

    :param request:
    :return:
    """
    dict_data = {key: [value] for key, value in request.model_dump().items()}
    return pd.DataFrame(dict_data)


def get_scaler() -> Pipeline:
    """Returns the scaler used for prediction.

    :return:
    """
    scaler_path = os.environ.get("SCALER_PATH", "model/scaler.pkl")
    with open(scaler_path, "rb") as file:
        scaler = load(BytesIO(file.read()))
    return scaler
