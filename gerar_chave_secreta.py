import secrets
import string

def gerar_chave_secreta(tamanho=32):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    chave = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return chave

# Exemplo de uso
chave_secreta = gerar_chave_secreta()
print("Chave secreta segura gerada:", chave_secreta)
