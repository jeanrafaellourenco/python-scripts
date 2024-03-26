from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Configurando o serviço do GeckoDriver
s = Service(GeckoDriverManager().install(), log_output="geckodriver.log")

# Criando uma instância do driver do Firefox
driver = webdriver.Firefox(service=s)

# Maximizando a janela do navegador
driver.maximize_window()

# Abrindo uma página da web
driver.get("https://www.google.com")

# Imprimindo o título da página
print("Título da página:", driver.title)

# Fechando o navegador
driver.quit()
