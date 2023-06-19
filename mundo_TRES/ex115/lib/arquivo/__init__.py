from lib.interface import *

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro ao criar o arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo.")
    else:
        rotulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:.<30}{dado[1]:.>10} anos")
        print(a.read())
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f"Falha ao tentar abrir {arquivo}")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print(f"Falha ao inserir dados no arquivo {arquivo}")
        else:
            print(f"Novo registro [bold blue]{nome}[/bold blue] adicionado!")
            a.close()

    
