import random
import numpy as np
import math
import matplotlib.pyplot as plt

def node():
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    return x, y

def draw():
    plt.title("初始節點")
    plt.xlim(xmax=100,xmin=0)
    plt.ylim(ymax=100,ymin=0)
    for i in coordinate:
        plt.scatter(i[0],i[1])
    coordinate.append(coordinate[0])
    for i in range(len(coordinate)-1):
        j = i+1
        plt.plot([coordinate[i][0],coordinate[j][0]],[coordinate[i][1],coordinate[j][1]])
    return

def distance_sum():
    distance_sum = 0
    for i in range(len(coordinate)-1):
        p1 = np.array(coordinate[i])
        p2 = np.array(coordinate[i+1])
        p3 = p2 - p1
        p4 = math.hypot(p3[0],p3[1])
        distance_sum = distance_sum + p4
    return distance_sum

def distance_each():
    distance_each = []
    for i in range(len(coordinate)-1):
        p1 = np.array(coordinate[i])
        p2 = np.array(coordinate[i+1])
        p3 = p2 - p1
        p4 = math.hypot(p3[0],p3[1])
        distance_each.append(p4)
    return distance_each

def visibility(x):
    return 1/x

node_num = int(input("你要幾個節點"))
coordinate = []

for i in range(node_num):
    coordinate.append(node())

draw()
    
print(coordinate) #目前節點順序
print(distance_each()) #節點之間距離
print(distance_sum()) #總距離
print(list(map(visibility,distance_each()))) #節點之間能見度



# random.choices(mylist, weights = [10, 1, 1], k = 1)

"""
node_begin = coordinate[0]
print(node_begin)
node_end = node_begin
coordinate.remove(node_begin)

for i in range(len(coordinate)):
    node = random.choice(coordinate)
    print(node)
    coordinate.remove(node)

print(node_end)
"""
plt.show()

