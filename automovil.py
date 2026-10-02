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

def calcular_tiempo_llegada(self, distancia: float) -> float:
        if self._velocidad_actual <= 0:
            return float('inf')
        return distancia / self._velocidad_actual

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} ({self.color}) - Vel. Actual: {self.velocidad_actual} km/h"


if __name__ == "__main__":
    auto = Automovil("Toyota", "Corolla", 2.0, "Gasolina", "Sedán", 4, 5, 200, "Rojo")
    auto.acelerar(100)
    print(auto)
    print(f"Tiempo estimado para 200 km: {auto.calcular_tiempo_llegada(200):.2f} horas")