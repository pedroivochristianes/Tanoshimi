def mostrar_cardapio():
  cardapio = {"Makimono":50.00, "sushi": 50.00, "Tempurá de frutos do mar": 25.00, "Tempurá de Sorvete": 28.00, "Saquê": 40.00 }
  
  print(f"-----cardapio----- \n")
  for item, precos in cardapio.items():
    print(F"Temos o produto: {item} valor: {precos}")
  return cardapio 


mostrar_cardapio()


#def fazer_pedido():
#   pedido = []
#   total = 0.0

#   item_escolhido = input("Digite o nome do produto escolhido: ")


