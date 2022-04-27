###############################################
#           Autor: Miguel A. Kotowey          #
# Feito p/ pesquisar loja no ifood via chrome #
###############################################

import pyautogui
import time

# MOVE CURSOR ATÉ A BARRA DE PESQUISA x = 901, y = 135
pyautogui.moveTo(901,135)

# CLICK NA BARRA DE PESQUISA
pyautogui.click()
time.sleep(1)

# APAGA ALGO SE EXISTIR, DIGITA O TERMO DE PESQUISA E TECLA ENTER
pyautogui.press('backspace', presses=10)
pyautogui.press('delete', presses=10)
time.sleep(1)
pyautogui.write('hot legs', interval=0.50)
pyautogui.press('enter')
time.sleep(1)

# MOVE ATÉ O PRIMEIRO SLOT DE RESULTADO E CLICA
pyautogui.moveTo(509,338)
pyautogui.click()