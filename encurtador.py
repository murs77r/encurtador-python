import requests
import json
import os

API_URL = "" #adicionar posteriormente
API_TOKEN = "" #adicionar posteriormente

def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_terminal()
    print("ENCURTADOR DE URL")
    print("")
    print("1 - Adicionar URL")
    print("2 - Editar URL")
    print("3 - Excluir URL")
    print("4 - Sair")
    print("")

def confirmar_informacao(mensagem):
    while True:
        confirmacao = input(f"{mensagem} (S/N): ").lower()
        if confirmacao == "S":
            return True
        elif confirmacao == "N":
            return False
        else:
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")

def adicionar_url():
    while True:
        short = input("URL Curta desejada: ")
        if confirmar_informacao(f"URL Curta: {short}. Está correto?"):
            break
        else:
            print("URL Curta reiniciada.")
            continue

    while True:
        long = input("URL Longa: ")
        if confirmar_informacao(f"URL Longa: {long}. Está correto?"):
            break
        else:
            print("URL Longa reiniciada.")
            continue


    data = {
        "metodo": "adicao",
        "short": short,
        "long": long,
        "token": API_TOKEN
    }
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        print(f"URL Criada: {response.text}")
        input("Pressione qualquer letra para continuar... ")
        clear_terminal()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar URL: {e}")
        input("Pressione qualquer letra para continuar... ")
        clear_terminal()

def editar_url():
    while True:
        short = input("URL Curta a ser editada: ")
        if confirmar_informacao(f"URL Curta: {short}. Está correto?"):
            break
        else:
            print("URL Curta reiniciada.")
            continue

    while True:
        long = input("Nova URL Longa: ")
        if confirmar_informacao(f"URL Longa: {long}. Está correto?"):
            break
        else:
            print("URL Longa reiniciada.")
            continue

    data = {
        "metodo": "edicao",
        "short": short,
        "long": long,
        "token": API_TOKEN
    }
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        print(f"URL Editada: {response.text}")
        input("Pressione qualquer letra para continuar... ")
        clear_terminal()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao editar URL: {e}")
        input("Pressione qualquer letra para continuar... ")
        clear_terminal()

def excluir_url():
    while True:
        short = input("URL Curta a ser excluída: ")
        if confirmar_informacao(f"URL Curta: {short}. Está correto?"):
            break
        else:
            print("URL Curta reiniciada.")
            continue

    data = {
        "metodo": "exclusao",
        "short": short,
        "long": "dummy",
        "token": API_TOKEN
    }
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        print(f"URL Excluída: {response.text}")
        input("Pressione qualquer letra para continuar... ")
        clear_terminal()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao excluir URL: {e}")
        input("Pressione qualquer letra para continuar... ")
        clear_terminal()

while True:
    display_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_url()
    elif opcao == "2":
        editar_url()
    elif opcao == "3":
        excluir_url()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")