# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import random
Global = []

def find(DICE, Goal, counts, F, sum = 0,  Values = []):
    temp = sum
    if counts > F:
        return
    else:   
        if temp == Goal and Values != None:
            Global.append(Values)
        
        if temp >= Goal:
            return 

        for index in range(len(DICE)):
            t = DICE[index]
            find(DICE, Goal, counts + 1, F,sum + t, Values + [t])

def solution(A, F, M):
    # write your code in Python 3.6
    SUM_required = (M*(len(A) + F)) - sum(A)
    DICE = DICE = [1, 2, 3, 4, 5, 6]
    if SUM_required > 6*len(A):
        return [0]
    
    else:
        find(DICE, SUM_required, 0, F)
        i = random.randint(0, len(Global))

        return Global[i]
    
if __name__ == "__main__":
    print(solution([3, 2, 4, 3], 2, 4))