n,q=[int(i) for i in input().split()]
l=list(map(int,input().split()))
for i in range(q):
	s,b=[int(i) for i in input().split()]
	d=0
	for i in range(s-1,b):
			d=min(l[s-1:b])
	print(d)	
