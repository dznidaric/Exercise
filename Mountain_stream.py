import sys
import math
import numpy as np

C = int(input("the number of points closest to the origin that we need to print: "))
zpoint = np.array([0, 0], ndmin=2)
points = []
min_list = []
min_distance = 0

def menu():
    print("\nMenu")
    print("----------------")
    print("1. Input another point by specifying its coordinates")
    print("2. Query the program to give us C points closest to the origin of the coordinate system (point (0, 0))")
    print("3. Terminate the program")
    option = int(input())

    if(option == 1):
        X, Y = map(int, input().split())
        points.append((X, Y))
        menu()

    
    elif(option == 2):
        sortArr(points, zpoint, C)
        menu()
    
    elif(option == 3):
        sys.exit(0)

    else:
        menu()


def sortArr(arr, zeroArr, C): 
    vp = []

    for i in range(len(points)): 
        distance = pow((arr[i][0] - zpoint[0][0]), 2) + pow((arr[i][1] - zpoint[0][1]), 2) 
        vp.append([distance, [arr[i][0], arr[i][1]]]) 
          
    vp.sort()
      
    for i in range(C): 
        print("(", vp[i][1][0], ", ",vp[i][1][1], ") ", sep="", end="\n") 

    print("")


menu()
