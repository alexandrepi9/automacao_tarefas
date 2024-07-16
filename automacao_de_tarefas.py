import pyautogui
import time

# Passo 1 - Entrar no sistema
# Abrindo o navegador

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("edge")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Fazer Login

pyautogui.click(x=774, y=362)

pyautogui.hotkey("ctrl","a")

pyautogui.write("pintoalexandre90@hotmail.com")

pyautogui.press("tab")

pyautogui.write("senha123")

pyautogui.click(x=949, y=503)

time.sleep(3)

# Passo 3 - Importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4 - Cadastrar o produto

# para cada linha da minha tabela:
for linha in tabela.index:
    # codigo
    pyautogui.click(x=837, y=245)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(str(codigo))

    # marca
    marca  = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    
    # preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)
    
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    
    # observacao
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
        
    # enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir para todos os produtos

