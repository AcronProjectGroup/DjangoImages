ListScores = [10, 3, 6, 9, 7, 12, 15, 20, 14, 15, 19, 18, 9, 2, 3, 11]


def MoreThan15(Score):
    return Score >= 15

# Filter
print(list(filter(MoreThan15, ListScores)))

# Lambda Expression
lambda Score: Score >= 15

# Use Lambda Expression
print(list(filter(lambda Score: Score >= 15, ListScores)))


