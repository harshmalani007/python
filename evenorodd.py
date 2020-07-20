my_num = int(input("Enter any numbers: "))
new = my_num%2
if new == 0:
    print(my_num, "is an even number")
elif new == 1:
    print(my_num, "is an odd number")
else:
    print("Error, Invalid input")