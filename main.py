#==================================================
# PROJETO: ANÁLISE DE VENDAS
# =================================================
vendas = [
  {
    "produto": "Notebook",
    "preco": 3500.00,
    "categoria": "Acessórios"
  },
  {
    "produto": "Mouse",
    "preco": 50.00,
    "categoria": "Acessórios"
  },
  {
    "produto": "Monitor",
    "preco": 800.00,
    "categoria": "Eletrônicos"
  },
  {
    "produto": "Teclado",
    "preco": 150.00,
    "categoria": "Acessórios"
  },
  {
    "produto": "Webcam",
    "preco": 200.00,
    "categoria": "Acessórios"
  }
]
def mostrar_produtos():
    print("\n====== PRODUTOS =======")

    for venda in vendas:
        print(
            f"Produto: {venda['produto']} | "
            f"Preço: R$ {venda['preco']:.2f} | "
            f"Categoria: {venda['categoria']}"
        )
def calcular_total():
    total = 0

    for venda in vendas:
        total += venda["preco"]

    return total
def calcular_media():
    total = calcular_total()
    media = total / len(vendas)
    return media
def produto_mais_caro():
    mais_caro = vendas[0]

    for venda in vendas:
        if venda["preco"] > mais_caro["preco"]:
            mais_caro = venda

    return mais_caro
def produto_mais_barato():
    mais_barato = vendas[0]

    for venda in vendas:
        if venda["preco"] < mais_barato["preco"]:
            mais_barato = venda

    return mais_barato
  
# Execução do programa

mostrar_produtos()

total = calcular_total()
media = calcular_media()

caro = produto_mais_caro()
barato = produto_mais_barato()

print("\n====== RESULTADOS ======")
print(f"Valor total: R$ {total:.2f}")
print(f"Preço médio: R$ {media:.2f}")

print(
    f"Produto mais caro: "
    f"{caro['produto']} - R$ {caro['preco']:.2f}"
)

print(
    f"Produto mais barato: "
    f"{barato['produto']} - R$ {barato['preco']:.2f}"
)
