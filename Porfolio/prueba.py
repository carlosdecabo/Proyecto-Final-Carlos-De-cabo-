import pyautogui
import webbrowser as web 
from time import sleep

web.open("https://web.whatsapp.com/send?phone=@numeroFormulario")
sleep(5)
for x in range(1):
    pyautogui.typewrite('Hola, Bienvenido Usuario @usuario ')
    pyautogui.press('enter')