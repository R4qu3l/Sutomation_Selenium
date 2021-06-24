import time
from selenium import webdriver

url = 'https://www.coronatracker.com/pt-br/'
drive = webdriver.Chrome()
drive.get(url)

confirmados = drive.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')

curados = drive.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')

mortes = drive.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')

time.sleep(3)

x = confirmados.text
y = int(x.replace('.', ''))

c = curados.text
b = int(c.replace('.', ''))

m = mortes.text
n = int(m.replace('.', ''))

recuperados = (b / y) * 100
perdas = (n / y) * 100

print("=-" * 3, "Casos recuperados e mortes - COVID", "-=" * 3)

print("{:.2f} % de casos curados e {:.2f} % de mortes".format(recuperados, perdas))
