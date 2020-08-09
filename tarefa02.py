usuario = input("Informe o nome de usuario: ")
senha = input("Informe a senha: ")

while (senha == usuario):
    print("A senha é igual ao nome de usuário. Informe os dados novamente.")
    usuario = input("Informe o nome de usuario: ")
    senha = input("Informe a senha: ")

if(senha != usuario):
    print("Dados válidos!")