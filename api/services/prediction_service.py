from api.config.utils import get_model
from api.config.utils import get_scaler
from api.config.utils import transform_dataframe
from api.models.movie import MoviePredictionRequest


class PredictionService:
    def __init__(self):
        self.model = get_model()
        self.scaler = get_scaler()

    def predict(self, features: MoviePredictionRequest) -> float:
        processed_features = transform_dataframe(features)
        scaled_features = self.scaler.transform(processed_features)
        # Change the row 0 of the processed features to the scaled features
        processed_features.loc[0] = scaled_features[0]
        prediction = self.model.predict(processed_features)
        return float(prediction[0])
