import pandas as pd


#Ahora lo mismo pero armando una funcion que se pueda llamar varias veces
def count_group_by(file, size, columBy):
    """Return a dictionary with counts of occurrences as value for each key."""
    countVeces = {}
    chunkDataFrameIterator = pd.read_csv(file, chunksize=size)
    for chunk in chunkDataFrameIterator:
        for entry in chunk[columBy]:
            if entry in countVeces.keys():
                countVeces[entry] = countVeces[entry] + 1
            else:
                countVeces[entry] = 1
    return countVeces
output1 = count_group_by("files/tweets.csv", 10, "lang")
print(output1)
