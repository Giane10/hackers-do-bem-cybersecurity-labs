def caesar_cipher(text, shift):
    """
    Função para cifrar ou decifrar um texto usando a Cifra de César.
    Garante a confidencialidade da mensagem através da substituição.
    """
    result = ""
    for char in text:
        # Verifica se o caractere é uma letra do alfabeto
        if char.isalpha():
            shift_amount = shift % 26  # Garante que o deslocamento esteja dentro do alfabeto
            
            # Tratamento para letras minúsculas
            if char.islower():
                shifted = ord(char) + shift_amount
                if shifted > ord("z"):
                    shifted -= 26
                elif shifted < ord("a"):
                    shifted += 26
                result += chr(shifted)
            
            # Tratamento para letras maiúsculas
            else:
                shifted = ord(char) + shift_amount
                if shifted > ord("Z"):
                    shifted -= 26
                elif shifted < ord("A"):
                    shifted += 26
                result += chr(shifted)
        else:
            # Mantém caracteres que não são letras (espaços, pontuação) inalterados
            result += char
    return result

def main():
    print("--- Ferramenta de Criptografia: Cifra de César ---")
    text = input("Digite o texto a ser cifrado/descifrado: ")
    shift = int(input("Digite a quantidade de posições (Ex: 10 ou -10): "))
    
    output = caesar_cipher(text, shift)
    print(f"\nResultado: {output}")

if __name__ == "__main__":
    main()