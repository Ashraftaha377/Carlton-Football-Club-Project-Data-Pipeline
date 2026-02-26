import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_matches():
    url = "https://afltables.com/afl/afl_index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # parse tables here
    # build list of matches
    
    data = []
    # append parsed rows

    df = pd.DataFrame(data, columns=[
        "date", "home_team", "away_team", 
        "home_score", "away_score", "venue"
    ])

    return df
