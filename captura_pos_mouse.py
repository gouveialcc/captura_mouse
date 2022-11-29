import pyautogui
import time

#pega posicao do mouse
def position():
    global posicao
    print('POSICIONE O MOUSE NA TELA!')
    time.sleep(5)
    posicao = x, y = pyautogui.position()
    print ("Posicao atual do mouse:")
    print ("x = "+str(x)+" y = "+str(y))
    #retorna Truee se x & y estiverem dentro da tela
    print ("\nEsta dentro da tela?")
    resp = pyautogui.onScreen(posicao)
    print (str(resp))
    time.sleep(3)

def click():
    time.sleep(2)
    drag = pyautogui.dragTo(posicao, button='left')
    
def mouse():
    position()
    click()

if __name__ == '__main__':
    mouse()