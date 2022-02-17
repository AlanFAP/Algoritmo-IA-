class Calculadora:
    def __init__(self,num1,num2): 
        self.operacionSuma = num1 + num2

objResp = Calculadora(2,4)
print(f'\nLa suma es: {objResp.operacionSuma}')
