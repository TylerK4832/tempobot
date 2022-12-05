from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from random import seed
from random import randint

COMMENTS = ["I love sig phi", "AWESOME!", "So cool", "xian zai wo you bing qi ling", 
            "Sig phi is the best", "what fine young men", "wow!", "I love tempo",
            "Sig phi is awesome", "Tempo is such a cool place to live", "I am a real person!"]

def generateRandomComment(comments):
    return comments[randint(0, len(comments)-1)]

def getRandomTime():
    randTime = randint(7, 15)
    return randTime

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)
        emailInput = self.browser.find_element(By.XPATH, '//input[@name="username"]')
        passwordInput = self.browser.find_element(By.XPATH, '//input[@name="password"]')

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)

        passwordInput.send_keys(Keys.ENTER)
        time.sleep(getRandomTime())

    def commentOnTempo(self):

        self.browser.find_element(By.XPATH, "//div/form").click()
        commentInput = self.browser.find_element(By.XPATH, "//form/textarea")

        # comment = generateRandomComment(COMMENTS)

        lines = open('quotes.txt').read().splitlines()
        comment = random.choice(lines)

        time.sleep(1)

        commentInput.send_keys(comment)
        commentInput.send_keys(Keys.ENTER)

    def goToPage(self, url):
        self.browser.get(url)



bot = InstagramBot('INSERT EMAIL OR USERNAME HERE', 'INSERT PASSWORD HERE')

bot.signIn()
bot.goToPage('https://www.instagram.com/p/ClzLaZgvPjs/')
time.sleep(3)

while(True):
    bot.commentOnTempo()
    time.sleep(getRandomTime())