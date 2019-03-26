import numpy as np
import pandas as pd

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

baseball = pd.read_csv("baseball/core/Batting.csv")
players = pd.read_csv("baseball/core/People.csv")

print(baseball)
mostHits = baseball.loc[baseball['H'].idxmax()]

print(mostHits)

print(players.loc[players['playerID'] == mostHits['playerID'] ]['nameFirst'])

mostHits = baseball.loc[baseball['HR'].idxmax()]

print(players.loc[players['playerID'] == mostHits['playerID'] ]['nameLast'])

mostHits = baseball.loc[baseball['3B'].idxmax()]

print(players.loc[players['playerID'] == mostHits['playerID'], ['nameFirst', 'nameLast']])

mostHits = baseball.loc[baseball['playerID'] == 'suzukic01', ['H', 'HR']].sum()

print(mostHits)

mostKs = baseball.groupby(['playerID'])['SO'].agg('sum').idxmax()

print(players.loc[players['playerID'] == mostKs, ['nameFirst', 'nameLast']])