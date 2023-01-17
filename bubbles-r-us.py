scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
index = 0
total_tests = len(scores)

while (index < total_tests):
    # Print the bubble solution statement
    print("Bubble solution #" + str(index), "score:", scores[index])

    # Increment the index by 1
    index = index + 1

# The total amount of tests
print("Bubbles Tests:", total_tests)

# Highest score in the list
print("Highest bubble score:", max(scores))

# Solution with the highest score
max_score = max(scores) # 69
max_scores = [] # expected to equal [11, 18]

for i, score in enumerate(scores):
    if score == max_score:
        # append to max_scores the index value of score
        max_scores.append(i)

print("Solutions with highest score:", max_scores) # [11, 18]
