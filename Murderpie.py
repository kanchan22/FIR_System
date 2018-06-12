import matplotlib.pyplot as plt

def murder_pie():

	ylist = ['kidnapping','murder','cyber_crime','kidnapping','murder','kidnapping','murder','kidnapping','kidnapping','robbery','robbery','murder','robbery','robbery','robbery','robbery','robbery','robbery','robbery','robbery','robbery','murder','murder','murder','murder','murder']

	clist = ['nashik','visrambag','kupwad','miraj','miraj','miraj','miraj','visrambag','visrambag','visrambag','visrambag','visrambag','visrambag','nashik','kupwad','nahsik','kupwad','kupwad','kupwad','nashik','kupwad','nashik','kupwad','kupwad','kupwad','kupwad',]

	nlist = []
	colist = []
	for i in range(len(ylist)):
		if ylist[i] == 'murder':
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


	slices = colist
	activities = list2
	cols = ['y' ,'r' , 'g','b']
	#explode = (0.06,0.06,0.06,0.06)
	explode = (0.02,0.02,0.02,0.02)

	plt.pie(slices, explode=explode ,labels=lcrime, colors=cols, autopct='%1.1f%%',shadow=True ,startangle=140)

	plt.axis('equal')
	plt.title('Murder Percentage In Different Cities')
	#plt.ylabel('2000 crime Rate')
	#plt.xlabel('X axis')
	plt.legend()
	plt.show()

