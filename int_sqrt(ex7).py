def CheckIfInteger(num):
    if (num**(.5))%1 == 0:
        print "True (",num,"is equal to an integer to the second power)\n"
    else:
        print "False (",num,"is equal to a float to the second power)\n"

flag="y"
while flag!="n":
	num = input("Give a number...\n")
	CheckIfInteger(num)
	flag=raw_input("Do you want to continue ??? (y/n) ")
