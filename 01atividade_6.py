from datetime import datetime

class Conta:
    """
    Classe base que representa uma conta bancária com controle de saldo e histórico.
    """
    def __init__(self, saldo_inicial=0.0, titular=""):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self._saldo = float(saldo_inicial)
        self.historico = []
        self.titular = titular
        self._registrar_transacao("Abertura de conta", saldo_inicial)

    @property
    def saldo(self):
        return f'R${self._saldo:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = float(valor)

    def _registrar_transacao(self, tipo, valor, detalhes=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historico.append({"data": timestamp, "tipo": tipo, "valor": f'{valor:.2f}', "detalhes": detalhes})

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor
        self._registrar_transacao("Depósito", valor)

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor
        self._registrar_transacao("Saque", -valor)

    def transferir(self, outra_conta, valor):
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para transferência.")
        self._saldo -= valor
        outra_conta._saldo += valor
        self._registrar_transacao(f"Transferência para {outra_conta.titular}", -valor)
        outra_conta._registrar_transacao(f"Transferência de {self.titular}", valor)
        print("Transferência realizada com sucesso!")

    def exibir_historico(self):
        print("\n=== HISTÓRICO DE TRANSAÇÕES ===")
        if not self.historico:
            print("Nenhuma transação realizada.")
            return
        for transacao in self.historico:
            detalhes = f" ({transacao['detalhes']})" if transacao['detalhes'] else ""
            print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']}{detalhes}")


class ContaCorrente(Conta):
    """
    Subclasse de Conta que representa uma conta corrente com limite de cheque especial.
    """
    def __init__(self, saldo_inicial=0.0, titular="", limite_cheque_especial=0.0):
        super().__init__(saldo_inicial, titular)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo + self.limite_cheque_especial:
            raise ValueError("Saldo insuficiente (incluindo cheque especial).")
        self._saldo -= valor
        self._registrar_transacao("Saque", -valor, "Cheque Especial utilizado" if self._saldo < 0 else None)


class ContaPoupanca(Conta):
    """
    Subclasse de Conta que representa uma conta poupança com rendimento mensal.
    """
    def __init__(self, saldo_inicial=0.0, titular="", taxa_rendimento=0.01):
        super().__init__(saldo_inicial, titular)
        self.taxa_rendimento = taxa_rendimento

    def aplicar_rendimento(self):
        rendimento = self._saldo * self.taxa_rendimento
        self._saldo += rendimento
        self._registrar_transacao("Rendimento", rendimento)
        print("Rendimento aplicado!")


def menu(conta):
    print(f"\n=== MENU CONTA BANCÁRIA ({conta.titular}) ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Transferir")
    print("5 - Ver histórico de transações")
    print("6 - Aplicar rendimento (Poupança)")
    print("7 - Sair")


if __name__ == "__main__":
    conta1 = ContaCorrente(1000.0, "João", 500.0)
    conta2 = ContaPoupanca(500.0, "Maria", 0.015)
    conta_ativa = conta1  # Começamos com a conta do João

    while True:
        menu(conta_ativa)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Saldo atual:", conta_ativa.saldo)

        elif opcao == '2':
            try:
                valor = float(input("Valor do depósito: ").replace(',', '.'))
                conta_ativa.depositar(valor)
                print("Depósito realizado com sucesso!")
            except ValueError as e:
                print("Erro:", e)

        elif opcao == '3':
            try:
                valor = float(input("Valor do saque: ").replace(',', '.'))
                conta_ativa.sacar(valor)
                print("Saque realizado com sucesso!")
            except ValueError as e:
                print("Erro:", e)

        elif opcao == '4':
            valor_transferencia = float(input("Valor da transferência: ").replace(',', '.'))
            if conta_ativa == conta1:
                conta_ativa.transferir(conta2, valor_transferencia)
            else:
                conta_ativa.transferir(conta1, valor_transferencia)

        elif opcao == '5':
            conta_ativa.exibir_historico()

        elif opcao == '6' and isinstance(conta_ativa, ContaPoupanca):
            conta_ativa.aplicar_rendimento()
        elif opcao == '6' and not isinstance(conta_ativa, ContaPoupanca):
            print("Esta opção é válida apenas para contas poupança.")

        elif opcao == '7':
            print("Saindo... Obrigado por usar nosso sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")
