from time import sleep
from random import choices, randint


def gerarNomes():
    nomes = ['João', 'Tomas', 'Aguiar', 'Nei', 'Mariana']
    return choices(nomes)[0]


def gerarEmails():
    emails = ['email1@email.com', 'email2@email.com',
              'email3@email.com', 'email4@email.com', 'email5@email.com']
    return choices(emails)[0]


def gerarTelefones():
    telefones = ['(41)00000-0001', '(41)00000-0002',
                 '(41)00000-0003', '(41)00000-0004', '(41)00000-0005']
    return choices(telefones)[0]


def gerarCidades():
    cidades = ['Cidade 1', 'Cidade 2', 'Cidade 3', 'Cidade 4', 'Cidade 5']
    return choices(cidades)[0]


def gerarEstados():
    estados = [
        'Acre', 'Alagoas', 'Amapá', 'Amazonas',
        'Bahia', 'Ceará', 'Espírito Santo', 'Goiás',
        'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais',
        'Pará', 'Paraíba', 'Paraná', 'Pernambuco',
        'Piauí', 'Rio De Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',
        'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo',
        'Sergipe', 'Tocantins', 'Distrito Federal'
    ]
    return choices(estados)[0]


def GerarSenha(mai=0, min=0, n=0, c=0, tam=8):
    maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minuscula = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '1234567890'
    caracteres = '!@#$%^&*()_-=+'
    geral = senha = ''

    if mai == 1:
        geral += maiuscula

    if min == 1:
        geral += minuscula

    if n == 1:
        geral += numeros

    if c == 1:
        geral += caracteres

    for i in range(0, tam):
        senha += geral[randint(0, len(geral))]
    return senha

    """ 
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@$%&*-_=+'
    senha = ''

    for i in range(1, tam+1):
        carac = choices(alpha)
        senha += str(carac[0])
    return senha
 """


while True:
    # ma = int(input('Deseja selecionar maiuscula? [1/0] '))
    # mi = int(input('Deseja selecionar minuscula? [1/0] '))
    nu = int(input('Deseja selecionar numeros? [1/0] '))
    # ca = int(input('Deseja selecionar caracteres? [1/0] '))
    t = int(input('Qual o tamanho da senha? '))

    # senha = GerarSenha(ma, mi, nu, ca, 8)
    senha = GerarSenha(n=nu, tam=t)
    print(senha)
    print()
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    print()

    if resp in 'Nn':
        break

print('Finalizado')
