from enum import Enum


class TipoCuenta(Enum):
    """Enumeración para los tipos de cuenta bancaria."""
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


class CuentaBancaria:
    """Clase que representa una cuenta bancaria y sus operaciones principales."""

    def __init__(self, nombres: str, apellidos: str, numero_cuenta: str, tipo_cuenta: TipoCuenta):
        """
        Constructor que inicializa los datos de la cuenta.
        El saldo inicial se establece siempre en cero.
        """
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        """Imprime por pantalla los valores de los atributos de la cuenta."""
        print("=== DATOS DE LA CUENTA BANCARIA ===")
        print(f"Nombres del titular: {self.nombres}")
        print(f"Apellidos del titular: {self.apellidos}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.value}")
        print(f"Saldo actual: ${self.saldo:,.2f}")
        print("-" * 35)

    def consultar_saldo(self) -> float:
        """Muestra y devuelve el saldo actual de la cuenta bancaria."""
        print(f"Saldo actual en cuenta {self.numero_cuenta}: ${self.saldo:,.2f}")
        return self.saldo

    def consignar(self, valor: float) -> bool:
        """
        Consigna un valor en la cuenta bancaria actualizando el saldo.
        Verifica que el monto sea un valor positivo.
        """
        if valor <= 0:
            print("Error: El valor a consignar debe ser mayor a cero.")
            return False

        self.saldo += valor
        print(f"Consignación exitosa de ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
        return True

    def retirar(self, valor: float) -> bool:
        """
        Retira un valor de la cuenta bancaria actualizando el saldo.
        Verifica que el retiro no supere el saldo disponible.
        """
        if valor <= 0:
            print("Error: El valor a retirar debe ser mayor a cero.")
            return False

        if valor > self.saldo:
            print(f"Error: Saldo insuficiente. Intenta retirar ${valor:,.2f} pero solo dispone de ${self.saldo:,.2f}.")
            return False

        self.saldo -= valor
        print(f"Retiro exitoso de ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
        return True


def main():
    """Prueba del funcionamiento de la clase CuentaBancaria."""

    # 1. Creación de una cuenta con saldo inicial $0.0
    cuenta = CuentaBancaria(
        nombres="Carlos",
        apellidos="Restrepo",
        numero_cuenta="100-200-300",
        tipo_cuenta=TipoCuenta.AHORROS
    )

    # 2. Imprimir datos iniciales
    cuenta.imprimir()

    # 3. Consignar dinero
    print("Consignando $150,000...")
    cuenta.consignar(150000.0)

    # 4. Consultar el saldo
    cuenta.consultar_saldo()

    # 5. Retirar un monto válido
    print("\nRetirando $50,000...")
    cuenta.retirar(50000.0)

    # 6. Intentar retirar más dinero del saldo disponible
    print("\nIntentando retirar $200,000...")
    cuenta.retirar(200000.0)

    # 7. Consultar saldo final
    print("\nEstado final:")
    cuenta.consultar_saldo()


if __name__ == "__main__":
    main()
