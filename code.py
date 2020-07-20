#basic print function 

print("hello world!!")

#basic identification

if 10 > 7 :
	print("ten is greater than seven")

#basic variables 

 x =  23
 y = "harsh"

 print (x)
 print (y)

my_var="harsh is improving"
print(my_var)

a , b , c="harsh","dhiraj","kushal"
print(a)
print(b)
print(c)

#basic adding two statement!

x = "bhaiya you "
y = "are amazing "
z= x + y

print(z)


#gobal varibles 

x = "bhaiya you "

def myfun():
	print("are amazing " + x )

	myfun()

#varible inside a function 

a = "amazing"

def myfunc():
  a = "fantastic"
  print("bhaiya you " + a)

myfunc()

print("bhaiya you " + a)