from selenium import webdriver
import pyaudio


driver = webdriver.Chrome()

driver.get("http://selenium.dev")


while True:
    command = input("Digite 'sair' para fechar o navegador: ")
    if command.lower() == "sair":
        break
    
driver.quit()

