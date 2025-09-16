from PIL import Image

# otevření obrázku
img = Image.open("screenshot.png")

# souřadnice rozsahu x
x_start, x_end = 1130, 1975

# --- první pole ---
y1 = 350
target_color1 = (252, 255, 122)
result1 = []

for x in range(x_start, x_end + 1):
    pixel = img.getpixel((x, y1))
    if pixel[:3] == target_color1:
        result1.append("#")
    else:
        result1.append("-")

# --- druhé pole ---
y2 = 298
target_color2 = (189, 236, 63)
result2 = []

for x in range(x_start, x_end + 1):
    pixel = img.getpixel((x, y2))
    if pixel[:3] == target_color2:
        result2.append("*")
    else:
        result2.append("_")

# výpis obou výsledků
print("".join(result1))
print()  # prázdný řádek
print("".join(result2))
