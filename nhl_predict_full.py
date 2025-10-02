
import requests
import datetime
import pandas as pd
import numpy as np
import os

# Dummy models for demonstration (replace with your trained models)
def dummy_predict_winner(features):
    return np.random.choice(["Home", "Away"])

def dummy_predict_goals(features):
    return round(np.random.uniform(4.5, 7.5), 1)

def dummy_predict_scores(features):
    # random plausible score
    home_goals = np.random.randint(1,6)
    away_goals = np.random.randint(1,6)
    return home_goals, away_goals

def get_team_features(team_name):
    # placeholder for team features (you would fetch from NHL API / stats)
    return np.random.rand(10)  # 10 features per team

def combine_features(home_stats, away_stats):
    return np.concatenate([home_stats, away_stats])

today = datetime.date.today().strftime("%Y-%m-%d")
schedule_url = f"https://statsapi.web.nhl.com/api/v1/schedule?date={today}"
schedule = requests.get(schedule_url).json()

games_today = []
for d in schedule['dates']:
    for g in d['games']:
        home = g['teams']['home']['team']['name']
        away = g['teams']['away']['team']['name']
        games_today.append((home, away))

predictions = []
for home, away in games_today:
    home_stats = get_team_features(home)
    away_stats = get_team_features(away)
    features = combine_features(home_stats, away_stats)
    winner = dummy_predict_winner(features)
    goals = dummy_predict_goals(features)
    score_home, score_away = dummy_predict_scores(features)
    predictions.append({
        "date": today,
        "home_team": home,
        "away_team": away,
        "predicted_winner": winner,
        "predicted_total_goals": goals,
        "predicted_score_home": score_home,
        "predicted_score_away": score_away
    })

df = pd.DataFrame(predictions)
os.makedirs("data", exist_ok=True)
df.to_csv("data/nhl_predictions.csv", index=False)
print("Predictions saved to data/nhl_predictions.csv")
