nome1 = int(input('Enter a number: '))
nome2 = int(input('Enter a number: '))
operation =int(input ('1.sum, 2.sub, 3.mul,4.div, 5.modulo, 6.flot div, 7.power, 8.grater '))
if operation == 1:
    print(nome1 + nome2)
elif operation == 2:
    print(nome1 - nome2)
elif operation == 3:
    print(nome1 * nome2)
elif operation == 4:
    print(nome1 / nome2)
elif operation == 5:
    print(nome1 % nome2)
elif operation == 6:
    print(nome1 // nome2)
elif operation == 7:
    print(nome1 ** nome2)
elif operation == 8:
    print(nome1 >= nome2)
    