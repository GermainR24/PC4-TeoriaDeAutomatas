class Aleatorio:
    def __init__(self, semilla):
        self.valor = semilla
        self.m = 2**31 - 1  # 2147483647
        self.a = 16807  # 7^5

    def siguiente(self):
        self.valor = (self.a * self.valor) % self.m
        return self.valor

    def elegir(self, limite):
        return self.siguiente() % limite