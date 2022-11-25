import random
import numpy as np
import math
import matplotlib.pyplot as plt

# 創造隨機節點
def node(): 
    x = random.randint(1, 199)
    y = random.randint(1, 199)
    return x, y

# 畫圖
def draw():
    plt.title("初始節點")
    plt.xlim(xmax=200,xmin=0)
    plt.ylim(ymax=200,ymin=0)
    for i in coordinate:
        plt.scatter(i[0],i[1])
    coordinate.append(coordinate[0])
    for i in range(len(coordinate)-1):
        j = i+1
        plt.plot([coordinate[i][0],coordinate[j][0]],[coordinate[i][1],coordinate[j][1]])
    coordinate.pop()
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
    distance_all.sort()
    return distance_all

# 距離出現次數
def distance_time():
    for i in distance_each():
        distance_times.append(i)
    return

# 計算費洛蒙
def Pheromones():
    pheromones = []
    for i in range(len(coordinate)):
        p1 = np.array(coordinates[len(coordinates) - 1])
        p2 = np.array(coordinate[i])
        print(p1,p2)
        p3 = p2 - p1
        p4 = math.hypot(p3[0],p3[1])
        #if(p4):
         #   print(p2,p1)
        p5 = distance_times.count(p4)
        p5 = p5 * 100 / p4
        pheromones.append(p5)
    return pheromones

# 計算能見度
def visibility(x):
    return 1/x

node_num = int(input("你要幾個節點"))

coordinate = []
distance_times = []
    
for i in range(node_num):
    coordinate.append(node())

print("所有節點之間距離",distance_all())

for i in range(len(coordinate)):
    coordinate.sort()
    coordinates = []
    for j in range(len(coordinate)):
        node = random.choice(coordinate)
        coordinate.remove(node)
        coordinates.append(node)
    coordinate = coordinates

    #draw()
    coordinate.append(coordinate[0])
    #print("第",i+1,"次",coordinate) #目前節點順序
    #print("彼此間距離",distance_each()) #所有節點之間距離
    distance_each()
    distance_time()
    #print("總距離",distance_sum()) #總距離
    #print("能見度",list(map(visibility,distance_each()))) #所有之間能見度
    coordinate.pop()
    #plt.show()


print(coordinate)
coordinates = []
node = random.choice(coordinate)
coordinate.remove(node)
coordinates.append(node)

for i in range(node_num-1):
    for j in range(len(coordinate)):
        print("費洛蒙",Pheromones())
        node = random.choices(coordinate, weights = Pheromones() , k = 1)
        coordinate.remove(node[0])
        coordinates.append(node[0])
        print(coordinates)
    coordinate = coordinates

#print(distance_each())

#coordinate.append(coordinate[0])
#distance_each()
#distance_time()
    

#plt.show()


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


