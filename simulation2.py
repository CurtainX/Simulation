import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
class Simulator:
	PACKAGE_LENGTH=0
	CHANNEL_CAPACITY=0
	TIME_OUT=0
	PROPERGATION_DELAY=0
	TIMER=0
	BER=0
	PACKAGE_COUNT=0
	PACKAGE_DELAY=0
	PACKAGE_TO_SEND=0 #number of packages
	def __init__(self,H,l,timeout,channel_capacity,proprogation_delay,ber,packagetosend):
		self.PACKAGE_LENGTH=H+l
		self.TIME_OUT=timeout
		self.CHANNEL_CAPACITY=channel_capacity
		self.PROPERGATION_DELAY=proprogation_delay
		self.BER=ber
		self.PACKAGE_TO_SEND=packagetosend
		self.PACKAGE_DELAY=(H+l)/channel_capacity+H/channel_capacity+proprogation_delay*2/1000
	def send(self):
		check_result=0
		error_bit_num=0
		noerror=(1-self.BER)**(self.PACKAGE_LENGTH*8)
		one2fourerrors=self.BER*(1-self.BER)**(self.PACKAGE_LENGTH*8-1)
		+self.BER**2*(1-self.BER)**(self.PACKAGE_LENGTH*8-2)+self.BER**3*(1-self.BER)**(self.PACKAGE_LENGTH*8-3)
		+self.BER**4*(1-self.BER)**(self.PACKAGE_LENGTH*8-4)
		morethan4errors=1-noerror-one2fourerrors
		for num in range(self.PACKAGE_TO_SEND):
			seednum=np.random.uniform(0,1)
			if(seednum<noerror):
				self.TIMER+=self.PACKAGE_DELAY
			elif(seednum<one2fourerrors):
				self.PACKAGE_TO_SEND+=1
				self.TIMER+=self.PACKAGE_DELAY
			elif(seednum<morethan4errors):
				self.TIMER+=self.TIME_OUT
				self.PACKAGE_TO_SEND+=1
	def getThroughput(self):
		throughput=self.PACKAGE_TO_SEND/self.TIMER
		return throughput



#prepare timeout value
timeout_index=np.array([2.5,5,7.5,10,12.5])
timeout_one=timeout_index*5/1000
timeout_two=timeout_index*250/1000
#function for plot the result
def plotResult(timeout,proprogation_delay):
	holder0=[]
	holder1=[]
	holder2=[]
	for j in range(len(timeout)):
		sim0=Simulator(54*8,1500*8,timeout[j],5*1024**2,proprogation_delay,0,10000)
		sim1=Simulator(54*8,1500*8,timeout[j],5*1024**2,proprogation_delay,10**-4,10000)
		sim2=Simulator(54*8,1500*8,timeout[j],5*1024**2,proprogation_delay,10**-5,10000)
		sim0.send()
		sim1.send()
		sim2.send()
		holder0.append(sim0.getThroughput())
		holder1.append(sim1.getThroughput())
		holder2.append(sim2.getThroughput())
	table={'Timeout':timeout_index,'BER=0.0':holder0,'BER=1e-5':holder2,'BER=1e-4':holder1}
	dataframe=pd.DataFrame(table)
	print('Propagation Delay*2= '+str(proprogation_delay*2)+' s')
	print(dataframe)
	plt.plot(timeout,holder0,label='BER=0')
	plt.plot(timeout,holder1,label='BER=10**-4')
	plt.plot(timeout,holder2,label='BER=10**-5')
	plt.title('Propagation Delay*2= '+str(proprogation_delay*2)+' ms')
	plt.xlabel('Timeout(s)')
	plt.ylabel('Throughput(ptk/s)')
	plt.xticks(timeout)
	plt.legend()
	plt.show()



#function call for get plot result
plotResult(timeout_one,5)
plotResult(timeout_two,250)
