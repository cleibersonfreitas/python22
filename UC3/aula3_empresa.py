class Colaborador:
    def __init__(self, id_colaborador, nome, cargo, salario):
        self.id_colaborador = id_colaborador
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id_colaborador} - Nome: {self.nome} - Cargo: {self.cargo} - Salário: R${self.salario:.2f}"

class Empresa:
    def __init__(self):
        self.colaboradores = {}

    def adicionar_colaborador(self, id_colaborador, nome, cargo, salario):
        if id_colaborador in self.colaboradores:
            print(f"Erro: Já existe um colaborador com o ID {id_colaborador}.")
        else:
            colaborador = Colaborador(id_colaborador, nome, cargo, salario)
            self.colaboradores[id_colaborador] = colaborador
            print(f"Colaborador {nome} adicionado com sucesso!")

    def buscar_colaborador_por_id(self, id_colaborador):
        colaborador = self.colaboradores.get(id_colaborador)
        if colaborador:
            print(colaborador)
        else:
            print(f"Colaborador com ID {id_colaborador} não encontrado.")

    def listar_colaboradores_acima_salario(self, salario_limite):
        colaboradores_filtrados = [colaborador for colaborador in self.colaboradores.values() if colaborador.salario > salario_limite]
        if colaboradores_filtrados:
            print("\nColaboradores com salário acima de R$", salario_limite)
            for colaborador in colaboradores_filtrados:
                print(colaborador)
        else:
            print(f"Nenhum colaborador encontrado com salário superior a R${salario_limite:.2f}.")

def menu():
    empresa = Empresa()

    # Adicionando alguns colaboradores já ao iniciar
    empresa.adicionar_colaborador(1, "Carlos Silva", "Gerente", 5000)
    empresa.adicionar_colaborador(2, "Fernanda Oliveira", "Analista", 3500)
    empresa.adicionar_colaborador(3, "João Pereira", "Assistente", 2500)
    empresa.adicionar_colaborador(4, "Maria Souza", "Coordenadora", 4500)
    empresa.adicionar_colaborador(5, "Lucas Martins", "Desenvolvedor", 6000)

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Colaborador")
        print("2. Buscar Colaborador por ID")
        print("3. Listar Colaboradores com salário acima de X")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            id_colaborador = int(input("Digite o ID do colaborador: "))
            nome = input("Digite o nome do colaborador: ")
            cargo = input("Digite o cargo do colaborador: ")
            salario = float(input("Digite o salário do colaborador: R$ "))
            empresa.adicionar_colaborador(id_colaborador, nome, cargo, salario)

        elif opcao == "2":
            id_colaborador = int(input("Digite o ID do colaborador a ser buscado: "))
            empresa.buscar_colaborador_por_id(id_colaborador)

        elif opcao == "3":
            salario_limite = float(input("Digite o salário limite: R$ "))
            empresa.listar_colaboradores_acima_salario(salario_limite)

        elif opcao == "4":
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
