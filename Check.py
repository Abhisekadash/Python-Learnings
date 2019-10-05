def Check_max(file_name):
	try:
		f=open(file_name,"r")
	except FileNotFoundError:
		f=open("F:\Python\story.txt","r")
	str1=f.read().split()
	dict={}
	for x in range(len(str1)):
		counter=0
		for y in range(len(str1)):
			if str1[x]==str1[y]:
				counter+=1
		dict[str1[x]]=counter
	#print(dict)
	li=sorted(dict.items(),key=lambda x:x[1],reverse=True)
	for x in range(5):
		print(li[x])
Check_max("novel2.txt")