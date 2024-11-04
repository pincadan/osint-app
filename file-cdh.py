import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class OSINT:
    def __init__(self, username):
        self.username = username
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def scrape_social_media(self):
        # Twitter
        twitter_url = f"https://twitter.com/{self.username}"
        self.driver.get(twitter_url)
        tweets = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='tweetText']")))
        print(f"\nLatest Tweets from {self.username} on Twitter:")
        for tweet in tweets:
            print(tweet.text)
        
        # Facebook
        facebook_url = f"https://www.facebook.com/{self.username}"
        self.driver.get(facebook_url)
        posts = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._5rgt._5gh8")))
        print(f"\nLatest Posts from {self.username} on Facebook:")
        for post in posts:
            print(post.text)
    
    def scrape_web(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"\nScraping {url}:")
        print(soup.prettify())
    
    def scrape_images(self, url):
        self.driver.get(url)
        images = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
        print(f"\nScraping images from {url}:")
        for image in images:
            src = image.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(f"image_{src.split('/')[-1]}", "wb") as f:
                f.write(response.content)
    
    def close(self):
        self.driver.quit()

# Example usage
osint = OSINT("example_username")
osint.scrape_social_media()
osint.scrape_web("https://example.com")
osint.scrape_images("https://example.com/gallery")
osint.close()