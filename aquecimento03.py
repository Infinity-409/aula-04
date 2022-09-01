usuario = input("Informe o usuário: ")
senha = int(input("Informe a senha: "))

if (usuario == 'admin') and senha == 619:
    print("Acesso liberado.")
else: 
    print("ATENÇÂO: ACESSO NEGADO!")
    print("Tente novamente.")