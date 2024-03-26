import hmac
import hashlib

def calcular_hmac(chave_secreta, mensagem):
    # Especificando a função hash (SHA-256 neste exemplo)
    hash_func = hashlib.sha256
    
    # Convertendo a chave para bytes (se não estiver em bytes)
    chave_bytes = bytes(chave_secreta, 'utf-8')
    
    # Criando o objeto HMAC
    h = hmac.new(chave_bytes, mensagem.encode('utf-8'), hash_func)
    
    # Obtendo o código HMAC
    codigo_hmac = h.hexdigest()
    
    return codigo_hmac

def decodificar_hmac(chave_secreta, mensagem, codigo_hmac):
    # Calcula o HMAC para a mensagem e a chave fornecida
    novo_codigo_hmac = calcular_hmac(chave_secreta, mensagem)
    
    # Compara o HMAC calculado com o HMAC fornecido
    if novo_codigo_hmac == codigo_hmac:
        return True
    else:
        return False

# Exemplo de uso
chave_secreta = "jB\8CqPJ&YtvCbob7FM_FSLqtp7Jb@=>"
mensagem = "Esta é uma mensagem de exemplo."
codigo_hmac = calcular_hmac(chave_secreta, mensagem)

print(f"Mensagem: {mensagem}")
print(f"Código HMAC: {codigo_hmac}")

# Testando a função de decodificar
if decodificar_hmac(chave_secreta, mensagem, codigo_hmac):
    print("O código HMAC é válido.")
else:
    print("O código HMAC é inválido.")

