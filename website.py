from selenium import webdriver
import pyaudio


def GoogleSite():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")


    while True:
        command = input("Digite 'sair' para fechar o navegador: ")
        if command.lower() == "sair":
            break
        
    driver.quit()


def FacebookSite():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")


    while True:
        command = input("Digite 'sair' para fechar o navegador: ")
        if command.lower() == "sair":
            break
        
    driver.quit()

