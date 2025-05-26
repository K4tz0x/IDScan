import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import signal
import sys
import time

visitados = set()
urls_com_id = set()
fila = []
salvar = True
dominio_base = ""
pasta_site = ""
nome_arquivo = ""

def exibir_banner():
    print(r"""
  _____ _____   _____                 
 |_   _|  __ \ / ____|                
   | | | |  | | (___   ___ __ _ _ __  
   | | | |  | |\___ \ / __/ _` | '_ \ 
  _| |_| |__| |____) | (_| (_| | | | |
 |_____|_____/|_____/ \___\__,_|_| |_|
                                      
      Ferramenta de Varredura ID/PHP
        Desenvolvida por K4tz0x - 2025
    """)

def salvar_resultados():
    if not nome_arquivo:
        return
    os.makedirs(pasta_site, exist_ok=True)
    caminho_txt = os.path.join(pasta_site, nome_arquivo)
    with open(caminho_txt, 'w', encoding='utf-8') as f:
        f.write("# Ferramenta desenvolvida por K4tz0x - 2025\n")
        f.write("# Resultados da varredura:\n\n")
        for link in sorted(urls_com_id):
            f.write(link + '\n')
    print(f"\n[✔] Varredura finalizada.")
    print(f"[+] Total de URLs com 'id=' ou 'php?id=' encontradas: {len(urls_com_id)}")
    print(f"[+] Resultados salvos em: {caminho_txt}")

def interromper_sinal(sig, frame):
    global salvar
    salvar = False
    print("\n[!] Interrompido por usuário. Salvando resultados...")
    salvar_resultados()
    sys.exit(0)

def encontrar_urls_com_id(base_url, max_urls=500, profundidade_max=5):
    global fila, dominio_base, pasta_site, nome_arquivo
    fila = [(base_url, 0)]
    dominio_base = urlparse(base_url).netloc
    pasta_site = os.path.join("resultados", dominio_base)
    nome_arquivo = "links_id.txt"

    while fila and len(visitados) < max_urls and salvar:
        url, profundidade = fila.pop(0)
        if url in visitados:
            continue
        if profundidade > profundidade_max:
            continue
        try:
            res = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code != 200:
                continue
        except requests.RequestException:
            continue

        visitados.add(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        for tag in soup.find_all('a', href=True):
            href = urljoin(url, tag['href'])
            parsed = urlparse(href)
            if dominio_base not in parsed.netloc:
                continue
            if href not in visitados and href not in fila:
                fila.append((href, profundidade + 1))
            if ('id=' in href or 'php?id=' in href) and href not in urls_com_id:
                urls_com_id.add(href)

        time.sleep(1)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, interromper_sinal)
    exibir_banner()
    alvo = input("Digite a URL inicial (ex: https://exemplo.com): ").strip()
    print(f"\n[*] Varredura em andamento, aguarde... (Ctrl+C para encerrar e salvar resultados)\n")
    try:
        encontrar_urls_com_id(alvo)
    finally:
        salvar_resultados()