# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
# %%

email = ''# Coloque seu e-mail aqui
password = '' #Coloque a senha do seu e-mail aqui

recipient_name = '' #Coloque o e-mail do destinatario

subject_matter = 'Teste de Automatização de E-mail'
write_content= '''Mensagem teste de E-mail enviada!\n Automatização funcionando!'''
# %%
sleep(2)
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://mail.google.com/mail/u/0/#inbox')

#Logar no seu e-mail
login_email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
sleep(2)
login_email.click()
sleep(2)
login_email.send_keys(email)
enter_email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
enter_email.click()
sleep(2)

#Preenche sua senha
login_senha = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
sleep(2)
login_senha.click()
sleep(2)
login_senha.send_keys(password)
enter_senha = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span')
enter_senha.click()
sleep(3)

#Não simplificar login
# not_simplify_login = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div/div/button/span')
# sleep(2)
# not_simplify_login.click()

#Permanecer com a conta
# sleep(2)
# remain_on_accont = driver.find_element(By.XPATH, '/html/body/chrome-signin-app//div/div[2]/div/div[4]/cr-button[1]/div')
# remain_on_accont.click()

write_email = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div')
write_email.click()

sleep(1)
to = driver.find_element(By.XPATH, '/html/body/div[28]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/form/div[2]')
to.click()
sleep(2)
to.send_keys(recipient_name)

sleep(2)
affairs = driver.find_element(By.XPATH, '/html/body/div[28]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/input')
affairs.click()
sleep(2)
affairs.send_keys(subject_matter)

write_email_content = driver.find_element(By.XPATH, '/html/body/div[28]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[2]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div/div[1]')
write_email_content.click()
sleep(2)
write_email_content.send_keys(write_content)

sending_email = driver.find_element(By.XPATH, '/html/body/div[27]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]')
sending_email.click()