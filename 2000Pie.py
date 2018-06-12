import matplotlib.pyplot as plt

def pie():
	ylist = [2001,2002,1999,2001,2002,2001,2002,2001,2001,2003,2000,2003,2000,2000,2000,2000,2000,2000,2000,2000,2000,2003,2003,2003,2003,2003]

	clist = ['kidnapping','murder','cyber_crime','robbery','accident','accident','accident','robbery','robbery','robbery','robbery','robbery','robbery','murder','kidnapping','kidnapping','kidnapping','kidnapping','kidnapping','kidnapping','kidnapping','kidnapping','kidnapping','kidnapping','cyber_crime','cyber_crime',]

	nlist = []
	colist = []
	for i in range(len(ylist)):
		if ylist[i] == 2000:
			nlist.append(clist[i])

	print nlist

	set1 = set(nlist)

	list2 = list(set1)
	 
	lcrime = list2

	for crime in list2:
			print crime,nlist.count(crime)
			colist.append(nlist.count(crime))
	print colist

	#years = [2001,2002,2003,2004]

	'''murder = [4,5,2,3]
	kidnappingidnapping = [1,2,1,3]
	accident = [12,13,40,57]
	'''

	slices = colist
	activities = list2
	cols = ['y' ,'r' , 'g']
	explode = (0.1,0.1,0.1)

	plt.pie(slices, explode=explode ,labels=lcrime, colors=cols, autopct='%1.1f%%',shadow=True ,startangle=140)

	plt.axis('equal')
	#plt.title('2000 crime Rate')
	plt.ylabel('2000 crime Rate')
	#plt.xlabel('X axis')
	plt.legend()
	plt.show()

