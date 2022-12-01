pretot1 = 0
pretot2 = 0
pretot3 = 0
vlrmenor = 1000000
vlrmaior = 0
valorprimeiraparcela = 0

for transacao in range(15):
  print("Transação", transacao+1)
  print("Utilize 'V' para transação a vista e 'P' para transação a prazo")
  
  transacaovp = input()
  print("Digite o preço da transação")
  preco = int(input())
  
  if transacaovp == "v" or "V":
    pretot1 += preco
    print("O valor total das compras a vista é", pretot1)
      
  
  if transacaovp == "p" or "P":
    pretot2 += preco
    valorprimeiraparcela = preco / 3
    pretot3 += preco
    print("o primeiro valor da parcela é", valorprimeiraparcela)

    if preco < vlrmenor:
      vlrmenor = preco
       
    if preco > vlrmaior:
      vlrmaior = preco


  
print("o valor maior é de R$:", vlrmaior)
print("o valor menor é de R$", vlrmenor)     
print("O valor total das compras a prazo e", pretot2)
print("O valor total das compras e", pretot3)

    