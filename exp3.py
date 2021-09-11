cost1 = [2,3,11,7]
cost2=[1,0,6,1]
cost3=[5,8,15,9]
supply= [6,1,10]
dem= [7,5,3,2]
cm1= list.copy(cost1)
cm2=list.copy(cost2)
cm3=list.copy(cost3)
cm1.sort()
cm2.sort()
cm3.sort()
cost=0
print('Transporation Model\n')
print('Supply from Plants 1-4 is',supply)
print('Demand for Centres 1-4 is',dem)
for i in range(4):
	if(supply[0]==0):
		break
	for j in range(4):
		if(cm1[i]==cost1[j] and dem[i]!=0):
			if(dem[j]>supply[0]):
				cost+=cm1[i]*supply[0]
				dem[j]=dem[j]-supply[0]
				supply[0]=0
		if(supply[0]==0):
			break

for i in range(4):
	if(supply[1]==0):
		break
	for j in range(4):
		if(cm2[i]==cost2[j]):
			if(dem[j]>supply[1]):
				
				cost+=cost2[j]*supply[1]
				dem[j]=dem[j]-supply[1]
				supply[1]=0
			if(supply[1]==0):
				break	

for i in range(4):
	cost=cost+cost3[i]*dem[i]
	supply[2]=supply[2]-dem[i]
	dem[i]=0

print('   C1 C2 C3  C4')
print('P1',cost1)
print('P2',cost2)
print('P3',cost3)

print('The cost for transporation is: Rs',cost*100) 



