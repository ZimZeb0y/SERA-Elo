
import requests
import csv
import pandas as pd
import os

api_key=os.environ[SOME_SECRET]
dic={}
players=["Cs_oJay","Folke-","rekz","DEBRE","Rollo-_-",
         "Nordby","Marden","kjaer666","Hanth","SlyGoingFTW",
         "Boye-_-","julius777","entire-","MolO11","Bukhavez-",
         "gleerup","bamme","screens-","caze","L2PaaDetBeat",
         "Ekke","TroskiDk","_PatchI_","Ep1sk_","BqreBedre"]

for player in players:
    url = f"https://open.faceit.com/data/v4/players?game=cs2&nickname={player}"
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + api_key
    }
    response = requests.get(url, headers=headers)
    faceitdata = response.json()
    dic[player]=str(faceitdata["games"]["cs2"]["faceit_elo"])

try:
    os.remove("Sera Elo.csv")
except:
    pass

df = pd.DataFrame(dic,index=[1])
df.to_csv("Sera Elo.csv")
