import os

print("Sistema Operacional")
while True:
    print("1- ls")
    print("2- mkdir")
    print("3- cd path")
    print("4- pwd")
    print("9- sair")
    opcao = input("Opção: ")
    if opcao == "1":
        os.system("ls")
    elif opcao == "2":
        diretorio = input("Nome do diretório: ")
        os.mkdir(diretorio)
    elif opcao == "3":
        cd = input("Informe o path: ")
        os.chdir(cd)
    elif opcao == "4":
        os.system("pwd")
    elif opcao == "9":
        print("Exit Sistema Operacional")
        break


