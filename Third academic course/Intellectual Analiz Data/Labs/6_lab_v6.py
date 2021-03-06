import matplotlib.pyplot as plt
import random as rand
import math

m = 0.1
sigma = 0.3
N = 25


def evklid2d(a = [],b = []):
    if a == b:
        return 666
    sum = 0
    for i,j in zip(a,b):
        sum += (i - j)**2
    return math.sqrt(sum)

def gen():
    eps = eps = math.sqrt(12/5) * (sum([rand.uniform(0,1) for i in range(5)]) - 5/2)
    return m + sigma * (0.01 * eps * (97 + eps ** 2))

data_0_0 = []
while (len(data_0_0) < 25):
    data_0_0.append([gen(),gen(),"r"])

data_1_1 = []
while (len(data_1_1) < 25):
    data_1_1.append([gen() + 1,gen() + 1,'g'])

data_3_1 = []
while (len(data_3_1) < 25):
    data_3_1.append([gen() + 3,gen() + 1, 'b'])





plt.figure()
plt.title("Вхідні дані")
plt.subplots_adjust(bottom=0.045, right=0.98, top=0.95, left=0.03)


for i in [[0,0],[1,1],[3,1]]:
    plt.scatter(i[0],i[1], color = "black")

for j in [data_0_0,data_1_1,data_3_1]:
    for i in j:
        plt.scatter(i[0],i[1], s = 5 , c = i[2])

plt.axvline(0)
plt.axhline(0)
plt.grid()





###############################################################


data = data_0_0 + data_1_1 + data_3_1
T = [sigma, sigma * 2 , sigma * 4]
subplot = [131,132,133]
plt.figure()

plt.subplots_adjust(bottom=0.045, right=0.98, top=0.95, left=0.03)

for k,sub in zip(T,subplot):
    counter = 1
    clusters = [
        {
            "xy" : [data[0][0], data[0][1]],
            "cluster" : [[data[0][0], data[0][1]],],
            "name" : counter
        },
    ]



    for i in data:
        distances = []
        for j in clusters:
            distances.append(evklid2d(i,j["xy"]))

        # print(distances,'\t Дистанція')
        # print(min(distances),'\t мінімальна дистанція')
        # print(distances.index(min(distances)),'\t індекс мінімальної дистанції')
        # print(clusters[distances.index(min(distances))],'\t кластер, до якого відстань мінімальна')
        # print(clusters[distances.index(min(distances))]['xy'],'\t координата кластера')
        # print(clusters[distances.index(min(distances))]["cluster"],'\t кластер')

        if (min(distances) > k):
            counter += 1
            clusters.append(
                {
                    "xy" : [i[0],i[1]],
                    "cluster" : [[i[0],i[1]],],
                    "name" : counter
                }
            )
        else:
            clusters[distances.index(min(distances))]["cluster"].append([i[0],i[1]])

    plt.subplot(sub)
    plt.title("T = " + str(k))
    for i in clusters:
        colors = [(rand.random(),rand.random(),rand.random())]
        for j in i['cluster']:
            plt.scatter(j[0],j[1], color = colors , s = 15)
            plt.text(j[0] + 0.02 , j[1] + 0.02 , s = i['name'] , fontsize = 8)
        plt.scatter(i['xy'][0],i['xy'][1], color = colors , s = 50)
        text = str(i["name"]) + "+"
        plt.text(i['xy'][0] + 0.02 , i['xy'][1] + 0.02, s = text, fontsize = 8)

    for i in [[0,0],[1,1],[3,1]]:
        plt.scatter(i[0],i[1], color = "black")

    plt.axvline(0)
    plt.axhline(0)
    plt.grid()










############################

plt.figure()
plt.subplots_adjust(bottom=0.045, right=0.98, top=0.95, left=0.03)

counter = 1
clusters = [
    {
        "xy" : [data[0][0], data[0][1]],
        "cluster" : [[data[0][0], data[0][1]],],
        "name" : counter
    },
]



for i in data:
    distances = []
    for j in clusters:
        distances.append(evklid2d(i,j["xy"]))

    # print(distances,'\t Дистанція')
    # print(min(distances),'\t мінімальна дистанція')
    # print(distances.index(min(distances)),'\t індекс мінімальної дистанції')
    # print(clusters[distances.index(min(distances))],'\t кластер, до якого відстань мінімальна')
    # print(clusters[distances.index(min(distances))]['xy'],'\t координата кластера')
    # print(clusters[distances.index(min(distances))]["cluster"],'\t кластер')

    if (min(distances) > T[2]):
        counter += 1
        clusters.append(
            {
                "xy" : [i[0],i[1]],
                "cluster" : [[i[0],i[1]],],
                "name" : counter
            }
        )
    else:
        clusters[distances.index(min(distances))]["cluster"].append([i[0],i[1]])

plt.title("T = " + str(k))
for i in clusters:
    colors = [(rand.random(),rand.random(),rand.random())]
    for j in i['cluster']:
        plt.scatter(j[0],j[1], color = colors , s = 15)
        plt.text(j[0] + 0.02 , j[1] + 0.02 , s = i['name'] , fontsize = 8)
    plt.scatter(i['xy'][0],i['xy'][1], color = colors , s = 50)
    text = str(i["name"]) + "+"
    plt.text(i['xy'][0] + 0.02 , i['xy'][1] + 0.02, s = text, fontsize = 8)

for i in [[0,0],[1,1],[3,1]]:
    plt.scatter(i[0],i[1], color = "black")

plt.axvline(0)
plt.axhline(0)
plt.grid()






plt.show()
