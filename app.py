from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Historical performance scores based on the last 5 years with team logos
historical_scores = {
    "Manchester City": {"score": 95, "logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"},
    "Liverpool": {"score": 85, "logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg"},
    "Arsenal": {"score": 80, "logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"},
    "Manchester United": {"score": 78, "logo": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg"},
    "Chelsea": {"score": 75, "logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"},
    "Tottenham Hotspur": {"score": 70, "logo": "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg"},
    "Newcastle United": {"score": 68, "logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Newcastle_United_Logo.svg"},
    "Brighton": {"score": 65, "logo": "https://upload.wikimedia.org/wikipedia/en/f/fd/Brighton_%26_Hove_Albion_logo.svg"},
    "Aston Villa": {"score": 62, "logo": "https://upload.wikimedia.org/wikipedia/en/f/f9/Aston_Villa_FC_crest_%282016%29.svg"},
    "West Ham United": {"score": 60, "logo": "https://upload.wikimedia.org/wikipedia/en/c/c2/West_Ham_United_FC_logo.svg"},
    "Brentford": {"score": 55, "logo": "https://upload.wikimedia.org/wikipedia/en/2/2a/Brentford_FC_crest.svg"},
    "Crystal Palace": {"score": 50, "logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Crystal_Palace_FC_logo.svg"},
    "Fulham": {"score": 48, "logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Fulham_FC_%28shield%29.svg"},
    "Wolverhampton Wanderers": {"score": 45, "logo": "https://upload.wikimedia.org/wikipedia/en/f/fc/Wolverhampton_Wanderers.svg"},
    "Nottingham Forest": {"score": 42, "logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Nottingham_Forest_logo.svg"},
    "Bournemouth": {"score": 40, "logo": "https://upload.wikimedia.org/wikipedia/en/e/e5/AFC_Bournemouth_%282013%29.svg"},
    "Everton": {"score": 38, "logo": "https://upload.wikimedia.org/wikipedia/en/7/7c/Everton_FC_logo.svg"},
    "Burnley": {"score": 35, "logo": "https://upload.wikimedia.org/wikipedia/en/1/12/Burnley_FC_logo.svg"},
    "Sheffield United": {"score": 30, "logo": "https://upload.wikimedia.org/wikipedia/en/3/3e/Sheffield_United_FC_logo.svg"},
    "Luton Town": {"score": 25, "logo": "https://upload.wikimedia.org/wikipedia/en/3/36/Luton_Town_FC_badge.svg"}
}

# Create a DataFrame
teams = list(historical_scores.keys())
scores = [historical_scores[team]["score"] for team in teams]
logos = [historical_scores[team]["logo"] for team in teams]

data = {
    "Team": [f'<img src="{logo}" alt="{team} logo" width="20"/> {team}' for team, logo in zip(teams, logos)],
    "Historical Score": scores
}

df = pd.DataFrame(data)
df = df.sort_values(by="Historical Score", ascending=False).reset_index(drop=True)

# Add predicted positions
df["Position"] = df.index + 1

# Determine European and relegation spots
df["Champions League"] = df["Position"].apply(lambda x: "Yes" if x <= 4 else "No")
df["Europa League"] = df["Position"].apply(lambda x: "Yes" if 5 <= x <= 6 else "No")
df["Conference League"] = df["Position"].apply(lambda x: "Yes" if x == 7 else "No")
df["Relegation"] = df["Position"].apply(lambda x: "Yes" if x > 17 else "No")

# Select relevant columns for the final output
final_df = df[["Position", "Team", "Historical Score", "Champions League", "Europa League", "Conference League", "Relegation"]]

@app.route('/')
def index():
    return render_template('index.html', tables=[final_df.to_html(classes='data', index=False, escape=False, render_links=True)], titles=final_df.columns.values)

if __name__ == "__main__":
    app.run(debug=True)
