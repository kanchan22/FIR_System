import numpy as np
import matplotlib.pyplot as plt

def place_bar():
	clist =['vishrambag','kupwad','miraj','kupwad','nashik','miraj','kupwad','kupwad','miraj','kupwad','kupwad','miraj','kupwad','vishrambag','miraj','kupwad','nashik','kupwad','vishrambag','nashik','miraj','kupwad','vishrambag','kupwad','vishrambag','kupwad']

	set1 = set(clist)

	list2 = list(set1)
	 
	llist = list2
	print llist
	y_pos = np.arange(len(list2))
	list3 = []
	count = 0
	for year in list2:
		count=0

		for year1 in clist:
		
			if year1 == year:
				count = count + 1
		list3.append(count)

	print list2
	print list3
	list4 = []
	#for ele in list3:
		#list4.append(ele2)
	#print list4

	plt.bar(y_pos ,list3 ,align='center' ,alpha=0.5)
	plt.xticks(y_pos , list2)
	#plt.yticks(list , list3)
	plt.ylabel('crime Rate')
	plt.xlabel('Crime Frequency')
	plt.title('Total Crime Rate in Respective Years ')

	plt.show()
	
		#print crime,clist.count(crime)
		#list3.append(clist.count(crime))

	'''year = [2012,2013,2014,2015,2016,2017]
	y_pos = np.arange(len(year))


	plt.bar(y_pos, list3)
	plt.show()'''
