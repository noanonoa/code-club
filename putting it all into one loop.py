scores = [60, 50, 60, 58, 54, 54, 58,
          50, 52, 54, 48, 69, 34, 55,
          51, 52, 44, 51, 69, 64, 66,
          55, 52, 61, 46, 31, 57, 52,
          44, 18, 41, 53, 55, 61, 51, 44]


costs = [.25, .27, .25, .25, .25, .25, .33,
         .31, .25, .29, .27, .22, .31, .25,
         .25, .33, .21, .25, .25, .25, .28,
         .25, .24, .22, .20, .25, .30, .25,
         .24, .25, .25, .25, .27, .25, .26, .29]

best_solutions = []

high_score = 0
length = len(scores)
cost = 100.0
most_effective = 0
index = best_solutions[i]

for i in range(length):
    if scores[i] > high_score:
        high_score = scores[i]
    if scores[i] == high_score:     
        best_solutions.append(i)
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]

#print Bubble solutions
print('Bubble solution #' + str(i), 'score:', scores[i])
   
#print number of bubble tests
print('Bubbles tests:', length)
    
#print the highest bubble score
print('Highest bubble score:', high_score)

#print the solutions with the highest score
print('Solutions with the highest score:', best_solutions)

#print the most effective solution and its related cost
print('Solution', most_effective,
      'is the most effective with a cost of', costs[most_effective])
