print("Hallo world2")
import winsound
from PIL import Image
import pygetwindow as gw
import pyautogui
import time

def find_segment(line, symbol):
    """Najde začátek a konec souvislého úseku se zadaným symbolem."""
    start = None
    end = None
    for i, c in enumerate(line):
        if c == symbol:
            if start is None:
                start = i
            end = i
    return start, end

def is_continuous(line, symbol, start, end):
    """Ověří, že mezi start a end jsou jen symboly."""
    segment = line[start:end+1]
    return all(c == symbol for c in segment)

def analyze_screenshot(screenshot: Image.Image) -> bool:
    """
    Analyzuje screenshot:
    - line1: '#' na y=350, barva (252,255,122)
    - line2: '*' na y=298, barva (189,236,63)
    
    Vrací:
        True  -> pokud jsou úseky souvislé a * je celý uvnitř #
        False -> pokud jsou souvislé, ale nepřekrývají se úplně
    Vyhodí výjimku, pokud úseky nejsou souvislé.
    """
    x_start, x_end = 1130, 1975

    # --- line1 ---
    y1 = 350
    target_color1 = (252, 255, 122)
    line1 = "".join(
        "#" if screenshot.getpixel((x, y1))[:3] == target_color1 else "-"
        for x in range(x_start, x_end + 1)
    )

    # --- line2 ---
    y2 = 298
    target_color2 = (189, 236, 63)
    line2 = "".join(
        "*" if screenshot.getpixel((x, y2))[:3] == target_color2 else "_"
        for x in range(x_start, x_end + 1)
    )

    print("".join(line1))
    print()  # prázdný řádek
    print("".join(line2))

    # --- najdi segmenty ---
    h_start, h_end = find_segment(line1, "#")
    s_start, s_end = find_segment(line2, "*")

    if h_start is None or s_start is None:
        raise ValueError("Chyba: žádný úsek # nebo * nebyl nalezen!")

    # --- kontrola souvislosti ---
    if not is_continuous(line1, "#", h_start, h_end):
        raise ValueError("Chyba: úsek # není souvislý!")
    if not is_continuous(line2, "*", s_start, s_end):
        raise ValueError("Chyba: úsek * není souvislý!")

    # --- kontrola úplného překrytí ---
    return s_start >= h_start and s_end <= h_end

# Udělá screenshot a uloží ho jako 'screenshot.png'

#screenshot = pyautogui.screenshot()
#screenshot.save('screenshot.png')
#print("Screenshot byl uložen jako screenshot.png")

#time.sleep(5)
#pyautogui.press('space')
# žlutá: 252, 255, 122
# zelená 189, 236, 63 
# řádek baru: 350
# možné hranice hledání baru: 1130-1975
# 298


screenshot = pyautogui.screenshot()
mam_zmacknout_mezeru = analyze_screenshot(screenshot)
