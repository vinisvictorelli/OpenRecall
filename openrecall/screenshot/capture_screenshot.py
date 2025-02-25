import threading
import time
import cv2
import numpy as np
import pyscreenshot as ImageGrab
from Xlib import display

import os
import datetime

# Tirar captura de tela
def take_screenshot():
    # Captura de tela do monitor principal
    screenshot = ImageGrab.grab()
    # Converte a captura de tela para um array NumPy (compatível com OpenCV)
    screenshot_np = np.array(screenshot)

    # Converte RGB para o formato BGR (OpenCV usa o formato BGR)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    return screenshot_np

def save_screenshot(screenshot):
    # Cria um nome de arquivo com data e hora
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
    filepath = f"openrecall/data/capture/{filename}"
    # Salva a imagem
    cv2.imwrite(filepath, screenshot)
    print(f"Screenshot saved as {filename}")
    print()

def compare_screenshots(prev_screenshot, curr_screenshot):
    # Converte para escala de cinza para comparação
    prev_gray = cv2.cvtColor(prev_screenshot, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_screenshot, cv2.COLOR_BGR2GRAY)

    # Calcula a diferença absoluta entre as capturas de tela
    diff = cv2.absdiff(prev_gray, curr_gray)
    diff_percentage = (np.sum(diff > 50) / diff.size) * 100
    return diff_percentage

# Função principal
def capture_screenshot_comparison():
    prev_screenshot = take_screenshot()
    save_screenshot(prev_screenshot)
    while True:
        time.sleep(3)
        curr_screenshot = take_screenshot()
        diff = compare_screenshots(prev_screenshot, curr_screenshot)
        print(f'Porcentagem de diferença: {diff}%')
        if diff > 5:
            save_screenshot(curr_screenshot)
            # Atualiza a captura de tela atual
            prev_screenshot = curr_screenshot

# Nova função para capturar capturas de tela em um intervalo especificado
def capture_screenshots_interval(interval_seconds):
    while True:
        screenshot = take_screenshot()
        save_screenshot(screenshot)
        time.sleep(interval_seconds)

# Exemplo de uso da nova função
if __name__ == "__main__":
    capture_interval = 10  # Intervalo em segundos
    capture_screenshots_interval(capture_interval)
