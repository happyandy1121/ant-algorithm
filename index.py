import random
import numpy as np
import math
import matplotlib.pyplot as plt

# 創造隨機節點
def node(): 
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    return x, y

# 畫圖
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

# 計算總距離
def distance_sum():
    distance_sum = 0
    for i in range(len(coordinate)-1):
        p1 = np.array(coordinate[i])
        p2 = np.array(coordinate[i+1])
        p3 = p2 - p1
        p4 = math.hypot(p3[0],p3[1])
        distance_sum = distance_sum + p4
    return distance_sum

# 計算節點之間距離
def distance_each():
    distance_each = []
    for i in range(len(coordinate)-1):
        p1 = np.array(coordinate[i])
        p2 = np.array(coordinate[i+1])
        p3 = p2 - p1
        p4 = math.hypot(p3[0],p3[1])
        distance_each.append(p4)
    return distance_each

# 計算所有節點之間距離
def distance_all():
    distance_all = []
    for i in range(len(coordinate)-1):
        for j in range(i+1,len(coordinate)):
            p1 = np.array(coordinate[i])
            p2 = np.array(coordinate[j])
            p3 = p2 - p1
            p4 = math.hypot(p3[0],p3[1])
            distance_all.append(p4)
    return distance_all

# 計算能見度
def visibility(x):
    return 1/x

node_num = int(input("你要幾個節點"))
coordinate = []

for i in range(node_num):
    coordinate.append(node())

draw()
coordinate.pop()
coordinate.sort()
print("所有節點之間距離",distance_all())

for i in range(len(coordinate)):
    coordinate.sort()
    coordinates = []
    for j in range(len(coordinate)):
        node = random.choice(coordinate)
        coordinate.remove(node)
        coordinates.append(node)
    coordinate = coordinates

    draw()
    print("第",i+1,"次",coordinate) #目前節點順序
    coordinate.pop()
    #plt.show()

    print("彼此間距離",distance_each()) #所有節點之間距離
    print("總距離",distance_sum()) #總距離
    print("能見度",list(map(visibility,distance_each()))) #所有之間能見度

plt.show()

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


