# Ferramenta de Varredura ID/PHP

**Desenvolvida por K4tz0x - 2025**

Ferramenta em Python para varredura automatizada de links em sites que contenham parâmetros como `id=` ou `php?id=`, comuns em aplicações suscetíveis a falhas de segurança (ex: SQL Injection). Ideal para testes de segurança e auditoria web.

---

## Funcionalidades

- Rastreamento recursivo de links internos a partir de uma URL inicial
- Coleta de URLs contendo `id=` ou `php?id=`
- Limite de profundidade configurável para evitar varredura excessiva
- Salvamento automático dos resultados em arquivo `.txt`
- Suporte à interrupção via Ctrl+C com salvamento seguro dos dados

---

## Captura de Tela (Banner)


---

|_   |  __ \ / |
| | | |  | | (   ___ __ _ _ __
| | | |  | |_ \ / / ` | ' \ | || || |) | (| (| | | | | ||/|___/ __,|| ||

Ferramenta de Varredura ID/PHP
    Desenvolvida por K4tz0x - 2025

---

## Requisitos

- Python 3.x

### Instalação de dependências:

```bash
pip install -r requirements.txt

Ou instale manualmente:

pip install requests beautifulsoup4


---

Como Usar

1. Clone o repositório:



git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

2. Execute o script:



python3 varredura_id.py

3. Insira a URL inicial quando solicitado:



Digite a URL inicial (ex: https://exemplo.com):

4. Aguarde a varredura. Use Ctrl+C a qualquer momento para encerrar e salvar os resultados.




---

Saída

Os links encontrados com id= ou php?id= são salvos em:

/resultados/NOME_DO_SITE/links_id.txt


---

Licença

Este projeto é livre para uso educacional e de pesquisa. Não utilize para atividades ilegais.


---

Autor

K4tz0x
Contato: github.com/seu-usuario (substitua pelo seu link)

---
