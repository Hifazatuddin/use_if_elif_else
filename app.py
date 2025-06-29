# ab if else ka use krty hvy age checker programe krna ha jismy child adult aur senior citizen ka check krna ha
age = int(input("Enter Your age:"))
if age < 18 and age >= 0:
    print("You are a chaild")
elif age >= 18 and age < 19:
    print("You are a teenager")
elif age >= 18 and age < 60:
    print("You are an adult")
elif age >= 60:
    print("You are a senior citizen")
else:
    print("Invalid age entered")


# result Checker assigment

result = int(input("Enter Your Marks ?"))
if result == 95:
    print("You have got A+ Grade")
elif result >=  90:
    print("You have got A Grade")
elif result >=  80:
    print("You have got B Grade")
elif result >=  70:
    print("You have got C Grade")
elif result >=  60:
    print("You have got D Grade")
elif result >=  50:
    print("You have got E Grade")
else:
    print("Invalid , try again, you can do better next time")



# for i in range(1,20,2):
#     print(" "*(20-i),"*"*i)
