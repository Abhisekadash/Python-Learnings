import os
import argparse
import request
#print(os.getcwd())
#os.makedirs('F:\Asim\Suchi\Miku\Chiku')
parser=argparse.ArgumentParser()
parser.add_argument('dirc')
args=parser.parse_args()
print("Args",args.dirc)
print(type(args.dirc))
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
delete(args.dirc)
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
print("n= "+n)
def finder(file_name):
	if n in os.listdir(file_name):
		os.remove(os.path.join(file_name,n))
	else:
		for x in os.listdir(file_name):
		    if os.path.isdir(os.path.join(file_name,x)):
		    	print(x)
		    	finder(os.path.join(file_name,x))
finder(args.dirc)



