import random
import string
# Em serviços como Gmail e Outlook, adicionar um sinal de mais (+) composto por alguma coisa após seu email, faz com que um alias para seu email seja criado.
# Os emails enviados para este alias devem chegar normalmente em sua caixa de entrada. Ideal pra cadastros temporários ou evitar SPAM. 
# Dica: Em alguns sites, o sinal de + não é aceito no cadastro. Quando aceito, não passa no login. Pra resolver isso, encode o email com %2B, ex: seu_email%2Bxyz@outlook.com

# Definindo email (antes do @)
email = "seu_email"

# Definindo provedor (depois do @)
provedor = "outlook.com"

# Defina os caracteres especiais desejados
special_characters = "!@#$%^&*()_+"

print("************** GERADOR DE LOGIN E SENHAS **************")

# Gere uma senha forte de 12 caracteres com os caracteres especiais
def generate_password(length):
    characters = string.ascii_letters + string.digits + special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print('Email: ' + f'{email}+' + ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) + f'@{provedor}')
print('Senha: ' + generate_password(12))
print("*******************************************************")
