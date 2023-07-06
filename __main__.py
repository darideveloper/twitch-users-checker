import os
import csv
from time import sleep
from dotenv import load_dotenv
from scraping.web_scraping import WebScraping

load_dotenv ()
HEADLESS = os.getenv ("HEADLESS")

CURRENT_FOLDER = os.path.dirname (__file__)
USERS_PATH = os.path.join (CURRENT_FOLDER, "users.csv")

def main (): 
    
    # Start scraper
    scraper = WebScraping (headless=HEADLESS)
    
    data = []
    
    selectors = {
        "unable_account": '[data-a-target="core-error-message"]' 
    }
    
    # Get users from csv
    with open (USERS_PATH, "r", encoding='utf-8') as file:
        users = list (csv.reader (file))
    
    # Validate each user
    for user in users:
        user_name = user[0]
        
        # Load twitdh page
        scraper.set_page (f"https://www.twitch.tv/{user_name}")
        sleep (1)
        scraper.refresh_selenium ()
        
        # Get error
        errors = scraper.get_texts (selectors["unable_account"])
        if errors:
            data.append ([user_name, "inactive", errors[0]])
        else:
            data.append ([user_name, "active", ""])
        
        sleep (1)
        

if __name__ == "__main__":
    main()