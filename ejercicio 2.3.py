from enum import Enum


class TipoCombustible(Enum):
    """Enumeración para los tipos de combustible."""
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"


class TipoAutomovil(Enum):
    """Enumeración para los tipos de automóvil."""
    CARRO_DE_CIUDAD = "Carro de Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    """Enumeración para los colores disponibles."""
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"


class Automovil:
    """Clase que representa un automóvil y sus operaciones de conducción."""

    def __init__(
        self,
        marca: str,
        modelo: int,
        motor: float,
        tipo_combustible: TipoCombustible,
        tipo_automovil: TipoAutomovil,
        numero_puertas: int,
        cantidad_asientos: int,
        velocidad_maxima: float,
        color: Color,
        velocidad_actual: float = 0.0
    ):
        """Constructor de la clase Automóvil."""
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = velocidad_actual

    # --- Métodos Getters y Setters ---
    def get_marca(self) -> str:
        return self._marca

    def set_marca(self, marca: str):
        self._marca = marca

    def get_modelo(self) -> int:
        return self._modelo

    def set_modelo(self, modelo: int):
        self._modelo = modelo

    def get_motor(self) -> float:
        return self._motor

    def set_motor(self, motor: float):
        self._motor = motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self._tipo_combustible

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible):
        self._tipo_combustible = tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self._tipo_automovil

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil):
        self._tipo_automovil = tipo_automovil

    def get_numero_puertas(self) -> int:
        return self._numero_puertas

    def set_numero_puertas(self, numero_puertas: int):
        self._numero_puertas = numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self._cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos: int):
        self._cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self) -> float:
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima: float):
        self._velocidad_maxima = velocidad_maxima

    def get_color(self) -> Color:
        return self._color

    def set_color(self, color: Color):
        self._color = color

    def get_velocidad_actual(self) -> float:
        return self._velocidad_actual

    def set_velocidad_actual(self, velocidad_actual: float):
        if velocidad_actual < 0:
            print("Error: La velocidad no puede ser negativa.")
            self._velocidad_actual = 0.0
        elif velocidad_actual > self._velocidad_maxima:
            print(f"Advertencia: No puede superar la velocidad máxima ({self._velocidad_maxima} km/h).")
            self._velocidad_actual = self._velocidad_maxima
        else:
            self._velocidad_actual = velocidad_actual

    # --- Métodos de Comportamiento ---
    def acelerar(self, incremento: float):
        """Aumenta la velocidad del automóvil sin superar la velocidad máxima."""
        if self._velocidad_actual + incremento > self._velocidad_maxima:
            print(f"Advertencia: No es posible acelerar a {self._velocidad_actual + incremento} km/h. Excede la velocidad máxima ({self._velocidad_maxima} km/h).")
            self._velocidad_actual = self._velocidad_maxima
        else:
            self._velocidad_actual += incremento

    def desacelerar(self, decremento: float):
        """Reduce la velocidad del automóvil sin permitir valores negativos."""
        if self._velocidad_actual - decremento < 0:
            print("Advertencia: No es posible desacelerar a una velocidad negativa. Se fija en 0 km/h.")
            self._velocidad_actual = 0.0
        else:
            self._velocidad_actual -= decremento

    def frenar(self):
        """Coloca la velocidad actual en cero."""
        self._velocidad_actual = 0.0

    def calcular_tiempo_llegada(self, distancia_km: float) -> float:
        """Calcula el tiempo estimado de llegada en horas dado un recorrido en kilómetros."""
        if self._velocidad_actual == 0:
            print("El automóvil está detenido. No se puede calcular el tiempo de llegada.")
            return 0.0
        return distancia_km / self._velocidad_actual

    def imprimir(self):
        """Muestra en pantalla todos los valores de los atributos del automóvil."""
        print("=== DATOS DEL AUTOMÓVIL ===")
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Motor: {self._motor} L")
        print(f"Tipo de Combustible: {self._tipo_combustible.value}")
        print(f"Tipo de Automóvil: {self._tipo_automovil.value}")
        print(f"Número de Puertas: {self._numero_puertas}")
        print(f"Cantidad de Asientos: {self._cantidad_asientos}")
        print(f"Velocidad Máxima: {self._velocidad_maxima} km/h")
        print(f"Color: {self._color.value}")
        print(f"Velocidad Actual: {self._velocidad_actual} km/h")
        print("-" * 35)


def main():
    """Prueba del ciclo de vida del objeto Automóvil según los requerimientos."""
    
    # 1. Crear un automóvil
    auto = Automovil(
        marca="Toyota",
        modelo=2023,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.COMPACTO,
        numero_puertas=5,
        cantidad_asientos=5,
        velocidad_maxima=180.0,
        color=Color.ROJO
    )

    auto.imprimir()

    # 2. Colocar su velocidad actual en 100 km/h
    print("Estableciendo velocidad actual en 100 km/h...")
    auto.set_velocidad_actual(100.0)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h\n")

    # 3. Aumentar su velocidad en 20 km/h
    print("Acelerando +20 km/h...")
    auto.acelerar(20.0)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h\n")

    # 4. Decrementar su velocidad en 50 km/h
    print("Desacelerando -50 km/h...")
    auto.desacelerar(50.0)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h\n")

    # Práctica adicional: Calcular tiempo para recorrer 140 km a la velocidad actual (70 km/h)
    distancia = 140.0
    tiempo = auto.calcular_tiempo_llegada(distancia)
    print(f"Tiempo estimado para recorrer {distancia} km a {auto.get_velocidad_actual()} km/h: {tiempo:.2f} horas\n")

    # 5. Frenar
    print("Frenando el vehículo...")
    auto.frenar()
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")


if __name__ == "__main__":
    main()
