import cvxpy
import numpy as np
import sys


maxCredits = 0
solutionArr = []
# The data for the Knapsack problem
# P is total weight capacity of sack
# weights and utilities are also specified
T = int(input())
N = int(input())

timeList = list(map(int, input().split()))
creditsList = list(map(int, input().split()))

timeArray = np.array(timeList)
creditsArray = np.array(creditsList)

# The variable we are solving for
selection = cvxpy.Variable(len(timeArray),boolean = True)

# The sum of the time should be less than or equal to T
time_constraint = timeArray @ selection <= T

# Our total utility is the sum of the item utilities
total_credits = creditsList @ selection

# Maximize total credits
# subject to weight_constraint. All constraints in 
# cvxpy must be passed as a list
webinar_problem = cvxpy.Problem(cvxpy.Maximize(total_credits), [time_constraint])

# Solving the problem
webinar_problem.solve(solver = cvxpy.GLPK_MI)

print()
for i in range (len(selection.value)):
    if (int(selection.value[i]) == 1):
        maxCredits += creditsArray[i] 
        solutionArr.append([timeArray[i], creditsArray[i]])

print(maxCredits)

finalArr = np.array(solutionArr)
np.savetxt(sys.stdout.buffer, finalArr, fmt="%i")

    