agenda = {}

def adicionar_contato():
    """
    Adiciona um novo contato à lista de contatos:
    Pedindo o nome do contato
    Pedindo o telefone do contato
    Pedindo o email do contato
    Pedindo se o contato é favorito ou não
    Criando um dicionário com os dados do contato
    Adicionando o dicionário à lista de contatos
    """
    nome = input("Digite o nome do contato: ").strip().title() #São funções que irão tirar os espaços brancos e colocar todos os nomes em letras maiuscula!
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("O contato é favorito? (s/n): ")
    agenda[nome] = {
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    print("Contato adicionado com sucesso!")


#Mostra a lista de contatos disponíveis
def exibirLista():
    if agenda:
      print("Lista de contatos:")
      for nome, contato in agenda.items():
        print(f"Nome: {nome}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print(f"Favorito: {contato['favorito']}")
        
    else:
      print("A lista de contatos está vazia.")


"""
Vamos perguntar ao usúario o nome do contato, 
verificar se este contato está na lista 
e então irá retornar o resultado
"""
def buscar_Contato():
    nome = input("Digite o nome do contato que deseja buscar: ").strip().title()
    if nome in agenda:
       print(f"nome:{nome}")
       print(f"telefone{agenda[nome]}")
    
    else:
       print("Contato não encontrado")

"""
Está pedindo o nome do contato que está procurando para deletar,
vai verificar se o contato existe na lista 
e então retornar o resultado
"""
def deletar():
   nome = input("Nome do contato que deseja deletar:")
   if nome in agenda:
      del agenda[nome]
      print("Contato deletado!")

   else:
      print("Contato não encontrado!")

def menu():
    """
    O menu principal 
    """
    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Editar contato")
        print("4. Marcar/desmarcar favorito")
        print("5. Visualizar contatos favoritos")
        print("6. Apagar contato")
        print("7. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            visualizar_contatos()
        elif escolha == '3':
            editar_contato()
        elif escolha == '4':
            marcar_favorito()
        elif escolha == '5':
            visualizar_favoritos()
        elif escolha == '6':
            apagar_contato()
        elif escolha == '7':
            print("Saindo da aplicação...")
            break
        else:
            print("Escolha inválida! Tente novamente.")

#iniciar a aplicação
menu()
