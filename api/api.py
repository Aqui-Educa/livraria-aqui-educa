from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import csv
from csv import writer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

clienteFile = '../db/cliente.csv'
categoriaFile = '../db/categoria.csv'
editoraFile = '../db/editora.csv'
idiomaFile = '../db/idioma.csv'
vendaFile = '../db/venda.csv'
depoimentoFile = '../db/depoimento.csv'

@app.route('/cliente/inserir', methods=['POST'])
def inserirCliente():
    cliente = json.loads(request.data)
    inserirClienteCsv(cliente)
    return { 'message': 'Cliente salvo com sucesso' }


@app.route('/cliente/listar', methods=['GET'])
def listarCliente():
    clientes = listarClienteCsv()
    return json.dumps(clientes)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/cliente/deletar/<nroLinha>', methods=['DELETE'])
def deletarCliente(nroLinha):
    clientes = listarClienteCsv()
    novosClientes = []       

    i = 0
    for cliente in clientes:        
        if int(nroLinha) != i:
            novosClientes.append(cliente)
        i = i + 1

    reinserirClienteCsv(novosClientes)
    return { 'message': 'Cliente deletado com sucesso' }


def listarClienteCsv():
    clientes = []
    with open(clienteFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                clientes.append({ 
                    'nome': linha[0], 
                    'telefone': linha[1], 
                    'email': linha[2],
                    'cpf': linha[3]
                })
            count += 1

    return clientes


def inserirClienteCsv(cliente):
    novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"], cliente["cpf"]]
    with open(clienteFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirClienteCsv(clientes):
    linhas = []
    linhas.append(["nome", "telefone", "email", "cpf"]) #é necessário inserir novamente o cabeçalho da planilha

    for cliente in clientes:
        novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"], cliente["cpf"]]
        linhas.append(novaLinha)

    with open(clienteFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()


        ###########################################

# C A T E G O R I A

@app.route('/categoria/inserir', methods=['POST'])
def inserirCategoria():
    categoria = json.loads(request.data)
    inserirCategoriaCsv(categoria)
    return { 'message': 'Categoria salvo com sucesso' }


@app.route('/categoria/listar', methods=['GET'])
def listarCategoria():
    categoria = listarCategoriaCsv()
    return json.dumps(categoria)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/categoria/deletar/<nroLinha>', methods=['DELETE'])
def deletarCategoria(nroLinha):
    categorias = listarCategoriaCsv()
    novosCategorias = []       

    i = 0
    for categoria in categorias:        
        if int(nroLinha) != i:
            novosCategorias.append(categoria)
        i = i + 1

    reinserirCategoriaCsv(novosCategorias)
    return { 'message': 'Categoria deletado com sucesso' }


def listarCategoriaCsv():
    categorias = []
    with open(categoriaFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                categorias.append({ 
                    'id': linha[0], 
                    'tipo_categoria': linha[1]
                })
            count += 1

    return categorias


def inserirCategoriaCsv(categoria):
    novaLinha = [categoria["id"], categoria["tipo_categoria"]]
    with open(categoriaFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirCategoriaCsv(categorias):
    linhas = []
    linhas.append(["id", "tipo_categoria"]) #é necessário inserir novamente o cabeçalho da planilha

    for categoria in categorias:
        novaLinha = [categoria["id"], categoria["tipo_categoria"]]
        linhas.append(novaLinha)

    with open(categoriaFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()        


        ###########################################

# E D I T O R A


@app.route('/editora/inserir', methods=['POST'])
def inserirEditora():
    editora = json.loads(request.data)
    inserirEditoraCsv(editora)
    return { 'message': 'Editora salva com sucesso' }


@app.route('/editora/listar', methods=['GET'])
def listarEditora():
    editora = listarEditoraCsv()
    return json.dumps(editora)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/editora/deletar/<nroLinha>', methods=['DELETE'])
def deletarEditora(nroLinha):
    editoras = listarEditoraCsv()
    novosEditoras = []       

    i = 0
    for editora in editoras:        
        if int(nroLinha) != i:
            novosEditoras.append(editora)
        i = i + 1

    reinserirEditoraCsv(novosEditoras)
    return { 'message': 'Editora deletada com sucesso' }


def listarEditoraCsv():
    editoras = []
    with open(editoraFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                editoras.append({ 
                    'id': linha[0], 
                    'nome': linha[1], 
                    'fundacao': linha[2],
                    'estado': linha[3],
                    'pais': linha[4]
                })
            count += 1

    return editoras


def inserirEditoraCsv(editora):
    novaLinha = [editora["id"], editora["nome"], editora["fundacao"], editora["estado"], editora["pais"]]
    with open(editoraFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirEditoraCsv(editoras):
    linhas = []
    linhas.append(["id", "nome", "fundacao", "estado", "pais"]) #é necessário inserir novamente o cabeçalho da planilha

    for editora in editoras:
        novaLinha = [editora["id"], editora["nome"], editora["fundacao"], editora["estado"], editora["pais"]]
        linhas.append(novaLinha)

    with open(editoraFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

###########################################

# I D I O M A


@app.route('/idioma/inserir', methods=['POST'])
def inserirIdioma():
    idioma = json.loads(request.data)
    inserirIdiomaCsv(idioma)
    return { 'message': 'Idioma salvo com sucesso' }


@app.route('/idioma/listar', methods=['GET'])
def listarIdioma():
    idioma = listarIdiomaCsv()
    return json.dumps(idioma)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/idioma/deletar/<nroLinha>', methods=['DELETE'])
def deletarIdioma(nroLinha):
    idiomas = listarIdiomaCsv()
    novosIdiomas = []       

    i = 0
    for idioma in idiomas:        
        if int(nroLinha) != i:
            novosIdiomas.append(idioma)
        i = i + 1

    reinserirIdiomaCsv(novosIdiomas)
    return { 'message': 'Idioma deletado com sucesso' }


def listarIdiomaCsv():
    idiomas = []
    with open(idiomaFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                idiomas.append({ 
                    'id': linha[0], 
                    'idioma': linha[1]
                })
            count += 1

    return idiomas


def inserirIdiomaCsv(idioma):
    novaLinha = [idioma["id"], idioma["idioma"]]
    with open(idiomaFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirIdiomaCsv(idiomas):
    linhas = []
    linhas.append(["id", "idioma"]) #é necessário inserir novamente o cabeçalho da planilha

    for idioma in idiomas:
        novaLinha = [idioma["id"], idioma["idioma"]]
        linhas.append(novaLinha)

    with open(idiomaFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()


###########################################

# V E N D A


@app.route('/venda/inserir', methods=['POST'])
def inserirVenda():
    venda = json.loads(request.data)
    inserirVendaCsv(venda)
    return { 'message': 'Venda salva com sucesso' }


@app.route('/venda/listar', methods=['GET'])
def listarVenda():
    venda = listarVendaCsv()
    return json.dumps(venda)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/venda/deletar/<nroLinha>', methods=['DELETE'])
def deletarVenda(nroLinha):
    vendas = listarVendaCsv()
    novosVendas = []       

    i = 0
    for venda in vendas:        
        if int(nroLinha) != i:
            novosVendas.append(venda)
        i = i + 1

    reinserirVendaCsv(novosVendas)
    return { 'message': 'Venda deletada com sucesso' }


def listarVendaCsv():
    vendas = []
    with open(vendaFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                vendas.append({ 
                    'idTitulo': linha[0], 
                    'quantidade': linha[1],
                    'valor': linha[2]
                })
            count += 1

    return vendas


def inserirVendaCsv(venda):
    novaLinha = [venda["idTitulo"], venda["quantidade"], venda["valor"]]
    with open(vendaFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirVendaCsv(vendas):
    linhas = []
    linhas.append(["idTitulo", "quantidade", "valor"]) #é necessário inserir novamente o cabeçalho da planilha

    for venda in vendas:
        novaLinha = [venda["idTitulo"], venda["quantidade"], venda["valor"]]
        linhas.append(novaLinha)

    with open(vendaFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

###########################################

# D E P O I M E N T O 

@app.route('/depoimento/inserir', methods=['POST'])
def inserirDepoimento():
    depoimento = json.loads(request.data)
    inserirDepoimentoCsv(depoimento)
    return { 'message': 'Depoimento salvo com sucesso' }


@app.route('/depoimento/listar', methods=['GET'])
def listarDepoimento():
    depoimentos = listarDepoimentoCsv()
    return json.dumps(depoimentos)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/depoimento/deletar/<nroLinha>', methods=['DELETE'])
def deletarDepoimento(nroLinha):
    depoimentos = listarDepoimentoCsv()
    novosDepoimentos = []       

    i = 0
    for depoimento in depoimentos:        
        if int(nroLinha) != i:
            novosDepoimentos.append(depoimento)
        i = i + 1

    reinserirDepoimentoCsv(novosDepoimentos)
    return { 'message': 'Depoimento deletado com sucesso' }


def listarDepoimentoCsv():
    depoimentos = []
    with open(depoimentoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                depoimentos.append({ 
                    'nome': linha[0], 
                    'depoimento': linha[1]
                })
            count += 1

    return depoimentos


def inserirDepoimentoCsv(depoimento):
    novaLinha = [depoimento["nome"], depoimento["depoimento"]]
    with open(depoimentoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirDepoimentoCsv(depoimentos):
    linhas = []
    linhas.append(["nome", "depoimento"]) #é necessário inserir novamente o cabeçalho da planilha

    for depoimento in depoimentos:
        novaLinha = [depoimento["nome"], depoimento["depoimento"]]
        linhas.append(novaLinha)

    with open(depoimentoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()



