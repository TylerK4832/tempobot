from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from random import seed
from random import randint

COMMENTS = ["I love sig phi", "AWESOME!", "So cool", "Nice!", 
            "Sig phi is the best", "What fine young men", "Wow!", "I love tempo",
            "Sig phi is awesome", "Tempo is such a cool place to live", "Comment", "Nice", 
            "Rush sig phi",
            "SPD ROCKS", "What a cool fraternity", "I wish i was them", "So handsome", "So cute",
            "I love SPD", "wowowowowow", "Tempo is awesome", ":)", ":))))))", ":->", "Go sig phi"]

def generateRandomComment(comments):
    return comments[randint(0, len(comments)-1)]

def getRandomTime():
    randTime = randint(20, 25)
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

        comment = generateRandomComment(COMMENTS)

        # lines = open('quotes.txt').read().splitlines()
        # comment = random.choice(lines)

        time.sleep(1)

        commentInput.send_keys(comment)
        commentInput.send_keys(Keys.ENTER)

    def goToPage(self, url):
        self.browser.get(url)

username = input("Enter username\n")
password = input("Enter password\n")

bot = InstagramBot(username, password)

bot.signIn()
bot.goToPage('https://www.instagram.com/p/ClzLaZgvPjs/')
time.sleep(3)

while(True):
    bot.commentOnTempo()
    time.sleep(getRandomTime())