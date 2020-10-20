import sys
import math
import numpy as np


while True:
    try:
        C = int(input("\nthe number of points closest to the origin that we need to print: "))

        if (C < 1 or C > 106):
            raise ValueError
        break
    except ValueError:
        print("\nInvalid integer. The number must be in the range of 1 and 106.")

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
        while True:
            try:
                X, Y = input("\nEnter two points here: ").split()
                X, Y = [int(X), int(Y)]         #map(int, input().split())
                
        
                if ((X < -1000 or X > 1000) or (Y < -1000 or Y > 1000)):
                    raise ValueError
                break
            except ValueError:
                print("Invalid integer. The number must be in the range of -1000 and 1000.")
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
