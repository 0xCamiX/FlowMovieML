from pydantic import BaseModel


class MoviePredictionRequest(BaseModel):
    domestic_gross: float
    production_budget: float
    title_year: float
    aspect_ratio: float
    duration: float
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float
    opening_gross: float
    screens: float


class MoviePredictionResponse(BaseModel):
    worldwide_gross: float
