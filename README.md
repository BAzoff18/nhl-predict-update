# NHL Prediction Script

This repository automatically pulls today's NHL games from the NHL API and predicts the winner, total goals, and score.
It saves predictions to `data/nhl_predictions.csv`.

## How to run locally

```bash
pip install pandas requests numpy
python nhl_predict_full.py
```

## GitHub Actions

Set up `.github/workflows/update.yml` as shown to run daily and commit the updated CSV back to your repo.
