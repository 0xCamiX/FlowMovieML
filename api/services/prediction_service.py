from api.config.utils import get_model
from api.config.utils import get_scaler
from api.config.utils import transform_dataframe
from api.models.movie import MoviePredictionRequest


class PredictionService:
    def __init__(self):
        self.model = get_model()
        self.scaler = get_scaler()

    def predict(self, features: MoviePredictionRequest):
        processed_features = transform_dataframe(features)
        scaled_features = self.scaler.transform(processed_features)
        prediction = self.model.predict(scaled_features)
        return prediction
