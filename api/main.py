from fastapi import FastAPI
from api.routers import predict
app = FastAPI(
    title='FlowMovieML',
    description='Predicting movie worldwide gross with machine learning'
)

app.include_router(predict.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
