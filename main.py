import cv2
import numpy as np
import pyautogui

def ekrangoruntusu():
    from PIL import ImageGrab
    cv2.namedWindow("Ekran",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Ekran",480,270) #Açılan Pencerenin Boyutu
    Ekran =  np.array(ImageGrab.grab(bbox=(0,0,885,548))) #Ekranda Alanınacak Alan 
    frame=cv2.cvtColor(Ekran,cv2.COLOR_BGR2RGB)
    cv2.imshow("Ekran",frame)
    return frame
while True:
    ekrangoruntusu()
    if cv2.waitKey(1) & 0xFF == ord("q"): # q tuşuna basılınca kapansın
        cv2.destroyAllWindows()
        print("Çıkıldı..")
        break
