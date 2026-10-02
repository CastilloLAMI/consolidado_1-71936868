class Automovil:
    def __init__(self, marca: str, modelo: str, motor: float, tipo_combustible: str, tipo_auto: str, puertas: int, asientos: int, velocidad_maxima: float, color: str, velocidad_actual: float = 0.0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_auto = tipo_auto
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self._velocidad_actual = 0.0
        self.velocidad_actual = velocidad_actual

@property
    def velocidad_actual(self) -> float:
        return self._velocidad_actual

    @velocidad_actual.setter
    def velocidad_actual(self, valor: float):
        if valor < 0:
            self._velocidad_actual = 0.0
        elif valor > self.velocidad_maxima:
            self._velocidad_actual = self.velocidad_maxima
        else:
            self._velocidad_actual = valor

    def acelerar(self, incremento: float):
        self.velocidad_actual += incremento

    def desacelerar(self, decremento: float):
        self.velocidad_actual -= decremento

    def frenar(self):
        self._velocidad_actual = 0.0