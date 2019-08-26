import os

print("Sistema Operacional")


def sistemaOperacionalLinux(opcao):
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
        print("Exit Linux")

def sistemaOperacionalWindows(opcao):
    if opcao == "1":
        os.system("dir")
    elif opcao == "2":
        diretorio = input("Nome do diretório: ")
        os.mkdir(diretorio)
    elif opcao == "3":
        cd = input("Informe o path: ")
        os.chdir(cd)
    elif opcao == "4":
        os.system("pwd")
    elif opcao == "9":
        print("Exit Windows")

sistema = input("Windows ou Linux: ")
while True:
    print("1- ls")
    print("2- mkdir")
    print("3- cd path")
    print("4- pwd")
    print("9- sair")
    opcao = input("Opção: ")
    if sistema == "linux":
        sistemaOperacionalLinux(opcao)
    elif sistema == "windows":
        sistemaOperacionalWindows(opcao)








