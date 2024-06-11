import numpy as np

# Tamanho padrão da palavra
TAMANHO_PALAVRA = 6

# Tabela de conversão de letras para números e vice-versa
TABELA_CONVERSÃO = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
    "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, " ": 0
}

# Tabela de desconversão (para retornar letras a partir de números)
TABELA_DESCONVERSÃO = {valor: chave for chave, valor in TABELA_CONVERSÃO.items()}

# Matriz de criptografia
matriz_de_criptografia = np.array([[1, 0, 1], [1, 1, 1], [0, 2, -1]])

# Função para converter um elemento de acordo com a tabela de conversão
def converter_matriz(elemento, tabela):
    if elemento in tabela:
        return tabela[elemento]
    else:
        return elemento

# Função para desconverter uma matriz usando a tabela de desconversão
def desconverter_matriz(matriz, tabela):
    idx = 0
    msg = ''
    while idx < 2:
        for linha in matriz:
            if linha[idx] in tabela:
                msg += tabela[linha[idx]]
        idx += 1
    return msg

# Função para verificar se a mensagem tem o tamanho correto e é composta apenas de letras
def verificar_mensagem(mensagem, tamanho):

    if(len(mensagem) > tamanho):
        print("A palavra só pode conter 6 caracteres! Tente novamente.")
        return False

    for letra in mensagem:
        if letra.isdigit():
            print("Você digitou um número! Tente novamente.")
            return False
        
    mensagem = mensagem.ljust(6, " ")

    return mensagem

# Loop principal do programa
while True:

    # Solicitar uma palavra ao usuário
    mensagem = input("Digite uma palavra com 6 letras: ").upper()

    # Verificar se a palavra está correta
    mensagem = verificar_mensagem(mensagem, TAMANHO_PALAVRA)

    if(mensagem):
        # Dividir a mensagem em duas partes para construir a matriz
        parte1 = mensagem[:3]
        parte2 = mensagem[3:]

        # Criar a matriz original
        matriz_original = np.array([[parte1[0], parte2[0]], [parte1[1], parte2[1]], [parte1[2], parte2[2]]])

        # Converter a matriz de acordo com a tabela de conversão
        matriz_convertida = [[converter_matriz(elemento, TABELA_CONVERSÃO) for elemento in linha] for linha in matriz_original]
        
        # Criptografar a mensagem
        matriz_criptografada = np.dot(matriz_de_criptografia, matriz_convertida) 

        # Exibir resultados
        print("\n**** PROGRAMA DE CRIPTOGRAFIA ****\n")
        print(f"A palavra original é: {mensagem}\n")
        print(f"A matriz codificada é: \n{matriz_convertida}\n")
        print(f"A matriz da mensagem criptografada é: \n{matriz_criptografada}\n")

    break

# Calcular a matriz inversa da matriz de criptografia
matriz_inversa = np.linalg.inv(matriz_de_criptografia)
matriz_inversa = matriz_inversa.astype(int)

# Descriptografar a mensagem
matriz_mensagem_original = np.dot(matriz_inversa, matriz_criptografada)
matriz_mensagem_original = matriz_mensagem_original.astype(int)

# Converter a matriz descriptografada em mensagem usando a tabela de desconversão
mensagem_original = desconverter_matriz(matriz_mensagem_original, TABELA_DESCONVERSÃO)

# Exibir a mensagem original
print("\n**** PROGRAMA DE DESCRIPTOGRAFIA ****\n")
print(f"Matriz da mensagem criptografada:\n{matriz_criptografada}\n")
print(f"Matriz descriptografada com a inversa:\n{matriz_mensagem_original}\n")
print(f"A mensagem original é: {mensagem_original}\n\n")



