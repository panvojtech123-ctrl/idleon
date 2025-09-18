import mss
from PIL import Image

from config import (
    ZACATEK_OBLASTI_BOXU,
    KONEC_OBLASTI_BOXU,
    Y_ZLUTEHO_BOXU,
    Y_LISTECKU,
    RGB_ZLUTEHO_BOXU,
    RGB_LISTECKU,
)
   
def najdi_zluty():
    return najdi(Y_ZLUTEHO_BOXU, RGB_ZLUTEHO_BOXU, '#')

def najdi_listecek():
    return najdi(Y_LISTECKU, RGB_LISTECKU, '*')[0]

def najdi(y, rgb, symbol):
    """
    Najde souvislý segment v horizontální linii na souřadnici y.
    Udělá screenshot jen 1 pixel vysokého řádku a vrátí start a end segmentu.
    """
    width = KONEC_OBLASTI_BOXU - ZACATEK_OBLASTI_BOXU + 1
    height = 1
    left = ZACATEK_OBLASTI_BOXU
    top = y

    # Udělej screenshot jen daného řádku
    monitor = {"top": top, "left": left, "width": width, "height": height}
    with mss.mss() as sct:
        img = sct.grab(monitor)
        screenshot = Image.frombytes("RGB", img.size, img.rgb)

    # Převod pixelů na řetězec symbolů
    line = "".join(
        symbol if screenshot.getpixel((x, 0))[:3] == rgb else "-"
        for x in range(width)
    )

    # Vyhlazení jednopixelových chyb
    line = smooth_line(line, symbol)

    print(line)  # volitelně, pro debug

    # Najdi segment
    start, end = find_segment(line, symbol)
    if start is None:
        raise ValueError(f"Nenalezen zacatek segmentu {symbol} na y={y}")
    if not is_continuous(line, symbol, start, end):
        raise ValueError(f"Segment {symbol} na y={y} neni souvisly")

    # Přepočítej na skutečné souřadnice obrazovky
    return start + ZACATEK_OBLASTI_BOXU, end + ZACATEK_OBLASTI_BOXU


# --- Pomocné funkce ---
def smooth_line(line, symbol):
    """
    Vyhladí řetězec: odstraní jednopixelové chyby.
    '-#-' -> '---'
    '#-#' -> '###'
    """
    lst = list(line)
    for i in range(1, len(lst) - 1):
        if lst[i] != symbol and lst[i-1] != symbol and lst[i+1] != symbol:
            continue  # -#- v negativní oblasti -> už je -
        if lst[i] != symbol:
            # '-#-' -> '---'
            if lst[i-1] != symbol and lst[i+1] != symbol:
                lst[i] = '-'
        else:
            # '#-#' -> '###'
            if lst[i-1] == symbol and lst[i+1] == symbol:
                lst[i] = symbol
    return "".join(lst)


def find_segment(line, symbol):
    """
    Vrátí (start, end) prvního souvislého segmentu složeného ze symbolů.
    """
    start = None
    for i, ch in enumerate(line):
        if ch == symbol and start is None:
            start = i
        elif ch != symbol and start is not None:
            return start, i - 1
    if start is not None:
        return start, len(line) - 1
    return None, None


def is_continuous(line, symbol, start, end):
    """
    Ověří, že segment od start do end je souvislý (bez mezer).
    """
    segment = line[start:end + 1]
    return all(ch == symbol for ch in segment)


# --- Příklad použití ---
if __name__ == "__main__":
    from config import RGB_ZLUTEHO_BOXU, Y_ZLUTEHO_BOXU

    zluty_start, zluty_end = najdi(
        y=Y_ZLUTEHO_BOXU,
        rgb=RGB_ZLUTEHO_BOXU,
        symbol="X"
    )
    print("Žlutý segment:", zluty_start, zluty_end)
