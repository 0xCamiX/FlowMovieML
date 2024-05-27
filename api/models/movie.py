from pydantic import BaseModel


class MoviePredictionRequest(BaseModel):
    domestic_gross: int
    production_budget: int
    title_year: float
    aspect_ratio: float
    duration: float
    cast_total_facebook_likes: int
    budget: float
    imdb_score: float
    opening_gross: float
    screens: float


class MoviePredictionResponse(BaseModel):
    worldwide_gross: float
