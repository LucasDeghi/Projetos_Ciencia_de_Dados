import texto
#Aqui o comando import está trazendo um arquivo texto separado deste
#Para que qualquer texto possa ser analisado sem alterar o código

#Importante ressaltar que as funções estão primeiro, pois serão lidas primeiro,
#e os parametros fornecidos serão "alimentados" pelo texto fornecido

#Contagem de sílabas, receberá uma lista de palavras
#essa lista é o texto analisado com a função split()
#Iterando cada palavra na lista de Palavras temos a soma
#das silabas válidadas pela função contagem_silabas_na_palavra

def contagem_silabas(palavras):
    contagem = 0


    for palavra in palavras:
        contagem_palavras = contagem_silabas_na_palavra(palavra)
        contagem += contagem_palavras
    # O return serve para retornar a leitura do código na variável selecionada
    return contagem

#Validação para dos itens da lista palavras para que sejam removidos
#Os caracteres .,!?:; , os 'e's no final das palavras (mudo no inglês)
#A contagem começa com a validação de que se a palavra tiver 3 letras ou
#menos ela já conta como uma sílaba, caso contrário, conta-se o nº de vogais
#Isso se chama Heurística, um tipo de algoritmo imperfeito ou o mais próximo possível da resposta
def contagem_silabas_na_palavra(palavra):
    contagem = 0
    final_da_palavra = '.,!?:;'
    ultimo_caractere = palavra[-1]

    if ultimo_caractere in final_da_palavra:
        palavra_processada =  palavra[0:-1]
    else:
        palavra_processada = palavra

    if len(palavra_processada) <= 3:
        return 1

    if palavra_processada[-1] in 'eE':
        palavra_processada = palavra_processada[0:-1]

    vogais = "aeiouAEIOU"
    palavra_anterior_era_vogal = False

    for caractere in palavra_processada:
        if caractere in vogais:
            if not palavra_anterior_era_vogal:
                contagem += 1
            palavra_anterior_era_vogal = True
        else:
            palavra_anterior_era_vogal = False

    if palavra_processada[-1] in 'yY':
        contagem += 1

    return contagem

def contagem_frases(texto_analisado):   #Para contar o nº de frases, contamos os caracteres terminais .,!?:;
    contagem = 0

    for caractere in texto_analisado:
        if caractere in '.;?!':
            contagem += 1
    return contagem

#Aqui teremos a resposta da análise, ou seja
#o nível de leitura do texto analisado mediante a
#fórmula Legibilidade de Flesch (Vista abaixo)
def resultado_final(pontuação):
    if pontuação >= 90:
        print('Nível de leitura igual a 10-11 anos de idade')
    elif pontuação >= 80:
        print('Nível de leitura igual a 11-12 anos de idade')
    elif pontuação >= 70:
        print('Nível de leitura igual a 12-13 anos de idade')
    elif pontuação >= 60:
        print('Nível de leitura igual a 13-15 anos de idade')
    elif pontuação >= 50:
        print('Nível de leitura igual a Estudante de Faculdade')
    else:
        print('Nível de leitura igual a Graduado de Faculdade')

def leitura_computador(texto_analisado):
    total_palavras = 0
    total_frases = 0
    total_silabas = 0
    pontuação = 0

    palavras = texto_analisado.split()
    total_palavras = len(palavras)
    total_frases = contagem_frases(texto.texto)
    total_silabas = contagem_silabas(palavras)

    print(f'{total_palavras} palavras, {total_frases} frases, {total_silabas} sílabas')

    #Fórmula da Legibilidade de Flesch
    pontuação = 206.835 - 1.015 * (total_palavras / total_frases) - 84.6 * (total_silabas/total_palavras)



    resultado_final(pontuação)

leitura_computador(texto.texto)

