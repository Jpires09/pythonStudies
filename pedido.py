from cgi import print_form


def main():
  n = 4

  total = 0

  for i in range(1, n + 1):
    pedido = input.split(" ")
    print(pedido)
    nome = pedido[0]
    print(nome)
    valor = float(pedido[1])
    print(valor)
    total += valor
    # desconto = float(pedido[2] / 100)

  print(f"Valor total: {total }")

input = """Pizza 19.99 Salada 29.99 Sushi 61.00 Pudim 10.00 20%"""
main()