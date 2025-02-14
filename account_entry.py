from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from account_gen import human_like_typing, solve_captcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from pystyle import Center, Colors, Colorate
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import undetected_chromedriver as uc
import pyperclip
import random
import socket
import time
import os


# Connection points
COUNTRIES = ["'Turkey'", "'Poland'", "'Portugal'"]

# Track used accounts and reset when all done
used_accounts = []

def choose_country():
    return random.choice(COUNTRIES)

def connect_to_vpn(country):
    current = os.getcwd()
    os.chdir("C:\\Path\\to\\NordVPN") # cd into nord directory
    os.system(f"nordvpn -c -g {country}") # connects
    os.chdir(current) # cd back into working directory

def disconnect_vpn():
    current = os.getcwd()
    os.chdir("C:\\Path\\to\\NordVPN") # disconnects
    os.system(f"nordvpn disconnect")
    os.chdir(current)

def get_accounts(country):
    # Load accounts for the specific country and randomize them Determine before usage
    filepath = fr"C:\Path\to\accounts_{country}.txt"
    with open(filepath, 'r') as file:
        accounts = file.readlines()
    random.shuffle(accounts)
    return accounts

def verify_vpn_connection():
    time.sleep(5)
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Address: {ip_address}")

    except Exception as e:
        print("Error fetching IP info:", e)

def get_random_account(accounts):
    global used_accounts
    available_accounts = [acc for acc in accounts if acc not in used_accounts]
    
    if len(available_accounts) < (random.randint(3, 5)):
        used_accounts = []  # Reset if all accounts have been used
        available_accounts = accounts
    
    selected_accounts = random.sample(available_accounts, (random.randint(3, 5)))
    used_accounts.extend(selected_accounts)  # Track used accounts
    return selected_accounts

# Folder containing images
image_folder = fr"C:\Path\to\images"
used_images = set()

def get_random_image():
    global used_images
    # Gets all image files from the folder
    all_images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    
    # Excludes used images
    unused_images = list(set(all_images) - used_images)
    
    if not unused_images:
        # Resets used images if all have been used
        used_images = set()
        unused_images = all_images

    # Picks a random image
    chosen_image = random.choice(unused_images)
    used_images.add(chosen_image)
    
    return os.path.join(image_folder, chosen_image)

# File containing list names
list_names_file = fr"C:\Path\to\list_names.txt"
used_names = set()

def get_random_list_name():
    global used_names
    # Reads all names from the file
    with open(list_names_file, "r") as file:
        all_names = [line.strip() for line in file if line.strip()]
    
    # Excludes used names
    unused_names = list(set(all_names) - used_names)
    
    if not unused_names:
        # Resets used names if all have been used
        used_names = set()
        unused_names = all_names

    # Picks a random name
    chosen_name = random.choice(unused_names)
    used_names.add(chosen_name)
    
    return chosen_name

