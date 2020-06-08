# Classes pai que será ponte: Motor


class Motor:
    def __init__(self):
        self.tipo = "motor generico"

    def motor_tipo(self):
        pass

# Classes filhas do motor


class Eletrico(Motor):
    def __init__(self):
        self.tipo = "elétrico"

    def motor_tipo(self):
        print("Eu carrego um motor do tipo elétrico")


class Hibrido(Motor):
    def __init__(self):
        self.tipo = "híbrido"

    def motor_tipo(self):
        print("Eu carrego um motor do tipo híbrido")


class Combustao(Motor):
    def __init__(self):
        self.tipo = "combustão"

    def motor_tipo(self):
        print("Eu carrego um motor do tipo combustão")

# classe pai Veículo


class Veiculo:
    def __init__(self, Motor):  # ponte motor na definicao de veiculo
        self.motor = Motor
        self.tipo = "veiculo generico"
        self.descricao = "Olá! eu sou um " + self.tipo + " com motor tipo " + self.motor.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo
        self.descricao = "Olá! eu sou um " + self.tipo + " com motor tipo " + self.motor.tipo

    def get_tipo(self):
        print(self.tipo)

    def get_descricao(self):
        print(self.descricao)


# aplicacao do metodo de fabrica


class InstanciarVeiculo:
    def instancia(self, Veiculo, tipo):
        instanciador = get_instanciador(tipo)
        return instanciador(Veiculo)


def get_instanciador(tipo):
    if (tipo == "moto") | (tipo == "motocicleta"):
        return _instancia_moto
    elif (tipo == "carro") | (tipo == "automovel"):
        return _instancia_carro
    elif (tipo == "caminhao") | (tipo == "caminhonete"):
        return _instancia_caminhao
    else:
        raise ValueError(tipo)


def _instancia_moto(Veiculo):
    Veiculo.set_tipo("moto")


def _instancia_carro(Veiculo):
    Veiculo.set_tipo("carro")


def _instancia_caminhao(Veiculo):
    Veiculo.set_tipo("caminhao")


motor1 = Eletrico()
motor2 = Combustao()
motor3 = Hibrido()

# fazendo a ponte entre as classes de veiculo e as classes de motor
veiculo1 = Veiculo(motor1)
veiculo2 = Veiculo(motor2)
veiculo3 = Veiculo(motor3)
instanciador = InstanciarVeiculo()
instanciador.instancia(veiculo1, "moto")
instanciador.instancia(veiculo2, "carro")
instanciador.instancia(veiculo3, "caminhao")
veiculo1.get_descricao()
veiculo2.get_descricao()
veiculo3.get_descricao()

