#write a loop that prints the following: cost #1: $ amount

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]


cost = len(costs)

for i in range(cost):
    fix = ' $' + str(costs[i])
    print('Cost #' + str(i), fix)

