ListScores = [10, 3, 6, 9, 7, 12, 15, 20, 14, 15, 19, 18, 9, 2, 3, 11]


def MoreThan15(Score):
    return Score >= 15

# Filter
print(list(filter(MoreThan15, ListScores)))
# Output:
    # [15, 20, 15, 19, 18]

# Lambda Expression
lambda Score: Score >= 15

# Use Lambda Expression
print(list(filter(lambda Score: Score >= 15, ListScores)))
# Output:
    # [15, 20, 15, 19, 18]


# Lambda for Power two
print(list(map(lambda Score: Score**2, ListScores)))
# Output:
    # [100, 9, 36, 81, 49, 144, 225, 400, 196, 225, 361, 324, 81, 4, 9, 121]

