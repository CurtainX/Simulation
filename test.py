import matplotlib.pyplot as plt
ff=[8.5280000000000005, 76.299000000000007, 742.50199999999995]
bf=[8.5809999999999995, 75.856999999999999, 737.85799999999995]
n=[10,100,1000]

plt.plot(n,ff)
plt.plot(n,bf)
plt.title('Lab3')
plt.xlabel('N')
plt.ylabel('Average number of servers')

plt.legend(['First Fit', 'Best Fit'])
plt.show()