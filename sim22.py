from collections import deque
import numpy as np
from scipy.special import comb
import random
import matplotlib.pyplot as plt



experimentCount = 10**6
arrivalRate =  [0.2, 0.3, 0.4, 0.45, 0.49, 0.495];
departureRate = 0.5
dict = {}

queueDelay = []

for i in range(len(arrivalRate)):
    delay=0
    servers_jobs = [0, 0, 0, 0, 0]
    arrRate = arrivalRate[i]
    jobcount = 5 * arrRate
    noJobRate = comb(5, 0) * (1 - arrRate)**5
    oneJobRate = comb(5, 1) * arrRate ** 1 * (1 - arrRate)**4
    twoJobsRate = comb(5, 1) * arrRate ** 2 * (1 - arrRate)**3
    threeJobsRate = comb(5, 1) * arrRate ** 3 * (1 - arrRate)**2
    fourJobsRate = comb(5, 1) * arrRate ** 4 * (1 - arrRate)**1
    fiveJobsRate = comb(5, 1) * arrRate ** 5
    queueLength=0
    queue1 = deque()
    queue2 = deque()
    queue3 = deque()
    queue4 = deque()
    queue5 = deque()
    for j in range(experimentCount):
        job_number=0
        rate = random.random()
        if(rate < fiveJobsRate):
            job_number = 5
        elif(rate < fourJobsRate):
            job_number = 4
        elif(rate < threeJobsRate):
            job_number = 3
        elif(rate < twoJobsRate):
            job_number = 2
        elif(rate < oneJobRate):
            job_number = 1
        else: #no job detected
            job_number =0

        for k in range(job_number):
            if(servers_jobs.index(min(servers_jobs)) == 0):
                queue1.append(j)
                servers_jobs[0] = len(queue1)
            elif(servers_jobs.index(min(servers_jobs)) == 1):
                queue2.append(j)
                servers_jobs[1] = len(queue2)
            elif(servers_jobs.index(min(servers_jobs)) == 2):
                queue3.append(j)
                servers_jobs[2] = len(queue3)
            elif(servers_jobs.index(min(servers_jobs)) == 3):
                queue4.append(j)
                servers_jobs[3] = len(queue4)
            elif(servers_jobs.index(min(servers_jobs)) == 4):
                queue5.append(j)
                servers_jobs[4] = len(queue5)




        if(random.random() < departureRate and len(queue1)>0):
                out = j - queue1.popleft()
                delay += out
                if(arrRate == 0.45):
                    if(dict.get(out)):
                        dict[out] += 1
                    else:
                        dict[out] = 1
                servers_jobs[0] = len(queue1)
        if(random.random() < departureRate and len(queue2) > 0):
                out = j - queue2.popleft()
                delay += out
                if(arrRate == 0.45):
                    if(dict.get(out)):
                        dict[out] += 1
                    else:
                        dict[out] = 1
                servers_jobs[1] = len(queue2)
        if(random.random() < departureRate and len(queue3) > 0):
                out = j - queue3.popleft()
                delay += out
                if(arrRate == 0.45):
                    if(dict.get(out)):
                        dict[out] += 1
                    else:
                        dict[out] = 1
                servers_jobs[2] = len(queue3)
        if(random.random() < departureRate and len(queue4) > 0):
                out = j - queue4.popleft()
                delay += out
                if(arrRate == 0.45):
                    if(dict.get(out)):
                        dict[out] += 1
                    else:
                        dict[out] = 1
                servers_jobs[3] = len(queue4)
        if(random.random() < departureRate and len(queue5) > 0):
                out = j - queue5.popleft()
                delay += out
                if(arrRate == 0.45):
                    if(dict.get(out)):
                        dict[out] += 1
                    else:
                        dict[out] = 1
                servers_jobs[4] = len(queue5)

    print(delay/experimentCount)
    queueDelay.append(delay/experimentCount)


xBar=[]
yBar=[]
for key in dict.keys():
    xBar.append(key)
for val in dict.values():
    yBar.append(val)
plt.bar(xBar,yBar)
plt.xlabel('Possible Delay')
plt.ylabel('Number of Jobs')
plt.title('Q2: Arrival Rate : 0.45')
plt.show()
plt.plot(arrivalRate, queueDelay)
plt.xlabel('Arrival Rate')
plt.ylabel('Average Delay')
plt.title('Q1')
plt.show()
