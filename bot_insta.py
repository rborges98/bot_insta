from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from tela import usuario, senha, lista
    

#credenciais importadas da tela
insta_user = usuario
insta_pass = senha
#lista de contas a serem seguidas vindo do banco de dados
lista_contas = lista


#iniciando o browser
browser = webdriver.Chrome(ChromeDriverManager().install())
#abrindo o site
browser.get('https://www.instagram.com/')
browser.implicitly_wait(20)


#fazendo o login
browser.find_element_by_name("username").send_keys(insta_user)
browser.find_element_by_name("password").send_keys(insta_pass)
browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click();


for usuario in lista_contas:
    #pesquisando o usuario
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(usuario);
    sleep(3)
    browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]").click();
    sleep(4)
    #unfollow 
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button").click();
    sleep(3)
    #confirmaçao do unfollow
    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click();
    sleep(2)
    #follow
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button").click();
    sleep(2)

browser.quit()



