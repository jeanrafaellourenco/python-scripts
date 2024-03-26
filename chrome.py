from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurando o serviço do ChromeDriver
s = Service(ChromeDriverManager().install())

# Criando uma instância do driver do Chrome
driver = webdriver.Chrome(service=s)

# Maximizando a janela do navegador
driver.maximize_window()

# Abrindo uma página da web
driver.get("https://www.google.com")

# Imprimindo o título da página
print("Título da página:", driver.title)

# Fechando o navegador
driver.quit()
