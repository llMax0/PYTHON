#importar bibliotecas

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #permite utilizar funcionalidades do teclado

#acessar o whatsapp web

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)#tempo para escanear o QR code com o celular para acessar o whatsapp

#definir contato/grupo

contatos = ['Dicas de estudos']
mensagem = 'TESTE'

#buscar contatos/ grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')#barra de texto[0]
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contatos)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')#barra de texto[1]
    campo_mensagem[1].click() #indexado de um para que o python identifique na lista das posições das barras de textp
    time.sleep(2)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    


