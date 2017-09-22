import random
import matplotlib.pyplot as plt
import numpy as np

def expectedDelay(arrivalRate):
    delay=[]
    avgDelay=[]
    for rate in arrivalRate:
        queue=0
        delay=[]
        for i in range(10**6):
            if(random.random()<rate):
                queue+=1
            if(random.random()<0.6):
                queue-=1
                if(queue<0):queue=0
            delay.append(queue)
        avgDelay.append(np.mean(delay))
    plt.plot(arrivalRate,avgDelay)
    plt.xlabel('Arrival Rate')
    plt.ylabel('Average Queuing Time')
    plt.show()        
expectedDelay([0.2,0.3,0.4,0.45,0.5,0.52,0.56,0.58,0.59])