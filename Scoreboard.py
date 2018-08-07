import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

# CONSTANTS #
URL = 'http://www.1zplay.com/score?category=csgo&state=active'
BASE_MATCH_URL = 'http://www.1zplay.com'
#############

# match data #
match_info = {
            "t1" : "",
            "t2" : "",
            "score_t1" : 0,
            "score_t2" : 0,
            "o_score_t1" : 0,
            "o_score_t2" : 0,
            "start_time" : ""
        }
#############

""" Main Method """ 
def main():
    while True:
        time.sleep(3600)
        if gameFound():
            #update loop here
            return 0

""" Check upcomming matches """
def gameFound():
    return 0

def update():
    return 0








    
