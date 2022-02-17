class Calculadora:
    def __init__(self,num1,num2): 
        self.operacionSuma = num1+num2
        self.operacionResta = num1-num2
        self.operacionMult = num1*num2
        self.operacionDiv = round(num1/num2,1)
while True:
    opcion = input('\nOperacion: ')
    if opcion == 'x':
        print('\n ** Gracias ** \n')
        break
    else: 
        num1 = float(input('Primer numero: '))
        num2 = float(input('Segundo numero: '))
        objResp = Calculadora(num1,num2)
        if opcion == '+':
            print(f'\nLa suma es: {objResp.operacionSuma}')
        elif opcion == '-':
            print(f'\nLa resta es: {objResp.operacionResta}')
        elif opcion == '*':
            print(f'\nLa multiplicacion es: {objResp.operacionMult}')
        elif opcion == '/':
            print(f'\nLa division es: {objResp.operacionDiv}')
        else:
            print('Operacion invalida')
