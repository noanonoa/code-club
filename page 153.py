scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 80, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
high_score = 0
i = 0

for score in scores:
    if score > high_score:
        high_score = score
        print(high_score)
