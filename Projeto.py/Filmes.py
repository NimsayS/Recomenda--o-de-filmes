print('\033[34m*'*50)
print('Operador do serviço\n')
def processando():
    print('\nPROCESSANDO...\n')
    print('Filmes registrados com sucesso!\n')
    print('\33[31m*'*50)
    

def pegaFilmes(tamanho):
    filmes = []
    for i in range(tamanho):
        filmes.append(input(f'Digite o {i+1}º filme: '))
        print('-'*50)
    return filmes


def usuarioAssistiu(filmes):
    filmesAssistidos = []
    for i in range(len(filmes)):
        assistiu = input(f'Você já assistiu: {filmes[i].strip().title()}? [S/N] ').upper().strip()
        filmesAssistidos.append(assistiu == 'S')
        print('-'*50)
    return filmesAssistidos
        

def recomendacao(usuario1, usuario2, filmes):
    recom = []
    for i in range(len(filmes)):
        recom.append(usuario1[i] and not usuario2[i])
    return recom


def transforma(recom, filmes):
    recomendacoes = []
    for i in range(len(filmes)):
        if recom[i]:
            recomendacoes.append(filmes[i])
    return recomendacoes


tamanho = 10
filmes = pegaFilmes(tamanho)
processando()

print('Usuário 1\n')
print('-'*50)

usuario1 = usuarioAssistiu(filmes)

print('\nUsuário 2\n')
print('-'*50)

usuario2 = usuarioAssistiu(filmes)

recom1 = recomendacao(usuario2, usuario1, filmes)
recom2 = recomendacao(usuario1, usuario2, filmes)

Resul1 = transforma(recom1, filmes)
Resul2 = transforma(recom2, filmes)
R1=str(Resul1)[1:-1]
R2=str(Resul2)[1:-1]

print('\033[33m*'*50)
print('\nRecomendações do usuário 1')
print('-'*50)
print(f'Tente assisitir:{R1}.')
print('\nRecomendações do usuário 2')
print('-'*50)
print(f'Tente assistir: {R2}.\n')
print('*'*50)