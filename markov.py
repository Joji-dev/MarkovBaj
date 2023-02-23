
import praw
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import pyperclip
from PIL import Image
from io import BytesIO
import pyautogui
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="test script by u/TheSeahorseHS (:tf:)",
    username="",
    password=""
)

subreddit = reddit.subreddit("forsen")
print("Up and running!")

for comment in subreddit.stream.comments(skip_existing=True):
    normal_comment = comment.body.lower()
    if "![img](emote|t5_33td5|9666)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9666)", "Clueless")
    if "![img](emote|t5_33td5|9667)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9667)", "Okayeg")
    if "![img](emote|t5_33td5|9668)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9668)", "cmonBruh")
    if "![img](emote|t5_33td5|9669)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9669)", "Copesen")
    if "![img](emote|t5_33td5|9670)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9670)", "forsenLevel")
    if "![img](emote|t5_33td5|9671)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9671)", "BatChest")
    if "![img](emote|t5_33td5|9672)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9672)", "forsenCD")
    if "![img](emote|t5_33td5|9673)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9673)", "forsenDespair")
    if "![img](emote|t5_33td5|9674)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9674)", "forsenE")
    if "![img](emote|t5_33td5|9675)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9675)", ":tf:")
    if "![img](emote|t5_33td5|9676)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9676)", "FeelsOkayMan")
    if "![img](emote|t5_33td5|9677)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9677)", "gachiGASM")
    if "![img](emote|t5_33td5|9678)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9678)", "monkaOMEGA")
    if "![img](emote|t5_33td5|9679)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9679)", "Sadeg")
    if "![img](emote|t5_33td5|9680)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9680)", "pepeLaugh")
    if "![img](emote|t5_33td5|9681)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9681)", "LULE")
    if "![img](emote|t5_33td5|9682)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9682)", "OMEGALUL")
    if "![img](emote|t5_33td5|9684)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9684)", "PagMan")
    if "![img](emote|t5_33td5|9685)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|9685)", "forsenBased")
    if "![img](emote|t5_33td5|10257)" in normal_comment:
        normal_comment = normal_comment.replace("![img](emote|t5_33td5|10257)", "amongE")

    print(normal_comment)
    if "markov" in normal_comment:
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(executable_path=r'C:\python\geckodriver.exe', options=options, firefox_profile=profile)
        driver.get("https://markovbaj.app/")
        input = driver.find_element(By.CLASS_NAME, 'Styles-chatInput')
        input.send_keys(normal_comment)
        input.submit()

        time.sleep(5)

        png = driver.get_screenshot_as_png()
        element  = driver.find_element(By.CLASS_NAME, 'Styles-chatContainer')
        location = element.location
        size = element.size

        im = Image.open(BytesIO(png))

        left = location['x']
        left = left + 100
        top = location['y']
        top = top + 100
        right = location['x'] + size['width']
        right = right + 150
        bottom = location['y'] + size['height']
        bottom = bottom + 100

        im = im.crop((left, top, right, bottom))
        im.save('screenshot.png')
        
        time.sleep(2)
        link = 'https://reddit.com' + comment.permalink
        driver.get(link)
        login=driver.find_element(By.LINK_TEXT, 'Log In')
        login.click()

        time.sleep(5)
        pyautogui.typewrite('DebilBaj')
        pyautogui.press('tab')
        pyautogui.typewrite('Roflcopter27')
        time.sleep(1)
        pyautogui.press('Enter')
        time.sleep(10)

        deny=driver.find_element(By.CLASS_NAME, 'icon-close')
        deny.click()

        reply=driver.find_element(By.XPATH, "//button[contains(.,'Reply')]")
        reply.click()

        time.sleep(2)
        image=driver.find_element(By.CLASS_NAME, 'icon-image_post')
        driver.execute_script("arguments[0].click();", image)
        time.sleep(5)
        pyperclip.copy('C:\python\screenshot.png')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('Enter')
        time.sleep(5)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('Enter')
        time.sleep(5)
        driver.quit()