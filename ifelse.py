my_nums = 1122
if 9 < my_nums < 99:
    print("Two digit num")
elif 99 < my_nums < 999:
    print("Three digit num")
elif 999 < my_nums < 9999:
    print("Four digit num")
else:
    print("num is <= 9 or >= 9999")