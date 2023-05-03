from tqdm import tqdm
from calculadoraThiagoSantos import Calculadora as ts
from calculadoraThiagoSantos import tester
from op import op
from op import hostName
import time
import random

#abertura 
op()
time.sleep(1)

def mathOperations(typeOperation,a,b):

    numbers = ts(a,b)
    numbersTest= tester(a,b)

    if typeOperation == "soma":
        numbers.soma
        print(numbers.resultadoSoma())
        resultado = tqdm.write(f'{a}+{b}={numbers.resultadoSoma()}.....{numbersTest.somaTest()}') 
        time.sleep(0.5)
    elif typeOperation == "sub":
        numbers.subtracao
        resultado = tqdm.write(f'{a}-{b}={numbers.resultadoSubtração()}.....{numbersTest.subTest()}') 
        time.sleep(0.5)
    elif typeOperation == "div":
        numbers.divisao
        resultado = tqdm.write(f'{a}/{b}={numbers.resultadoDivisao()}, resto:{numbers.resultadoResto()}..{numbersTest.divTest()}') 
        time.sleep(0.5)
    elif typeOperation == "mult":
        numbers.multiplicacao
        resultado = tqdm.write(f'{a}*{b}={numbers.resultadoMultiplicacao()}......{numbersTest.multTest()}')
        time.sleep(0.5)
    return resultado   

while True:
    print("escolha uma opção " + hostName())
    time.sleep(1)
    print()
    print("entrada geradas aleatoriamente(1)")
    print("entradas geradas manualmente(2)")
    
    choice = input("qual a sua escolha: ")

    if choice == "1":
        print("opção 1 selcionada")
        print()
        qtd = input("qtd de teste:")
        numOne = input("")
        numTwo = input("")

        for i in tqdm(range(int(qtd))):
            try:
                randomNumOne = random.randint(int(numOne),int(numTwo))
                randomNumTwo = random.randint(int(numOne),int(numTwo))
            except:
                randomNumOne = random.uniform(float(numOne),float(numTwo)) 
                randomNumTwo = random.uniform(float(numOne),float(numTwo))

            mathOperations("soma",randomNumOne,randomNumTwo)
            mathOperations("sub",randomNumOne,randomNumTwo)
            mathOperations("div",randomNumOne,randomNumTwo)
            mathOperations("mult",randomNumOne,randomNumTwo)
            tqdm.write("")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

    elif choice == "2":
        print("opção 2 selcionada")
        print()
        qtd = 1

        numOne = input("primeira entrada: ")
        numTwo = input("segunda entrada: ")

        for i in tqdm(range(qtd)):
            mathOperations("soma",numOne,numTwo)
            mathOperations("sub",numOne,numTwo)
            mathOperations("div",numOne,numTwo)
            mathOperations("mult",numOne,numTwo)
            