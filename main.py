from matplotlib import pyplot as plt
import numpy as np
sum_error = 0
iterations= 10000000
data = [[1,3],
        [2,5],
        [3,7],
        [4,9],
        [5,11],
        [6,13]]
learning_rate = 0.1
Q0 = np.random.randn()
Q1 = np.random.randn()
print("ILK DEGERLER",Q0,"------",Q1)
def vis_data():
    plt.grid()

    for i in range(len(data)):
        c = 'r'
        plt.scatter([data[i][0]], [data[i][1]], c=c)

    plt.show()




def hypothesis(a):
    return (Q0+Q1*a)


for j in range (iterations):
    ri = np.random.randint(len(data))
    point = data[ri]

    print(j,". DEGERLERİ",Q0,"------------",Q1)
    squared_error = ((hypothesis(point[0])-point[1])**2)
    print(j,". Squared Error Degeri",squared_error)
    sum_error += squared_error/6
    tempQ0 = Q0 - learning_rate* ((hypothesis(point[0])-point[1])/3)
    tempQ1 = Q1 - learning_rate*((((hypothesis(point[0])-point[1]))*point[0])/3)
    Q1 = tempQ1
    Q0 = tempQ0
    if (squared_error==0):
            break
print("Toplam Error",sum_error)

print("7 için tahmin",hypothesis(7))
for i in range (15):
    plt.plot (i,hypothesis(i),'bo')
vis_data()
