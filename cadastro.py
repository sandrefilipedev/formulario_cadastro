# Sistema simples de ficha cadastral utilizando dicionários.
# O usuário pode cadastrar informações, consultar campos específicos e visualizar todos dados armazenados na ficha.

op = 0
ficha = {} 

# Loop principal do sistema, será exibido o menu de opções
while op != 4:
    print("\nSEJA BEM VINDO!, FICHA DE CADASTRO, SELECIONE A OPÇÃO DESEJADA  ")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informações da ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    op = int(input("Informe a opção desejada: "))

    #Opção 1 - Cadastro de novos campos na ficha
    if op == 1:
        #inserir dados na ficha, dados inseridos pelo usuário
        chave = input("Informe o campo que deseja cadastrar na ficha: ")
        valor = input("Informe o dados que deseja cadastrar neste campo: ")
        # Insere os dados no dicionário
        ficha[chave] = valor
        ficha.update({chave:valor})
        
    elif op == 2:
        #recuperar dados da ficha 
        print(f"Os campos diponíveis  na ficha são {ficha.keys()}")
        chave = input("Informe qual campo deseja exibir: ")

        if chave in ficha.keys():
            print(f"O campo {chave} contém o dado {ficha.get(chave)}")
        else:
            print("Você digitou um campo inexistente.")
    elif op == 3:
        #exibir ficha completa
        print("FICHA CADASTRAL")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} --> {dado}")

    elif op == 4:
        print("Saindo do sistema de ficha cadastral")
        break