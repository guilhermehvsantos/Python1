from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html'
}

url = "https://www.kabum.com.br/produto/444038/monitor-gamer-lg-ultragear-27-full-hd-144hz-1ms-ips-hdmi-e-displayport-hdr-10-99-srgb-freesync-premium-vesa-27gn65r"
site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.text, 'html.parser')

# Atualize o seletor conforme necessário
prices = soup.find('h4')

if prices is not None:
    print(prices.text.split()[-1])
else:
    print("Não foi possível encontrar o elemento com a classe especificada.")
