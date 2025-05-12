from abc import ABC, ABCMeta, abstractmethod

# Metaclasse
class AnimalMeta(ABCMeta):
    def __new__(cls, name, bases, dct):
        if name != "Animal":
            required_methods = ['apresentar', 'acao1', 'acao2', 'acao3']
            for method in required_methods:
                if method not in dct:
                    raise TypeError(f"Classe {name} deve implementar o método {method}.")
        return super().__new__(cls, name, bases, dct)

# Classe abstrata Animal
class Animal(ABC, metaclass=AnimalMeta):
    @abstractmethod
    def apresentar(self):
        pass

    @abstractmethod
    def acao1(self):
        pass

    @abstractmethod
    def acao2(self):
        pass

    @abstractmethod
    def acao3(self):
        pass

# Classe Cachorro
class Cachorro(Animal):
    def apresentar(self):
        print("\n🐶 Eu sou um cachorro! Sou leal e adoro brincar.")

    def acao1(self):
        print("🐶 O cachorro está latindo alto!")

    def acao2(self):
        print("🐶 O cachorro está correndo atrás da bola!")

    def acao3(self):
        print("🐶 O cachorro está cavando o quintal!")

# Submenu interativo
def submenu(animal):
    animal.apresentar()
    while True:
        print("\nEscolha uma ação:")
        print("1 - Ação 1")
        print("2 - Ação 2")
        print("3 - Ação 3")
        print("0 - Voltar ao menu principal")

        opcao = input("Digite sua opção: ")
        if opcao == '1':
            animal.acao1()
        elif opcao == '2':
            animal.acao2()
        elif opcao == '3':
            animal.acao3()
        elif opcao == '0':
            break
        else:
            print("❌ Opção inválida, tente novamente.")

# Menu principal
def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cachorro")
        print("0 - Sair")
        opcao = input("Digite sua opção: ")

        if opcao == '1':
            cachorro = Cachorro()
            submenu(cachorro)
        elif opcao == '0':
            print("👍 Programa encerrado. Até a próxima!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

# Execução
if __name__ == "__main__":
    main()
