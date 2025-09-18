import pyautogui

# Udělej screenshot celé obrazovky
screenshot = pyautogui.screenshot()

# Ulož do souboru
screenshot.save("screenshot.png")

print("Screenshot uložen jako screenshot.png")