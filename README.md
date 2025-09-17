# Idleon stromová minihra - Automatizovaný program pro hru
Automatický program v Pythonu, který hraje hru za nás. Snímá obrazovku a automaticky stiskne mezerník (tlačítko myši), když se šipka dostane do žlutého boxu.

---

## Denník vývoje

### **17. září 2025** (David)
* **Nápady na další postup:**
    * Rozdělení projektu do souborů a přejmenování hello.py na main.py (což je standardní název v Pythonu)
        * main
```py
import time
import pyautogui
from screenshot_utils import analyze_screenshot, find_segment, is_continuous
from control_utils import press_random_mouse
from config import SCREENSHOT_AREA, TARGET_COLORS, Y_COORDS, MAX_SPACES

def main():
    time.sleep(10)
    spaces_pressed = 0
    while spaces_pressed < MAX_SPACES:
        screenshot = pyautogui.screenshot(region=SCREENSHOT_AREA)
        should_press = analyze_screenshot(screenshot)
        
        if should_press:
            press_random_mouse()
            print("Stisknuto.")
            spaces_pressed += 1
            
        # Tady by byla logika pro algoritmus 3b, pokud ho budete chtít použít.

    print("Program dokončen.")

if __name__ == "__main__":
    main()
```

### **16. září 2025** (Vojta + David)
* **Co se stalo:** Dnešní práce se soustředila na soubor `hallo.py`.

### **15. září 2025** (David + Vojta)
* **Plán na 16. září:** Implementace nápadů a úprava kódu. Nový kód se bude vyvíjet v nové složce.
* **Vojtův plán (úvodní idea):**
    1.  Použít Python.
    2.  Nějaké IDE (editor) pro Python.
    3.  Vytvořit "Hello World".
* **Davidův plán (detaily, o kterých je řeč):**
    1.  **Bod 1 - Získání screenshotu:**
        * Zajímá nás, jak určit, který monitor snímat při dvou monitorech. Možná jen ten s myší.
        * Problém s přepnutím okna: Řešení je použít `sleep()` po spuštění, aby bylo dost času na přepnutí.
        * Definice funkcí: `udelej_screenshot()`, `sleep()`, `mezera()`.
    2.  **Bod 2 - Pomocné funkce:**
        * Identifikace potřebných bodů (x,y) na screenshotu.
        * Funkce: `najdi_zluty_box(screenshot)` a `najdi_x_sipky(screenshot)`.
        * Funkce pro kontrolu: `x_sipky_v_boxu(x_zluty_bod_1, x_zluty_bod_2, x_sipky)` -> tato funkce vrátí `True/False` pro stisk mezerníku.
    3.  **Bod 3 - Algoritmus (verze 3a a 3b):**
        * **Algoritmus 3a (základní):** Zpracovává screenshoty maximální rychlostí, dokud se nenastiskne mezerník 15x.
        * **Algoritmus 3b (pokročilejší):** Počítá s pohybem šipky mezi dvěma screenshoty pro přesnější stisk.
    * **Výzva:** Zjistit, jak se ti tento plán zdá.

### **14. září 2025** (Vojta)
* **Původní cíl:**
    * Snímat obrazovku 10x za sekundu.
    * Ze screenshotu získat pozice žlutého boxu a "lístku" (šipky).
    * Pokud jsou nad sebou, stisknout mezerník.
    * Opakovat 15x.
    * Bonus: smazat screenshoty.
* **Počáteční kód v souboru `hallo.py`:** Vojta přidal již existující kód, který obsahuje základní funkce pro analýzu snímků a simulaci stisku.

## Zajímavé kousky kódu, které jsme zatím nepoužili

