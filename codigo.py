# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5

# Abrir o navegador (chrome)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2: Fazer login
# Selecionar o campo de email

pyautogui.click(x=694, y=366)

# Escrever o seu email

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("enter")
time.sleep(2)

# Passo 3: Importar a base de produtos pra cadastrar

import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto

for linha in tabela.index:

    # Clicar no campo de código

    pyautogui.click(x=687, y=247)

    codigo = tabela.loc[linha, "codigo"]

    # Preencher os campos

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # Apertar para enviar

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

    # Passo 5: Repetir o processo de cadastro até o fim
