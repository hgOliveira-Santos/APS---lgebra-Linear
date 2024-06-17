# Atividade da disciplina de Álgebra Linear

**Curso:** Ciência da Computação  
**Instituição:** Centro Universitário UniCarioca  
**Professor:** Manuel Martins

# Criptografia e Descriptografia de Mensagens

Este é um programa simples em Python que permite criptografar e descriptografar uma mensagem utilizando uma matriz de criptografia específica.

## Funcionalidades

- **Criptografia:**
  - O usuário insere uma palavra de exatamente 6 letras (incluindo espaços se necessário).
  - A palavra é convertida em uma matriz 3x2 usando uma tabela de conversão de letras para números.
  - A matriz é então multiplicada por uma matriz de criptografia predefinida para obter a mensagem criptografada.
  - A matriz criptografada e a palavra original são exibidas.

- **Descriptografia:**
  - Utiliza a matriz inversa da matriz de criptografia para descriptografar a mensagem criptografada.
  - A matriz descriptografada é convertida de volta em texto usando uma tabela de desconversão.
