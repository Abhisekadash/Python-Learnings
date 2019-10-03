import os
c=0
for x in os.listdir('F:\Asim\Such\Miku'):
	if os.path.isfile(x):
		for y in os.listdir('F:\Asim\Such\Miku\Chiku'):
			if os.path.isfile(y):
				if os.path.getsize(x)>os.path.getsize(y):
					#print(x,y)
					if os.path.getsize(c)<os.path.getsize(x):
						c=x
				else:
					if os.path.getsize(c)<os.path.getsize(y):
						c=y

if c in os.listdir('F:\Asim\Such\Miku'):
	os.remove(os.path.join('F:\Asim\Such\Miku',c))
else:
	os.remove(os.path.join('F:\Asim\Such\Miku\Chiku',c))