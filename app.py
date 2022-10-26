import random
import os


# Gerador de dados
# Gerar Nomes
def gerador_de_nomes():
    nomes = ['João', 'Tomas', 'Aguiar', 'Nei', 'Mariana']
    return random.choices(nomes)

# Gerar e-mail
def gerador_de_emails():
    emails = ['email1@email.com', 'email2@email.com', 'email3@email.com', 'email4@email.com', 'email5@email.com']
    return random.choices(emails)
    
# Gerar telefone
def gerador_de_telefones():
    telefones = ['(41)00000-0001', '(41)00000-0002', '(41)00000-0003', '(41)00000-0004', '(41)00000-0005']
    return random.choices(telefones)
    

# Gerar Cidade
def gerador_de_cidades():
    cidades = ['Cidade 1', 'Cidade 2', 'Cidade 3', 'Cidade 4', 'Cidade 5']
    return random.choices(cidades)

# Gerar Estados
def gerador_de_estados():
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

# Salvar Arquivos?
def salvar_arquivos(r1, r2, r3, r4, r5):
    with open('Gerador De Dados p-testes/Dados.txt', 'a', newline='') as arquivo:
        if r1 != '':
            arquivo.write(r1 + os.linesep)
        if r2 != '':
            arquivo.write(r2 + os.linesep)
        if r3 != '':
            arquivo.write(r3 + os.linesep)
        if r4 != '':
            arquivo.write(r4 + os.linesep)
        if r5 != '':
            arquivo.write(r5 + os.linesep)
        arquivo.write('-'*25 + os.linesep)
        
            


while True:
    result1 = result2 = result3 = result4 = result5 = ''
    print('Bem-vindo \nGerador de Dados p. testes \nPara Finalizar digite "parar".')
    print('-'*35)
    print("""[1] - Gerar nome
[2] - Gerar e-mail
[3] - Gerar telefone
[4] - Gerar cidade
[5] - Gerar estado""")
    opc = str(input('Selecione uma opção: '))
    salvar = str(input('Deseja salvar os dados em um arquivo de texto?[s/n] '))
    print(salvar)
    
    print('\n')
    print('-'*35)
    
    if "parar" in opc:
        print('Finalizando o programa.')
        break
    if str(1) in opc:
        result1 = gerador_de_nomes()[0]
        print(result1)
    if str(2) in opc:
        result2 = gerador_de_emails()[0]
        print(result2)
    if str(3) in opc:
        result3 = gerador_de_telefones()[0]
        print(result3)
    if str(4) in opc:
        result4 = gerador_de_cidades()[0]
        print(result4)
    if str(5) in opc:
        result5 = gerador_de_estados()[0]
        print(result5)
    
    if 's' in salvar:
        salvar_arquivos(result1, result2,  result3, result4, result5)
    print('-'*35)

print('App finalizado.')
