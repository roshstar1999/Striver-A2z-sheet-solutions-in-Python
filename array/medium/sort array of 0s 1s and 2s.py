

def sortArray(arr, n):
	count0,count1,count2=0,0,0
	# Write your code here
	for i in arr:
		if i==0:
			count0+=1
		elif i==1:
			count1+=1
		else:
			count2+=1
	for i in range(len(arr)):
		if i<count0:
			arr[i]=0
		elif i<count0+count1:
			arr[i]=1
		elif i<count0+count1+count2:
			arr[i]=2
		
