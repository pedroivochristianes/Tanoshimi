# 1. Funções matemáticas da Matriz Operacional (slide 7)
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    # Gatilho de segurança: if b != 0
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"




def mostrar_cardapio():
  cardapio = {"makimono":20.00, "sushi": 20.00, "tempurá": 25.00, "tempurá de sorvete": 28.00, "saquê": 40.00 }
  
  print(f"-----cardapio----- \n")
  for item, precos in cardapio.items():
    print(F"Temos o produto: {item} valor: {precos}")
  return cardapio 






def fazer_pedido():
    pedido = []
    total = 0.0
    cardapio = mostrar_cardapio()
    while True:
      try:
          item_escolhido = input("Digite o nome do produto escolhido ou 'sair' para finalizar: ").lower()

          if item_escolhido.lower() == "sair":
            break 

          elif item_escolhido in cardapio:
            quantidade = int(input(f"quantos(as) {item_escolhido} você deseja?"))
            pedido.append({"item": item_escolhido, "quantidade": quantidade, "preço": cardapio[item_escolhido]})
            total += cardapio[item_escolhido] * quantidade
            print(f"{quantidade}x {item_escolhido} adicionado(s)! R$ {total:.2f}.")
    
          else:
            print("Item não encontrado no cardápio. Tente novamente.")

          return total
      
      except ValueError as e:
        print(f"Erro. Detalhes {e}")
        print("Escreva corretamente o item desejado.")

      
        


# 4. Etapa 3: Saída - fechar_conta (slide 12)
def fechar_conta(total_sem_taxa):
    taxa = multiplicacao(total_sem_taxa, 0.10)  # 10% de taxa de serviço
    total_com_taxa = soma(total_sem_taxa, taxa)
    
    print("\n--- CONTA FINAL ---")
    print(f"Total consumido: R$ {total_sem_taxa:.2f}")
    print(f"Taxa de serviço (10%): R$ {taxa:.2f}")
    print(f"Total a pagar: R$ {total_com_taxa:.2f}")
    return total_com_taxa

# 5. Execução principal - Integração completa (slide 12)
def main():
    print("=== Bem-vindo ao Restaurante Tanoshimi ===")
    
    total_sem_taxa = fazer_pedido()
    if total_sem_taxa > 0:
        fechar_conta(total_sem_taxa)
    else:
        print("Nenhum pedido foi realizado. Até logo!")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()


