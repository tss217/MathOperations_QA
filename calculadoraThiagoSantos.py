
#thiago santos da silva - Ra:320193

class Calculadora:
    def __init__(self,operadorUm,operadorDois):
        self._operadorUm = operadorUm
        self._operadorDois = operadorDois
        self._soma = self.soma
        self._subtracao = self.subtracao
        self._multiplicacao = self.multiplicacao
        self._divisao = self.divisao 
        self._resto = self.resto
        
    @property
    def a(self):
        try:
            return int(self._operadorUm)
        except:
            return float(self._operadorUm)

    @property
    def b(self):
        try:
            return int(self._operadorDois)
        except:
            return float(self._operadorDois)

    @property
    def soma(self):
        operaçãoDeSoma = (self.a) + (self.b)
        return operaçãoDeSoma

    def resultadoSoma(self):
        return self.soma

    @property
    def subtracao(self):
        operaçãoDeSubtração = (self.a) - (self.b)
        return operaçãoDeSubtração

    def resultadoSubtração(self):
        return self.subtracao

    @property
    def multiplicacao(self):
        operaçãoDeMultiplicação = (self.a) * (self.b)
        return operaçãoDeMultiplicação

    def resultadoMultiplicacao(self):
        return  self.multiplicacao

    @property
    def divisao(self):
        try:
            operaçãoDeDivisão = (self.a) / (self.b)
        except:
            operaçãoDeDivisão = False
        return operaçãoDeDivisão

    @property
    def resto(self):
        if self.b == 0:
            operaçãoResto=print(self.b)
        else:
            operaçãoResto = (self.a) % (self.b)
        return operaçãoResto

    def resultadoDivisao(self):
        return self.divisao
    
    def resultadoResto(self):
        return self.resto

class tester(Calculadora):
    def __init__(self, operadorUm, operadorDois):
        super().__init__(operadorUm, operadorDois)
        self._ok = self.ok
        self._erro = self.erro
    
    def erro(self):
        erro = "erro"
        return erro

    def ok(self):
        ok = "ok"
        return ok

    def somaTest(self):
        plus = (self.a)+(self.b)

        if plus == self.resultadoSoma():
            return self.ok()
        else:
            return self.erro()
        
    def subTest(self):
        minus = (self.a)-(self.b)

        if minus == self.resultadoSubtração():
            return self.ok()
        else:
            return self.erro()
        
    def multTest(self):
        mult = (self.a)*(self.b)

        if mult == self.resultadoMultiplicacao():
            return self.ok()
        else:
            return self.erro()
        
    def divTest(self):

        try:
            div = (self.a)/(self.b)
            
            if div == self.resultadoDivisao():
                return self.ok()
            else:
                return self.erro()
        except: 
            if self.resultadoDivisao() == False:
                non = "non"
                return non