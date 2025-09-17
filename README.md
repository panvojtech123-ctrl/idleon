# Idleon stromová minihra - Automatizovaný program pro hru
Automatický program v Pythonu, který hraje hru za nás. Snímá obrazovku a automaticky stiskne mezerník (tlačítko myši), když se šipka dostane do žlutého boxu.

---

## Denník vývoje

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
