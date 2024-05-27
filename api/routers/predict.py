from fastapi import APIRouter, Depends
from api.models.movie import MoviePredictionRequest
from api.services.prediction_service import PredictionService

router = APIRouter()


@router.post("/predict")
async def predict(movie_features: MoviePredictionRequest, service: PredictionService = Depends(PredictionService)):
    prediction = service.predict(movie_features)
    return {"prediction": prediction}
