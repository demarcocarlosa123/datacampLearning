import pandas as pd

tweet_df = pd.read_csv('tweets.csv')
countVecesIdioma = {}

for idioma in tweet_df["lang"]:
    if idioma in countVecesIdioma.keys():
        countVecesIdioma[idioma] = countVecesIdioma[idioma] + 1
    else:
        countVecesIdioma[idioma] = 1
print(countVecesIdioma)


#Ahora lo mismo pero armando una funcion que se pueda llamar varias veces
def count_group_by(dataFrame, columBy):
    """Return a dictionary with counts of occurrences as value for each key."""
    countVeces = {}
    for entry in dataFrame[columBy]:
        if entry in countVeces.keys():
            countVeces[entry] = countVeces[entry] + 1
        else:
            countVeces[entry] = 1
    return countVeces
output1 = count_group_by(tweet_df, "lang")
output2 = count_group_by(tweet_df, "source")
print(output1)
print(output2)


#Ahora lo mismo pero armando una funcion que se pueda llamar varias veces
def count_group_by_variable(dataFrame, *args):
    """Return a dictionary with counts of occurrences as value for each key."""
    countVeces = {}
    for columa in args:
        for element in dataFrame[columa]:
            if element in countVeces.keys():
                countVeces[element] = countVeces[element] + 1
            else:
                countVeces[element] = 1
    return countVeces

output3 = count_group_by_variable(tweet_df, "lang")
output4 = count_group_by_variable(tweet_df, "lang", "source")
print(output3)
print(output4)











