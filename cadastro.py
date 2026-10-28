op = 0
ficha = {} 
while op != 4:
    print("\nFICHA CADASTRAL")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informações da ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))

    if op == 1:
        #inserir dados na ficha
        chave = input("Informe o campo que deseja cadastrar na ficha: ")
        valor = input("Informe o dados que deseja cadastrar neste campo: ")
        ficha[chave] = valor
        ficha.update({chave:valor})
        
    elif op == 2:
        #recuperar dados da ficha 
    elif op == 3:
        #exibir ficha completa
    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break