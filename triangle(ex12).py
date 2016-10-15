def CheckForTriangles(a,b,c):
	l=[]
	l.append(int(a))
	l.append(int(b))
	l.append(int(c))
	l.sort()
	if l[0]+l[1]>l[2] or l[1]+l[2]>l[0] or l[2]+l[0]>l[1]:
		if l[2]**2<l[0]**2+l[1]**2:
			print 1,"(Acute)"
		elif l[2]**2>l[0]**2+l[1]**2:
			print 2,"(Obtuse)"
		else:
			print 3,"(Right)"
	else:
		print -1,"(Not a triangle)"

flag="y"
while flag!="n":
	a=raw_input("Give value for the 1st side...\n")
	b=raw_input("Give value for the 2nd side...\n")
	c=raw_input("Give value for the 3rd side...\n")
	CheckForTriangles(a,b,c)
	flag=raw_input("Do you want to continue ??? (y/n)\n")
