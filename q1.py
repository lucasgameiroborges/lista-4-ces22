# Classes pai que será ponte: Motor


class Motor:
    def motor_tipo(self):
        pass

# Classes filhas do motor


class Eletrico(Motor):
    def motor_tipo(self):
        print("Eu carrego um motor do tipo elétrico")


class Hibrido(Motor):
    def motor_tipo(self):
        print("Eu carrego um motor do tipo híbrido")


class Combustao(Motor):
    def motor_tipo(self):
        print("Eu carrego um motor do tipo combustão")

# classe pai Veículo


class Veiculo:
    def __init__(self, Motor):  # ponte motor na definicao de veiculo
        self.motor = Motor

    def descricao(self):
        pass

# classes filhas de veiculo


class Caminhao(Veiculo):
    def __init__(self, Motor):
        super().__init__(Motor)

    def descricao(self):
        print("Olá! Eu sou um caminhão.")
        self.motor.motor_tipo()


class Carro(Veiculo):
    def __init__(self, Motor):
        super().__init__(Motor)

    def descricao(self):
        print("Olá! Eu sou um carro.")
        self.motor.motor_tipo()


class Moto(Veiculo):
    def __init__(self, Motor):
        super().__init__(Motor)

    def descricao(self):
        print("Olá! Eu sou uma moto.")
        self.motor.motor_tipo()


motor1 = Eletrico()
motor2 = Combustao()
motor3 = Hibrido()

# fazendo a ponte entre as classes de veiculo e as classes de motor
veiculo1 = Moto(motor1)
veiculo1.descricao()
veiculo2 = Caminhao(motor2)
veiculo2.descricao()
veiculo3 = Carro(motor3)
veiculo3.descricao()