from collections import defaultdict

def remover_duplicatas_por_nome(itens):
    """
    Remove duplicatas com base apenas no nome do item, preservando a ordem
    """
    nomes_vistos = set()
    unicos = []
    for nome, preco, categoria in itens:
        if nome.lower() not in nomes_vistos:
            unicos.append((nome, preco, categoria))
            nomes_vistos.add(nome.lower())
    return unicos

def obter_itens_acima_de_preco(itens, preco_limite):
    return [item for item in itens if item[1] > preco_limite]

def exibir_itens_por_categoria(itens_filtrados):
    categorias = defaultdict(list)
    for item in itens_filtrados:
        categorias[item[2]].append(item)

    print("\nItens encontrados com preço superior ao limite:")
    for categoria, itens_categoria in categorias.items():
        print(f"\nCategoria: {categoria} (Total: {len(itens_categoria)} produtos)")
        for item in itens_categoria:
            print(f"{item[0]} - R${item[1]:.2f}")

def obter_preco_limite():
    while True:
        try:
            preco_limite = float(input("Digite o preço limite para filtrar os itens (ex: 1000): R$ "))
            if preco_limite < 0:
                print("O preço limite não pode ser negativo. Tente novamente.")
            else:
                return preco_limite
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    itens = [
        ("Tênis Esportivo", 300, "Calçados"),
        ("Cadeira de Escritório", 600, "Móveis"),
        ("Smartphone", 2000, "Eletrônicos"),
        ("Camiseta", 50, "Roupas"),
        ("Cafeteira Elétrica", 400, "Eletrodomésticos"),
        ("Fritadeira Elétrica", 700, "Eletrodomésticos"),
        ("Batedeira", 350, "Eletrodomésticos"),
        ("Geladeira Inox", 3500, "Eletrodomésticos"),
        ("Sofá Retrátil", 2500, "Móveis"),
        ("Cama King Size", 1800, "Móveis"),
        ("Mesa de Jantar", 1200, "Móveis"),
        ("Escrivaninha", 800, "Móveis"),
        ("Luminária LED", 150, "Iluminação"),
        ("Jogo de Panelas", 350, "Cozinha"),
        ("Aspirador de Pó", 450, "Eletrodomésticos"),
        ("Torradeira", 200, "Cozinha"),
        ("Tênis Casual", 150, "Calçados"),
        # Duplicatas
        ("Tênis Esportivo", 350, "Calçados"),
        ("Cafeteira Elétrica", 500, "Eletrodomésticos"),
        ("Smartphone", 2100, "Eletrônicos"),
        ("Sofá Retrátil", 2800, "Móveis"),
        ("Cama King Size", 1700, "Móveis"),
        ("Jogo de Panelas", 400, "Cozinha"),
        ("Aspirador de Pó", 500, "Eletrodomésticos"),
        ("Escrivaninha", 850, "Móveis")
    ]

    preco_limite = obter_preco_limite()
    itens_filtrados = obter_itens_acima_de_preco(itens, preco_limite)
    exibir_itens_por_categoria(itens_filtrados)

    comando = input("\nDeseja remover duplicatas? Digite: remove duplicatas\n> ").strip().lower()
    if comando == "remove duplicatas":
        print("\nRemovendo duplicatas por nome...")
        itens_sem_duplicatas = remover_duplicatas_por_nome(itens_filtrados)
        exibir_itens_por_categoria(itens_sem_duplicatas)
    else:
        print("\nNenhuma duplicata foi removida.")

main()


