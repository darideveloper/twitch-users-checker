import os
import csv
from time import sleep
from dotenv import load_dotenv
from scraping.web_scraping import WebScraping

load_dotenv ()
HEADLESS = os.getenv ("HEADLESS") == "True"
WAIT_SEC = int(os.getenv ("WAIT_SEC"))

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
        csv_reader = csv.reader (file)
        users = list (csv_reader)
    
    # Validate each user
    for user in users:
        user_name = user[0]
        print (f"Validating user: {user_name}...")
        
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
        
        sleep (WAIT_SEC)
        
    # Save data in scv file
    with open (USERS_PATH, "w", encoding='utf-8') as file:
        csv_writer = csv.writer (file)
        csv_writer.writerows (data)
        

if __name__ == "__main__":
    main()