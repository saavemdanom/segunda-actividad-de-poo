from enum import Enum


class TipoPlaneta(Enum):
    """Enumeración con los posibles tipos de planeta."""
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    """Clase que representa el concepto de un planeta del sistema solar."""
    
    # Constante para una Unidad Astronómica en kilómetros
    VALOR_UA_KM = 149597870

    def __init__(
        self,
        nombre: str = None,
        cantidad_satelites: int = 0,
        masa: float = 0.0,
        volumen: float = 0.0,
        diametro: int = 0,
        distancia_media_sol: int = 0,
        tipo_planeta: TipoPlaneta = None,
        es_observable: bool = False
    ):
        """Constructor que inicializa los atributos del planeta."""
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa  # en kg
        self.volumen = volumen  # en km^3
        self.diametro = diametro  # en km
        self.distancia_media_sol = distancia_media_sol  # en millones de km
        self.tipo_planeta = tipo_planeta
        self.es_observable = es_observable

    def calcular_densidad(self) -> float:
        """Calcula la densidad como el cociente entre masa y volumen."""
        if self.volumen <= 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        """
        Determina si es un planeta exterior.
        Un planeta es exterior si está más allá del cinturón de asteroides (> 3.4 UA).
        """
        distancia_km = self.distancia_media_sol * 1_000_000
        distancia_ua = distancia_km / self.VALOR_UA_KM
        return distancia_ua > 3.4

    def imprimir(self):
        """Imprime los valores de los atributos del planeta."""
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia media al Sol: {self.distancia_media_sol} millones de km")
        tipo_str = self.tipo_planeta.value if self.tipo_planeta else "No asignado"
        print(f"Tipo de planeta: {tipo_str}")
        print(f"Es observable a simple vista: {'Sí' if self.es_observable else 'No'}")


def main():
    """Función principal para probar la creación de objetos y métodos."""
    
    # Planeta 1: Tierra (Interior)
    tierra = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.9736e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_media_sol=150,
        tipo_planeta=TipoPlaneta.TERRESTRE,
        es_observable=True
    )

    # Planeta 2: Júpiter (Exterior)
    jupiter = Planeta(
        nombre="Júpiter",
        cantidad_satelites=95,
        masa=1.8986e27,
        volumen=1.43128e15,
        diametro=139820,
        distancia_media_sol=778,
        tipo_planeta=TipoPlaneta.GASEOSO,
        es_observable=True
    )

    # Mostrar Tierra
    print("=== INFORMACIÓN PLANETA 1 ===")
    tierra.imprimir()
    print(f"Densidad: {tierra.calcular_densidad():.4e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if tierra.es_planeta_exterior() else 'No'}\n")

    # Mostrar Júpiter
    print("=== INFORMACIÓN PLANETA 2 ===")
    jupiter.imprimir()
    print(f"Densidad: {jupiter.calcular_densidad():.4e} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if jupiter.es_planeta_exterior() else 'No'}\n")


if __name__ == "__main__":
    main()
