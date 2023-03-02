x={}
n=int(input(" Enter the number of candidates"))
for i in range(n):
	name=input("Enter the name")
	x[name]=input("Password")
print(x)
username= input("Enter a name")
if username in x:
	password=input("Enter a password")
	correctpassword=x[username]
	if password==correctpassword:
		print ("logged in")
	else:
		print("wrong password")
else:
	print("Wrong user")
