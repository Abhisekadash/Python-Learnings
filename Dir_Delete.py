import os
#print(os.getcwd())
#os.makedirs('F:\Asim\Suchi\Miku\Chiku')
c={}
def delete(m):
	for x in os.listdir(m):
		if os.path.isfile(os.path.join(m,x)):
			c[x]=os.path.getsize(os.path.join(m,x))
	for x in os.listdir(m):
		#print(x)
		if os.path.isdir(os.path.join(m,x)):
			#print(x)
			m=os.path.join(m,x)
			delete(m)
delete('F:\Asim\Suchi\Miku')
#print(c)
m=0
for x,y in c.items():
	for j,k in c.items():
		if y<k:
			if m<k:
				m=k
		else:
			if m<y:
				m=y				
#print(m)
n=''
for x,y in c.items():
	if m==y:
		n=n+x
print(n)
def finder(m):
	if n in os.listdir(m):
		os.remove(os.path.join(m,n))
	else:
		for x in os.listdir(m):
		    if os.path.isdir(os.path.join(m,x)):
		    	print(x)
		    	finder(os.path.join(m,x))
finder('F:\Asim\Suchi\Miku')