def main():
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
Inititation. In case of an error, reach Ralph
 """)))

    # Path need to be determined before usage
    service = Service(executable_path=r"C:\\Path\\to\\chromedriver.exe")

    while True:
        # VPN Setup
        country = choose_country()
        print(f"Connecting to VPN in {country}")
        connect_to_vpn(country)

        verify_vpn_connection()

        # Account Selection
        accounts = get_accounts(country)
        selected_accounts = get_random_account(accounts)

        # Browser Tasks
        browser_instances = []
        for account in selected_accounts:
            username, password = account.strip().split(':')

            try:
                driver = uc.Chrome(service=service, use_subprocess=True)
                browser_instances.append(driver)
                wait = WebDriverWait(driver, 10)
# Login
                driver.get("https://www.mywebsite.com/")

                driver.maximize_window()
                time.sleep(random.uniform(1, 2))

                username_input = driver.find_element(By.CSS_SELECTOR, "element")
                password_input = driver.find_element(By.CSS_SELECTOR, "element")

                human_like_typing(username_input, username)
                time.sleep(random.uniform(0.5, 1.5))

                human_like_typing(password_input, password)
                time.sleep(random.uniform(0.5, 1.5))

                driver.find_element(By.CSS_SELECTOR, "elemet").click()

                time.sleep(random.uniform(5.6, 6.2))

# Captcha handling
                try:
                    captcha = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element")))

                    site_key = captcha.get_attribute("sitekey")
                    url = driver.current_url

                    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe']")))
                    driver.switch_to.frame(iframe)

                    solve_captcha(driver, site_key, url)
                except:
                    pass
                    print("No CAPTCHA")

                try:
                    time.sleep(random.uniform(2.6, 3.2))
                    driver.find_element(By.ID, 'element').click()
                    time.sleep(random.uniform(4, 5))

                    driver.switch_to.default_content()
                    driver.find_element(By.XPATH, "element").click()
                except:
                    pass
                    print(f"Error while clicking captcha")

                time.sleep(random.uniform(2, 3))

                driver.switch_to.default_content()

# Cookie
                try:
                    cookie = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "element"))
                    )
                    time.sleep(random.uniform(1, 1.5))
                    cookie.click()

                except Exception as e:

                    try:
                        button = wait.until(
                            EC.element_to_be_clickable((By.ID, "element"))
                        )
                        time.sleep(random.uniform(1, 1.5))
                        button.click()
                        
                    except Exception as e:
                        time.sleep(random.uniform(1, 3))

# Go to mainpage
                try:
                    mainpage = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'element"]')))
                    mainpage.click()
                    time.sleep(random.uniform(4, 4.4))
                except:
                    pass

# Create list Part 1
                # 10% probabilty to create list
                list_trigger = random.random() < 0.1

                if list_trigger:
                    create_list_1 =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'element"]')))
                    create_list_1.click()
                    time.sleep(random.uniform(1, 1.5))

                    create_list_2 = driver.find_element(By.CSS_SELECTOR, 'element')
                    create_list_2.click()
                    time.sleep(random.uniform(4.3, 4.7))

# Offer Handling
                    try:
                        iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
                        driver.switch_to.frame(iframe)

                        dismiss = driver.find_element(By.CSS_SELECTOR, "element")
                        dismiss.click()

                        driver.switch_to.default_content()
                        time.sleep(random.uniform(2.1, 2.5))
                    except NoSuchElementException:
                        pass

# Create list Part 2
                    edit_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'element"]')))
                    edit_list.click()
                    time.sleep(random.uniform(2, 2.5))

                    # Gets a random image
                    random_image_path = get_random_image()
                    edit_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'element')))
                    edit_image.send_keys(random_image_path)
                    time.sleep(random.uniform(3, 3.2))
                    
                    # Gets a random name
                    list_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'element')))
                    list_name_input.clear()
                    list_name = get_random_list_name()
                    human_like_typing(list_name_input, list_name)
                    time.sleep(random.uniform(1, 1.5))

                    submit_button = driver.find_element(By.XPATH, "element")
                    submit_button.click()
                    time.sleep(random.uniform(1, 1.7))

                    # Copies the link of the list
                    driver.find_element(By. XPATH, f'element{list_name}').click()
                    time.sleep(random.uniform(0.5, 0.9))
                    driver.find_element(By. XPATH, 'element').click()
                    time.sleep(random.uniform(0.4, 0.8))
                    driver.find_element(By. XPATH, 'element').click()
                    time.sleep(random.uniform(2.2, 3.4))
                
# Go list
                # Determine before usage
                with open('list.txt', 'r') as file:
                    links = [line.strip() for line in file if line.strip()]

                random_link = random.choice(links)

                driver.get(random_link)
                time.sleep(random.uniform(2.2, 2.9))

# Action
                wait.until(EC.presence_of_element_located((By.XPATH, 'element'))).click()

                time.sleep(random.uniform(2.1, 2.3))

                option_xpath = "element" 
                option = driver.find_element(By.XPATH, option_xpath)
                current_class = option.get_attribute("class")

                if 'element' in current_class:
                    # Already in the desired state, do nothing
                    pass
                elif 'element' in current_class:
                    # In the non-desired, click once to go to the desired state
                    option.click()
                elif 'option' in current_class:
                    # In the non-desired, click twice to go to the desired state
                    option.click()
                    time.sleep(0.5)
                    option.click()

                time.sleep(random.uniform(1, 1.6))

                mix = driver.find_element(By.CSS_SELECTOR, 'element"]')

                # Checks the element and clicks only if it is "false"
                if mix.get_attribute("element") == "false":
                    mix.click()
                time.sleep(random.uniform(1.2, 1.5))

                # Touches to the list
                list_touch_button = driver.find_element(By.CSS_SELECTOR, 'element"]')
                if list_touch_button.get_attribute("element") == "false":
                    list_touch_button.click()
                time.sleep(1)

# Add some to the list
                if list_trigger:

                    # List of row indices that you want to potentially like
                    row = [str(i) for i in range(1, 35)]

                    # Decide the number of repetitions randomly between 25 and 30
                    num_repeats = random.randint(40, 60)

                    for _ in range(num_repeats):
                        try:
                            # Randomly selects one row
                            selected_row = random.choice(row)

                            # Constructs the XPath for the selected row
                            add_list = f"element'{selected_row}'element"
                            
                            # Clicks th options of a row
                            driver.find_element(By.XPATH, add_list).click()
                            time.sleep(random.uniform(2, 3))

                            # Clicks add to list
                            driver.find_element(By.XPATH, 'element').click()
                            time.sleep(random.uniform(2, 3))

                            # Clicks list name
                            driver.find_element(By.XPATH, f"element'{list_name}'").click()
                            time.sleep(random.uniform(2, 3))

                            # If already added
                            already_added = WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.XPATH, 'element'))
                            )
                            if already_added:
                                time.sleep(random.uniform(0.7, 1.2))
                                already_added.click()
                                row.remove(selected_row)             

                        except Exception as e:
                            # Removes the row from the list to avoid retrying the same one
                            if selected_row in row:
                                row.remove(selected_row)

                    time.sleep(random.uniform(0.4, 0.7))

                    # Determine the list file
                    
                    link = pyperclip.paste()
                    with open("list.txt", "a") as file:
                        file.write(link + "\n")

                time.sleep(1)

            except Exception as e:
                print(Colors.red, "An error occurred", str(e))

        time.sleep(4)

         # Waits for determined time
        print(f"Running tasks for {len(browser_instances)} instances. Waiting for 15-20 minutes.")
        end_time = datetime.now() + timedelta(minutes=(random.randint(15, 20)))
        while datetime.now() < end_time:
            time.sleep(10)  # Keeps lightweight and checks every 10 seconds

        # Clean up
        print("Closing browser instances.")
        for driver in browser_instances:
            driver.quit()

        # Disconnect VPN
        print("Disconnecting from VPN.")
        disconnect_vpn()

        # # Break for the ip (not sure if it is really needed)
        # time.sleep(random.randint(12, 18) * 60) 
        
if __name__ == "__main__":
        main()