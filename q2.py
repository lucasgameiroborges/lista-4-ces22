# Classe base: Pizza


class Pizza:
    def massa_tipo(self):
        pass

    def sabor(self):
        pass

    def custo(self):
        pass

# Classes Tipos de massas


class MassaFina(Pizza):
    def massa_tipo(self):
        print("Eu sou uma pizza de massa fina")

    def custo(self):
        return 10


class MassaGrossa(Pizza):
    def massa_tipo(self):
        print("Eu sou uma pizza de massa grossa")

    def custo(self):
        return 15

# Classe abstrata decorator


class PizzaDecorator(Pizza):
    def __init__(self, Pizza):  # ponte motor na definicao de veiculo
        self.pizza = Pizza

# Tipos de decoradores


class Muzzarella(PizzaDecorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)

    def massa_tipo(self):
        self.pizza.massa_tipo()

    def sabor(self):
        print("Sabor Muzzarella")

    def custo(self):
        return self.pizza.custo() + 5


class Calabresa(PizzaDecorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)

    def massa_tipo(self):
        self.pizza.massa_tipo()

    def sabor(self):
        print("Sabor Calabresa")

    def custo(self):
        return self.pizza.custo() + 7


class QuatroQueijos(PizzaDecorator):
    def __init__(self, Pizza):
        super().__init__(Pizza)

    def massa_tipo(self):
        self.pizza.massa_tipo()

    def sabor(self):
        print("Sabor Quatro Queijos")

    def custo(self):
        return self.pizza.custo() + 10


# teste de implementacao
massa1 = MassaFina()
massa2 = MassaGrossa()
pizza1 = Muzzarella(massa2)
pizza1.massa_tipo()
pizza1.sabor()
print("Eu custo ", pizza1.custo(), "reais \n")
pizza1 = Muzzarella(massa1)
pizza1.massa_tipo()
pizza1.sabor()
print("Eu custo ", pizza1.custo(), "reais \n")
pizza1 = Calabresa(massa2)
pizza1.massa_tipo()
pizza1.sabor()
print("Eu custo ", pizza1.custo(), "reais \n")
pizza1 = QuatroQueijos(massa1)
pizza1.massa_tipo()
pizza1.sabor()
print("Eu custo ", pizza1.custo(), "reais")
