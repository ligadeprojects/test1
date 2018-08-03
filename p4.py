# from functools import reduce
file='/Users/ppligade/itech/test.txt'
f=open(file,'r')

s=[line.strip() for line in f]

# s=f.read().splitlines()

def maxx(x,y):
	if(x>y):
		return x

s2=s.split(" ")
s3=map(lambda x: (x,len(x)),s2)
s4=reduce((lambda x,y: maxx(x,y)),s3)

print(s4[0])
