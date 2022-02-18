from builtins import print


# print('mnhnmg')
# x = "salah"
# u = "20"
# print(f"{x} has {u} years")
# salary = int(input('please enter ur salary'))
#
# salary2 = int(input("please enter ur salary2"))
# print(salary + salary2 * 30 / 100)

# password = 1245646
# x = input(str(" fsddgs"))
# if password == x:
#     print("sccuess pass")
# else:
#     print("worng pass")
# age =30
# salray= "23320"
# if age >20:
#
#     print("gg")
# else:
#     print("gf")

# salry =int(input("enter ur salry"))
# age =int(input("enter ur age"))
# if age > 30:
#     print(salry*30/100)
# else:
#     print(salry)

# s1 =int(input("s1"))
# s2 =int(input("s1"))
# s3 =int(input("s1"))
# s4 =int(input("s1"))
# s5 =int(input("s1"))
#
# avg=(s1+s3+ s2+s5+s4)/5
# if avg>70:
#     print("ez")
# else:
#    print("gg")
# for i in range(22, 52,11):
#     print(i)
# def gga():
#     num1 = int(input("enter num1"))
#     num2 = int(input("enter num2"))
#     print(num1 + num2)
#
#
# gga()





print('Choose a number')
a = float(input())
print('Choose a second number')
b = float(input())
print('Do you want to * / - or + ?')
sign = input()


def calculate(a, b, sign):
    if sign == '+':
        print(a+b)
    elif sign == '-':
        print(a - b)
    elif sign == '*':
        print(a * b)
    elif sign == '/':
        print(a / b)
    else:
        print('not included')


answer = calculate(a, b, sign)
print(answer)

