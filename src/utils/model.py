import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from joblib import dump
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def update_model(model: Pipeline) -> None:
    dump(model, "./model/models.pkl")


def update_scaler(scaler: StandardScaler) -> None:
    dump(scaler, "./model/scaler.pkl")


def save_report(train_score: float, test_score: float, model: Pipeline) -> None:
    with open('./reports/scores.txt', 'w') as f:

        f.write(f'# Model Pipeline description')

        for key, value in model.named_steps.items():
            f.write(f'### {key}: {value.__repr__()}'+'\n')

        f.write(f'### Train Score: {train_score}'+'\n')
        f.write(f'### Test Score: {test_score}'+'\n')
        f.close()


def plot_model_results(y_true: pd.Series, y_pred: pd.Series) -> None:
    fig, ax = plt.subplots()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    sns.regplot(x=y_true, y=y_pred, ax=ax)
    ax.set_xlabel('Predicted Worldwide Gross')
    ax.set_ylabel('Actual Worldwide Gross')
    ax.set_title('Model Predictions vs Actual')
    plt.savefig('./reports/model_performance.png')

