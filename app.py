import random
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

# Parar aplicação
def finalizar_aplicacao():
    resultado = str(input('Deseja Continuar rodando? "parar" para finalizar: '))
    if resultado == 'parar':
        print('Finalizando.')
        return True
    else:
        return False



while True:
    print("""
[1] - Gerar nome
[2] - Gerar e-mail
[3] - Gerar telefone
[4] - Gerar cidade
[5] - Gerar estado
          """)
    opc = []
    opc.append(int(input('Selecione uma opção: ')))
    print(opc)
    
    if opc in 1:
        print(gerador_de_nomes()[0])
    elif opc == 2:
        print(gerador_de_emails()[0])
    elif opc == 3:
        print(gerador_de_telefones()[0])
    elif opc == 4:
        print(gerador_de_cidades()[0])
    elif opc == 5:
        print(gerador_de_estados()[0])
    else:
        print('opção invalida')
    
    """ print('\n\n')
    print(gerador_de_emails()[0])
    print(gerador_de_telefones()[0])
    print(gerador_de_cidades()[0])
    print(gerador_de_estados()[0]) """

    if finalizar_aplicacao() == True:
        break

    
print('App finalizado.')
