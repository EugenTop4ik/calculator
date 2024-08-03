result=0
print('Введите первое число')
firstnum=int(input())
print('Введите второе число')
secondnum=int(input())
print('Введите знак арифметической операции (+, -, *, /)')
sign=str(input())
if sign == "+":
    result=firstnum+secondnum
elif sign == "-":
    result=firstnum-secondnum
elif sign == "*":
    result=firstnum*secondnum
elif sign == "/":
    result=firstnum/secondnum
else:
    print ('Ошибка выполнения. Пожалуйста проверьте введённые данные')
print (result)
print ('Для завершения работы программы нажмине клавишу Enter')
pause=str(input())
