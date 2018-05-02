import pandas as pd

tweet_df = pd.read_csv('tweets.csv')

fechas = tweet_df["created_at"]
print(fechas)

soloHoraMinutoSegundo = [elemento[11:19] for elemento in fechas]
print(soloHoraMinutoSegundo)

soloEnSegundo19 = [elemento[11:19] for elemento in fechas if elemento[17:19] == "19"]
print(soloEnSegundo19)

soloEnSegundo19 = [elemento[11:19] if elemento[17:19] == "19" else "" for elemento in fechas ]
print(soloEnSegundo19)

soloSegundo17 = [elemento for elemento in fechas if elemento[17:19] == "17"]
print(soloSegundo17)