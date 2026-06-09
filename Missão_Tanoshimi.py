def mostrar_cardapio():
  cardapio = {"Makimono":50.00, "Sushi": 50.00, "Tempurá de frutos do mar": 25.00, "Tempurá de sorvete": 28.00, "Saquê": 40.00 }
  
  print(f"-----cardapio----- \n")
  for item, precos in cardapio.items():
    print(F"Temos o produto: {item} valor: {precos}")
  return cardapio 




cardapio = mostrar_cardapio()

def fazer_pedido():
  pedido = []
  total = 0.0
  while True:
   
    item_escolhido = input("Digite o nome do produto escolhido ou 'sair' para finalizar: ")

    
    if item_escolhido.lower() == "sair":
      break 

    elif item_escolhido in cardapio:
      quantidade = int(input(f"quantos(as) {item_escolhido} você deseja?"))
      pedido.append({"item": item_escolhido, "quantidade": quantidade, "preço": cardapio[item_escolhido]})
      total += cardapio[item_escolhido] * quantidade
      print(f"{quantidade}x {item_escolhido} adicionado(s)!")
    
    else:
      print("Item não encontrado no cardápio. Tente novamente.")
    
fazer_pedido()

