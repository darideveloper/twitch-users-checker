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
USERS_ACTIVE_PATH = os.path.join (CURRENT_FOLDER, "users_active.csv")
USERS_INACTIVE_PATH = os.path.join (CURRENT_FOLDER, "users_inactive.csv")

def main (): 
    
    # Start scraper
    scraper = WebScraping (headless=HEADLESS)
    
    data_active = [["user", "status"]]
    data_inactive = [["user", "status", "error"]]
    
    selectors = {
        "unable_account": '[data-a-target="core-error-message"]' 
    }
    
    # Get users from csv
    with open (USERS_PATH, "r", encoding='utf-8') as file:
        csv_reader = csv.reader (file)
        users = list (csv_reader)
    
    # Skip empry recors
    users = [user for user in users if user]
    
    # Get usernames and skip duplicated
    users = [user[0] for user in users]
    users = list (set (users))
    
    # Sort users
    users.sort ()
    
    # activeate each user
    for user_name in users:
        
        print (f"checking user: {user_name}...")
        
        # Load twitdh page
        scraper.set_page (f"https://www.twitch.tv/{user_name}")
        sleep (1)
        scraper.refresh_selenium ()
        
        # Get error
        errors = scraper.get_texts (selectors["unable_account"])
        if errors:
            data_inactive.append ([user_name, "inactive", errors[0]])
        else:
            data_active.append ([user_name, "active", ""])
        
        sleep (WAIT_SEC)
        
    # Save data in scv files
    with open (USERS_ACTIVE_PATH, "w", encoding='utf-8', newline='') as file:
        csv_writer = csv.writer (file)
        csv_writer.writerows (data_active)
        
    # Save data in scv files
    with open (USERS_INACTIVE_PATH, "w", encoding='utf-8', newline='') as file:
        csv_writer = csv.writer (file)
        csv_writer.writerows (data_inactive)
    
    print ("Finish activeation")

if __name__ == "__main__":
    main()