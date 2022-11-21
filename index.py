import random

def node():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    return x, y

node_num = int(input("你要幾個節點"))
coordinate = []

for i in range(node_num):
    coordinate.append(node())

print(coordinate)

a = np.array([1,2])