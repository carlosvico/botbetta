from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import ast

class eita:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver.exe")
    

    def bora(self):
        print("Estou no bora")
        driver = self.driver
        frases = ["Mais um teste de frases", "Esta é a segundo frase"]
        driver.get("https://www.google.com.br")
        time.sleep(3)
        elemento = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").click()
        time.sleep(2)
        elementon = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
        print("Clicou no campo de pesquisa")
        self.digitando(random.choice(frases), elementon)
        print("Voltei para bora")  
        time.sleep(5)
        self.driver.quit()  
            
    @staticmethod
    def digitando(frase, local):
        print("Agora estou no metodo de digitação")
        for letra in frase:
            local.send_keys(letra)
            time.sleep(random.randint(1,6)/50)
            print("digitando: "+letra)





inicio = eita()
inicio.bora()


    