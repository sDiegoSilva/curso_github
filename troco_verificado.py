# Este programa deve verificar o preço do produto, quantidade, valor recebido.
# Este programa deve tambem calcular o troco e se falta quantia dada pelo cliente

# A quantidade de "print" no bloco é para o usuario acompanhar os valores
preco_unitario_produto = float(input("Digite o preço unitário do produto em reis: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))
dinheiro_recebido = float(input("Digite o valor recebido nesta venda: "))
print(f">>>>>>> Este produto custa R${preco_unitario_produto:5.2f}.")
print(f">>>>>>> Você vendeu {quantidade_comprada} deste produto.")
print(f">>>>>>> Você recebeu R${dinheiro_recebido:5.2f} do cliente.")
print("=============================================================")
print("====================== RESUMO ===============================")
venda_total = preco_unitario_produto * quantidade_comprada
print(f">>>>>>> O valor final da venda é de R${venda_total:5.2f}. <<<<<<<")

if dinheiro_recebido > venda_total:
    troco = dinheiro_recebido - venda_total
    print(f"Você recebeu R${dinheiro_recebido:5.2F}, a venda ficou em R${venda_total:5.2f} e o troco é de R${troco:5.2f}.")
    print("Volte sempre!!!")
elif dinheiro_recebido == venda_total:
    print(f"Tudo certo com sua compra. Volte sempre!!!")
else: 
    dinheiro_recebido < venda_total
    troco = venda_total - dinheiro_recebido
    print(f"Valor insuficiente para completar essa compra. Faltam R${troco:5.2f}.")
print("=============================================================")
