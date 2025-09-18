import time
import pyautogui
from screenshot_utils import najdi_zluty, najdi_listecek
from control_utils import press_random_mouse

def mam_stisknout(zluty_start, zluty_konec, sipka_old, sipka_new):
    hodnota = sipka_new - sipka_old + sipka_new
    return zluty_start <= hodnota <= zluty_konec


def main():
    # Čekání na start
    cekej_na_start()

    # Inicializace
    should_press = False
    zluty_start, zluty_konec = najdi_zluty()
    sipka_new = najdi_listecek()

    # Hlavní smyčka
    while not should_press:
        sipka_old = sipka_new
        sipka_new = najdi_listecek()
        should_press = mam_stisknout(zluty_start, zluty_konec, sipka_old, sipka_new)
        if should_press:
            stiskni_neco()

    print("Program dokončen.")

# Funkce pro simulaci stisku
def stiskni_neco():
    #press_random_mouse()
    print("Stisknuto.")

# Funkce pro čekání na start
def cekej_na_start():
    time.sleep(5)
    print("Startujeme")

# Spuštění programu
if __name__ == "__main__":
    main()