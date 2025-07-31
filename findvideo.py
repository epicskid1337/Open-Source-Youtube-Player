import undetected_chromedriver as webdriver
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import video
import ctypes

def youtube():
    driver = webdriver.Chrome()
    driver.get("https://youtube.com")
    wait = WebDriverWait(driver, timeout=10000)
    wait.until(EC.url_contains("watch"))
    if EC.url_contains("list"):
        ctypes.windll.user32.MessageBoxW(0, "hi you opened a playlist sorry thats not supported yet ", "error during finding song / video", 0x40)
    video.download(driver.current_url)
    video.play()