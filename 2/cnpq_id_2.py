#WebCrawler para salvar os ids dos pesquisadores do Lattes: https://buscatextual.cnpq.br/buscatextual/busca.do#
#Desenvolvido por Fernando Almeida
#Data: 5/01/2023
#new token github: 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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd
import csv
import os

def OptionsDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service() 
    chrome_Wedriver = webdriver.Chrome(service=service, options=options)
    return chrome_Wedriver

class Info:
    def __init__(self,driver):
        self.url_base = 'https://buscatextual.cnpq.br/buscatextual/busca.do;jsessionid=77E5F7274B287D45CD80802C37EDDFF7.buscatextual_0#'
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
    def dataPublish(self):
        self.driver.get(self.url_base)
        sleep(5)
        self.driver.find_element('id', 'filtro0').click()
        sleep(5)
        self.driver.find_element('id', 'checkbox2').click()
        sleep(3)
        self.driver.find_element('id', 'preencheCategoriaNivelBolsa').click()
        sleep(5)
        self.driver.find_element('id', 'botaoBuscaFiltros').click()
        sleep(10)

        ids = []
    
        for p in range(12, 13):
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click()
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 60 - 1630
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 60 - 1630
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 1800
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 1900
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 1900
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(p + 1) +']').click() # page: 2100
            sleep(3)
            
            for i in range(2, 12):
                #p = 6
                self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[2]/a['+ str(i) +']').click()
                ####Ver isso aqui##### ir incrementando +1 para mudar de pagina

                # Armazena o identificador da janela original
                janela_original = self.driver.current_window_handle

                for j in range(1, 11):
                    #elemento_pesq = self.driver.find_elements('css selector', 'body > form > div > div.content-wrapper > div > div > div > div.layout-cell.layout-cell-12 > div > div.resultado > ol > li:nth-child('+str(p)+') > b > a')
                    #for ele in elementos_pesq:
                    sleep(2)        
                    self.driver.find_element('xpath', '/html/body/form/div/div[4]/div/div/div/div[3]/div/div[3]/ol/li['+str(j)+']/b/a').click()
                    print("Abriu o PopUp do "+str(j)+"° pesquisador da página "+str(i))
                    sleep(3)
                    #self.driver.execute_script(elemento_pesq.get_attribute('href'))
                    #sleep(10)
                    #self.driver.find_element('id', 'idbtnabrircurriculo').click()
                    #sleep(10)
                    abrir_curr = self.driver.find_element('id', 'idbtnabrircurriculo')
                    #for elemento in elementos:
                    #Executa a chamada de função JavaScript
                    self.driver.execute_script(abrir_curr.get_attribute('href'))
                    # Obtém uma lista de todas as guias abertas
                    sleep(2)
                    janelas = self.driver.window_handles

                    # Acessa a nova guia
                    self.driver.switch_to.window(janelas[-1])
                    sleep(5)

                    # Define um tempo limite de 5 segundos
                    #timeout = 5
                    try:
                        # Aguarda o carregamento da página até o tempo limite
                        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(("xpath", '/html/body/div[1]/div[3]/div/div/div/div[1]/ul/li[2]/span[2]')))
                        
                        text = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/div/div/div/div[1]/ul/li[2]/span[2]').text
                        print(text)
                        ids.append(text)

                        # Fecha a nova guia
                        self.driver.close()
                    
                        # Volta para a janela original
                        self.driver.switch_to.window(janela_original)
                        sleep(1)
                        self.driver.find_element('xpath', '/html/body/form/div/div[1]/div/div/div/div[1]/a').click()
                        #sleep(10)
                    except TimeoutException:
                        # Tempo limite excedido, fecha a guia
                        self.driver.close()

                        # Volta para a janela original
                        self.driver.switch_to.window(janela_original)
                        sleep(1)
                        self.driver.find_element('xpath', '/html/body/form/div/div[1]/div/div/div/div[1]/a').click()
                        #sleep(10)

        df = pd.DataFrame(ids)

        # Escrever o dataframe em um arquivo CSV
        df.to_csv('nova_coleta/ids2_page_30.csv') # 
        #self.getInfosPubl
    '''def getInfosPublish(self):
        Bs = bs(self.driver.page_source, 'html.parser')
        #try:
        #for i in range(0, 201):
        sleep(5)
        text = self.driver.find_element("xpath", '/html/body/div[1]/div[3]/div/div/div/div[1]/ul/li[2]/span[2]').text
        print(text)'''
        #self.info_publish.writerow([name])      

#* Configuração do webdriver
Web_Driver = OptionsDriver()
execute_Scrip = Info(Web_Driver)
execute_Scrip.dataPublish()