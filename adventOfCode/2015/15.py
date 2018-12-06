ingreds ={
    "Sprinkles": [5, -1, 0, 0, 5],
    "PeanutButter": [-1, 3, 0, 0, 1],
    "Frosting": [0, -1, 4, 0, 6],
    "Sugar": [-1, 0, 0, 2, 8],
}

best_score = 0

for sprinkles in range(0, 100 + 1):
    for butter in range(0, 100 + 1 - sprinkles):
        for frosting in range(0, 100 + 1 - sprinkles - butter):
            sugar = 100 - sprinkles - butter  - frosting
            score = 1
            for i in range(4):
                score *= max(0, sprinkles * ingreds["Sprinkles"][i] + \
                    butter * ingreds["PeanutButter"][i] + \
                    frosting * ingreds["Frosting"][i] + \
                    sugar * ingreds["Sugar"][i])

            calories = sprinkles * ingreds["Sprinkles"][4] + \
                       butter * ingreds["PeanutButter"][4] + \
                       frosting * ingreds["Frosting"][4] + \
                       sugar * ingreds["Sugar"][4]
            if score > best_score and calories == 500:
                best_score = score
                print score, sprinkles, butter, frosting, sugar
