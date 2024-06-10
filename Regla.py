class Regla:
    def init(self, izquierda, derecha):
        self.left = izquierda
        self.right = derecha
        self.cont = 1

    def repr(self):
        return f"{self.cont} {self.left} {' '.join(self.right)}"


regla = Regla('Historia', ('Frase', 'y', 'Historia'))
print(regla)
