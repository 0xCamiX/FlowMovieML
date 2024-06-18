from api.config.config import get_model
from api.config.config import get_scaler
from api.config.config import transform_dataframe
from api.models.movie import MoviePredictionRequest


class PredictionService:
    def __init__(self):
        self.model = get_model()
        self.scaler = get_scaler()

    def predict(self, features: MoviePredictionRequest) -> float:
        processed_features = transform_dataframe(features)
        scaled_features = self.scaler.transform(processed_features)
        predict = self.model.predict(scaled_features)
        return float(predict[0])
