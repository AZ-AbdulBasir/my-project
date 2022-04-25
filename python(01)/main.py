#1
password = input()
password2 = input()
while len(password) < 8:
    print("Короткий!")
    password = input()
    password2 = input()
while "123" in password:
    print("Простой!")
    password = input()
    password2 = input()
while password2 != password:
    print("Различаются.")
    password = input()
    password2 = input()
else:
    print("OK")


#2

f1 = open('data.txt')
f1.readline()
'one - 1 - I\n'
f1.readline()
'two - 2 - II\n'
f1.readline()
'three - 3 — III\n'

#3

handle = open("test.txt")
handle = open(r"C:\Users\mike\py101book\data\test.txt", "r")

#1

try:
    age_list = []

    user_input = int(input('Int: '))
    int_list.append(user_input)
    print(int_list)

except ValueError:
    print('Вы сможете вводить только int')

else:
    print('Программа работает верно!')

finally:
    print('Это финальная операция')


#2
try:
    age_list = []

    a = int(input("a:"))
    b = int(input("b:"))
    print(a/b)

except:
    print('Вы сможете вводить только числа')

else:
    print('Программа работает верно!')

finally:
    print('Это финальная операция')

