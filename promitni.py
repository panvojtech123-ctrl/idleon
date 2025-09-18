import tkinter as tk
from PIL import Image, ImageTk

# Otevři obrázek
img = Image.open("screenshot.png")

# Vytvoř hlavní okno fullscreen
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')

# Velikost obrazovky
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()

# Přepočet velikosti obrázku s zachováním poměru stran
ratio = min(sw / img.width, sh / img.height)
img_resized = img.resize(
    (int(img.width * ratio), int(img.height * ratio)), 
    Image.Resampling.LANCZOS
)

# Tkinter Image
tk_img = ImageTk.PhotoImage(img_resized)

# Canvas a obrázek vycentrovaný
canvas = tk.Canvas(root, width=sw, height=sh, highlightthickness=0)
canvas.pack()
canvas.create_image((sw - img_resized.width)//2, (sh - img_resized.height)//2, anchor="nw", image=tk_img)

# Ukončení po Esc nebo kliknutí myší
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Button-1>", lambda e: root.destroy())

# Spusť
root.mainloop()

