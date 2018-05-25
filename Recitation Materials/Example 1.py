#Ask for a number between 50 and 200 and print all numbers between 1 and then input that are divisible by 3. Print the sum of all others.
x=int(input("Pick a number between 50 and 200: "))
y=0
for i in range(1,x+1):
	if i%3==0: 
		print(i)
	else:
		y=y+i
print(y)
