import pyautogui # automatiza o mouse, teclado e tela do computador
import time
import pandas  # ferramenta para trabalhar com base de dados de diferentes formatos

# pyautogui.click - click com o mouse
# pyautogui.write - escrever um texto 
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - Combinação de teclas (Ctrl C)
# pyautogui.scroll - rolagem de tela

pyautogui.PAUSE = 0.9

# Passo 1 - entrar no sistema 
# Abrir o navegador
pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Fazer login

pyautogui.click(x=1987, y=413)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=2154, y=568) # Botão de logar

# Importar base de dados 

tabela = pandas.read_csv("Projetos PY/Automação/produtos.csv")

print(tabela)


for linha in tabela.index: # Index = linha 

    # Cadastrar Produtos
    # Código

    pyautogui.click(x=1967, y=286)
    codigo = str(tabela.loc[linha, codigo]) # localiza uma informação na tabela
    pyautogui.write(codigo)

    # marca
    marca = str(tabela.loc[linha, marca])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # tipo
    tipo = str(tabela.loc[linha, tipo])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # categoria 
    categoria = str(tabela.loc[linha, categoria])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preço unitário
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    # Custo
    custo = str(tabela.loc[linha, custo])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # Obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])    
    if obs != "nan": # != diferente 
        pyautogui.write("obs")
        # nan = not a number (vazio)
        # forma de tratar uma condição

    # Botão enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(4000)