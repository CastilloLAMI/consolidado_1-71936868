class Planeta:
    def __init__(self, nombre: str, satelites: int, masa: float, volumen: float, diametro: float, distancia_sol: float, tipo: str, es_observable: bool):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo.upper()
        self.es_observable = es_observable

    def calcular_densidad(self) -> float:
        if self.volumen <= 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        # Distancia media en millones de km (3.3 UA ≈ 493.5 mill. km)
        return self.distancia_sol > 493.5

    def __str__(self) -> str:
        return (f"Planeta: {self.nombre}\n"
                f"Satelites: {self.satelites}\n"
                f"Masa: {self.masa} kg\n"
                f"Volumen: {self.volumen} km3\n"
                f"Densidad: {self.calcular_densidad():.4f} kg/km3\n"
                f"Tipo: {self.tipo}\n"
                f"Exterior: {self.es_planeta_exterior()}\n"
                f"Observable a simple vista: {self.es_observable}")


if __name__ == "__main__":
    p1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 149.6, "TERRESTRE", True)
    p2 = Planeta("Júpiter", 79, 1.899e27, 1.43128e15, 139822, 778.5, "GASEOSO", True)

    print(p1)
    print("\n" + "="*30 + "\n")
    print(p2)

    