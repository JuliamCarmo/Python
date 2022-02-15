nome = input('Qual o nome do funcionário? ')
salario = float(input('Qual é o salario de {}? R$ '.format(nome)))
novo = salario + (salario * 15/ 100)
print('O salário atual de {} é de R${:.2f}. Com o aumento de 15% o salário será de R${:.2f}'.format(nome, salario, novo))