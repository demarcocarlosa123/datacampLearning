import pandas as pd

tweet_df = pd.read_csv('tweets.csv')

#Quiero imprimir solo los reteets
resultado = filter(lambda tweet: tweet[0:2]=="RT",tweet_df["text"])
print(list(resultado))


#Ahora lo mismo pero armando una funcion que se pueda llamar varias veces
def count_group_by(dataFrame, columBy="lang"):
    """Return a dictionary with counts of occurrences as value for each key."""
    countVeces = {}
    try:
        for entry in dataFrame[columBy]:
            if entry in countVeces.keys():
                countVeces[entry] = countVeces[entry] + 1
            else:
                countVeces[entry] = 1
        return countVeces
    except:
        print("No existe el nombre de columna: " + columBy)
output1 = count_group_by(tweet_df, "lang")
output2 = count_group_by(tweet_df, "long")
print(output1)
print(output2)
