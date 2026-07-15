print("-" * 40)
print("Bem-vindo ao Sistema de Compras!")
print("-" * 40)
print("")

print("Digite o nome do produto: ")
nome_produto = input()

print("Digite o valor do produto em reais (R$): ")
valor_produto = float(input())

print("Digite a quantidade de produtos: ")
quantidade_produto = int(input())

valor_total = valor_produto * quantidade_produto

if(valor_total > 100):
    print("Você ganhou um desconto de 10%!")
    valor_total = valor_total - (valor_total * 0.1)
    print(f"Valor total da compra: R$ {valor_total}")

else:
    print(f"Valor total da compra: R$ {valor_total}")