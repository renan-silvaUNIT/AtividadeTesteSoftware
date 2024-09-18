usuarios = {"karl": "senha123",
            "ana": "senha456",
            "joao": "senha789"}

def cadastrar():
    print("=== Cadastro de Novo Usuário ===")
    
    while True:
        novo_username = input("Digite o nome de usuário: ")
        
        if novo_username in usuarios:
            print("Nome de usuário já existe! Tente outro.")
        else:
            nova_senha = input("Digite uma senha: ")
            usuarios[novo_username] = nova_senha
            print(f"Usuário {novo_username} cadastrado com sucesso!")
            break
                    

def login():
    print("=== Sistema de Login ===")

    username = input("Digite seu nome de usuário: ")

    if username in usuarios:
        password = input("Digite sua senha: ")

        if usuarios[username] == password:
            print("Login bem-sucedido! Bem-vindo(a),", username)
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")

def menu():
    while True:
        print("\n=== Sistema ===")
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1/2/3): ")
        
        if opcao == "1":
            login()
        elif opcao == "2":
            cadastrar()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

menu()
