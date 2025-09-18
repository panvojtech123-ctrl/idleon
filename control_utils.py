def press_random_mouse(min_time=0.04, max_time=0.05):
    """
    Simuluje lidský klik levým tlačítkem myši s náhodnou délkou držení.
    """
    hold_time = random.uniform(min_time, max_time)
    pyautogui.mouseDown(button='left')  # stisk levého tlačítka
    time.sleep(hold_time)
    pyautogui.mouseUp(button='left')    # uvolnění