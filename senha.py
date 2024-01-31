import random # Gera Aletoriamente 
import string # Gerar numeros,especial, maisculo, minusculo

def gerar_senha(comprimento, incluir_numeros=True, incluir_maiusculo=True, incluir_minusculo=True, incluir_especial=True):
    caracteres = string.ascii_letters  # Mostra Letras maisculas e minusculas
    if incluir_numeros:
        caracteres += string.digits  # Adiciona Numeros

    if incluir_maiusculo:
        caracteres += string.ascii_uppercase  # Adiciona Caracteres Maiusculas

    if incluir_minusculo:
        caracteres += string.ascii_lowercase  # Adiciona Caracteres Minusculas

    if incluir_especial:
        caracteres += "!@#$%^&*()--++"  # Adiciona algum simbolo especial
        
        # Gera a senha Aletoriamente
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha
# Perguntas para poder gerar a senha
comprimento_senha = int(input("Digite o comprimento desejado da senha: "))
incluir_numeros = input("Gostaria de incluir numeros: (S/N)").lower() == 's'
incluir_minusculo = input("Gostaria de incluir letras minusculas: (S/N)").lower() == 's'
incluir_maiusculo = input("Gostaria de letras maisculas: (S/N)").lower() == 's'
incluir_especial = input("Gostaria de incluir caracteres especiais: (S/N)").lower() == "s"

# Quando colocar Negativo, não entra
if comprimento_senha <= 0:
    print("Senha Necessita de Comprimento Positivo")
    exit()

senha_foi_gerada = gerar_senha(comprimento_senha, incluir_numeros, incluir_maiusculo, incluir_minusculo, incluir_especial)
print("Senha Gerada:", senha_foi_gerada)

   