from time import sleep
from random import choices


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


def GerarSenha(tam):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@$%&*-_=+'
    senha = ''

    for i in range(1, tam+1):
        carac = choices(alpha)
        senha += str(carac[0])
    return senha


""" t = int(input('Que tamanho deseja a senha: '))
print('Gerando...')
sleep(1)
senha = GerarSenha(t)
print('Sua senha é: ')
print(senha)
 """
