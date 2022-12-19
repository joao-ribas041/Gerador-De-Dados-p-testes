import random

# Gerar Nomes
def gerarNomes():
    nomes = ['João', 'Tomas', 'Aguiar', 'Nei', 'Mariana']
    return random.choices(nomes)

# Gerar e-mail
def gerarEmails():
    emails = ['email1@email.com', 'email2@email.com', 'email3@email.com', 'email4@email.com', 'email5@email.com']
    return random.choices(emails)
    
# Gerar telefone
def gerarTelefones():
    telefones = ['(41)00000-0001', '(41)00000-0002', '(41)00000-0003', '(41)00000-0004', '(41)00000-0005']
    return random.choices(telefones)
    

# Gerar Cidade
def gerarCidades():
    cidades = ['Cidade 1', 'Cidade 2', 'Cidade 3', 'Cidade 4', 'Cidade 5']
    return random.choices(cidades)

# Gerar Estados
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
    return random.choices(estados)