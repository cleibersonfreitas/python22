class UsuarioMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['contador'] = 0
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.contador += 1


class UsuarioRepository(metaclass=UsuarioMeta):
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        """Cadastra um usuário (dicionário com nome e email)."""
        if self.buscar_por_email(usuario['email']):
            print(f"Usuário com email {usuario['email']} já cadastrado.")
            return
        self.usuarios.append(usuario)
        print(f"Usuário {usuario['nome']} cadastrado com sucesso.")

    def listar_todos(self):
        """Retorna uma lista com todos os usuários cadastrados."""
        return self.usuarios

    def buscar_por_email(self, email):
        """Retorna o usuário correspondente ao email informado."""
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return usuario
        return None

    def remover(self, email):
        """Remove o usuário correspondente ao email informado."""
        usuario = self.buscar_por_email(email)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuário {usuario['nome']} removido com sucesso.")
        else:
            print(f"Não foi possível remover, usuário com email {email} não encontrado.")

    def atualizar(self, usuario):
        """Atualiza os dados do usuário correspondente ao email informado."""
        for i, u in enumerate(self.usuarios):
            if u['email'] == usuario['email']:
                self.usuarios[i] = usuario
                print(f"Usuário {usuario['nome']} atualizado com sucesso.")
                return
        print(f"Usuário com email {usuario['email']} não encontrado.")

    def listar_por_nome(self, nome):
        """Retorna uma lista com todos os usuários que possuem o nome informado."""
        usuarios_encontrados = [usuario for usuario in self.usuarios if usuario['nome'] == nome]
        if not usuarios_encontrados:
            print(f"Nenhum usuário encontrado com o nome {nome}.")
        return usuarios_encontrados

    def listar_por_email(self, email):
        """Retorna uma lista com todos os usuários que possuem o email informado."""
        usuarios_encontrados = [usuario for usuario in self.usuarios if usuario['email'] == email]
        if not usuarios_encontrados:
            print(f"Nenhum usuário encontrado com o email {email}.")
        return usuarios_encontrados

    def listar_por_nome_e_email(self, nome, email):
        """Retorna uma lista com todos os usuários que possuem o nome e email informados."""
        usuarios_encontrados = [usuario for usuario in self.usuarios if usuario['nome'] == nome and usuario['email'] == email]
        if not usuarios_encontrados:
            print(f"Nenhum usuário encontrado com o nome {nome} e email {email}.")
        return usuarios_encontrados

    def exibir_usuarios(self):
        """Exibe todos os usuários de forma legível."""
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("Usuários cadastrados:")
        for usuario in self.usuarios:
            print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")


def main():
    repo = UsuarioRepository()
    comandos = {
        "1": "Cadastrar usuário",
        "2": "Listar todos os usuários",
        "3": "Buscar usuário por email",
        "4": "Remover usuário por email",
        "5": "Atualizar usuário",
        "6": "Listar usuários por nome",
        "7": "Listar usuários por email",
        "8": "Listar usuários por nome e email",
        "9": "Exibir contador de instâncias de UsuarioRepository",
        "0": "Sair"
    }

    while True:
        print("\nMenu:")
        for key in sorted(comandos.keys()):
            print(f"{key} - {comandos[key]}")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Encerrando o programa.")
            break

        elif escolha == "1":  # Cadastrar usuário
            nome = input("Nome do usuário: ").strip()
            email = input("Email do usuário: ").strip()
            repo.cadastrar({'nome': nome, 'email': email})

        elif escolha == "2":  # Listar todos os usuários
            repo.exibir_usuarios()

        elif escolha == "3":  # Buscar usuário por email
            email = input("Digite o email para buscar: ").strip()
            usuario = repo.buscar_por_email(email)
            if usuario:
                print(f"Usuário encontrado: Nome = {usuario['nome']}, Email = {usuario['email']}")
            else:
                print("Usuário não encontrado.")

        elif escolha == "4":  # Remover usuário por email
            email = input("Digite o email do usuário a remover: ").strip()
            repo.remover(email)

        elif escolha == "5":  # Atualizar usuário
            email = input("Digite o email do usuário que deseja atualizar: ").strip()
            usuario_existente = repo.buscar_por_email(email)
            if usuario_existente:
                novo_nome = input(f"Digite o novo nome (atual: {usuario_existente['nome']}): ").strip()
                novo_email = input(f"Digite o novo email (atual: {usuario_existente['email']}): ").strip()
                # Se usuário deixar em branco, mantemos o valor antigo
                if not novo_nome:
                    novo_nome = usuario_existente['nome']
                if not novo_email:
                    novo_email = usuario_existente['email']
                repo.atualizar({'nome': novo_nome, 'email': novo_email})
            else:
                print("Usuário não encontrado para atualizar.")

        elif escolha == "6":  # Listar usuários por nome
            nome = input("Digite o nome para buscar: ").strip()
            usuarios = repo.listar_por_nome(nome)
            if usuarios:
                for u in usuarios:
                    print(f"Nome: {u['nome']}, Email: {u['email']}")

        elif escolha == "7":  # Listar usuários por email
            email = input("Digite o email para buscar: ").strip()
            usuarios = repo.listar_por_email(email)
            if usuarios:
                for u in usuarios:
                    print(f"Nome: {u['nome']}, Email: {u['email']}")

        elif escolha == "8":  # Listar usuários por nome e email
            nome = input("Digite o nome para buscar: ").strip()
            email = input("Digite o email para buscar: ").strip()
            usuarios = repo.listar_por_nome_e_email(nome, email)
            if usuarios:
                for u in usuarios:
                    print(f"Nome: {u['nome']}, Email: {u['email']}")

        elif escolha == "9":  # Exibir contador de instâncias
            print(f"Número de instâncias de UsuarioRepository: {UsuarioRepository.contador}")

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

