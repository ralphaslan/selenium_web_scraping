from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from pystyle import Center, Colors, Colorate
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import schedule
import random
import socket
import time
import pytz
import os


COUNTRIES = ["'Turkey'", "'Poland'", "'Portugal'"]

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

def verify_vpn_connection():
    time.sleep(5)
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Address: {ip_address}")

    except Exception as e:
        print("Error fetching IP info:", e)

def solve_captcha(driver, site_key, url):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("key")
    solver.set_website_url(url)
    solver.set_website_key(site_key)

    answer = solver.solve_and_return_solution() 
    driver.execute_script('script')
    if answer != 0:
        print("Captcha solved")
    else:
        print("Task finished with error: " + solver.error_code)

def human_like_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.25))

# Probabilities need to be increased
uname_items = ["few", "items", "here"]
uname_items2 = ["few", "items", "here"]

def generate_credentials(num_entries, file_name="accounts.txt"):
    with open(file_name, 'w') as file:
        for _ in range(num_entries):

            item1 = random.choice(uname_items)
            item2 = random.choice(uname_items2)
            runame = item1 + item2

            email = runame + str(random.randint(100, 9999)) + "@mymail.com"
            password = runame + str(random.randint(100, 9999))
            file.write(f"{email}:{password}\n")
    print(f"{num_entries} entries saved in accounts.txt file")

def save_credentials(country, username, password):
    file_path = f"accounts_{country}.txt"
    with open(file_path, 'a') as file:  # Opens in append mode
        file.write(f"{username}:{password}\n")

def get_random_display_name(display_names_path):
    with open(display_names_path, 'r') as file:
        d_names = file.readlines()
    d_names = [d_name.strip() for d_name in d_names if d_name.strip()]
    return random.choice(d_names)

# Path need to be determined before usage
display_names_path = (r"C:\\Path\\to\\display_names.txt")

def main(): 
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
In case of error, reach Ralph
 """)))

    num_entries = int(input("Enter the number of accounts you want to generate: "))
    generate_credentials(num_entries)

    # Path need to be determined before usage
    service = Service(executable_path=r"C:\\Path\\to\\chromedriver.exe")

    wait = WebDriverWait(driver, 10)

    while True:
# VPN connection
            country = choose_country()
            print(f"Connecting to VPN in {country}")
            connect_to_vpn(country)

            verify_vpn_connection()

            # Path need to be determined before usage
            with open(r"C:\\Path\\to\\accounts.txt", 'r') as file:
                accounts = file.readlines()

                drivers = []

            for account in accounts:

                driver = uc.Chrome(service=service, use_subprocess=True)

                username, password = account.strip().split(':')

# Registeration Phase
                try:
                    driver.get("https://www.mywebsite/signup")

                    driver.maximize_window()
                    time.sleep(random.uniform(4, 5))

                    # Cookie Handling
                    try:
                        cookie = wait.until(
                            EC.element_to_be_clickable((By.XPATH, 'element'))
                        )
                        time.sleep(random.uniform(1, 1.5))
                        cookie.click()

                    except Exception as e:

                        try:
                            button = wait.until(
                                EC.element_to_be_clickable((By.XPATH, 'element'))
                            )
                            time.sleep(random.uniform(1, 1.5))
                            button.click()
                            
                        except Exception as e:
                            time.sleep(random.uniform(1, 3))

                    try:
                        register_uname = wait.until(EC.presence_of_element_located((By.XPATH, 'element')))
                        human_like_typing(register_uname, username)
                        time.sleep(random.uniform(0.5, 1.5))

                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'element')))
                        next_button.click()
                        time.sleep(random.uniform(1, 2))

                        register_password = wait.until(EC.presence_of_element_located((By.XPATH, 'element')))
                        human_like_typing(register_password, password)
                        time.sleep(random.uniform(0.5, 1.5))

                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'element')))
                        next_button.click()
                        time.sleep(random.uniform(1, 3))

                        register_dname = wait.until(EC.presence_of_element_located((By.XPATH, 'element')))
                        dname = get_random_display_name(display_names_path)
                        human_like_typing(register_dname, dname)
                        time.sleep(random.uniform(0.5, 1.5))

                        bdateday = wait.until(EC.presence_of_element_located((By.XPATH, 'element')))
                        bday = str(random.randint(1, 28))
                        human_like_typing(bdateday, bday)
                        time.sleep(random.uniform(0.5, 1.5))

                        bdaymonth = Select(wait.until(EC.presence_of_element_located((By.ID, "element"))))
                        available_options = bdaymonth.options[1:]
                        random_option = random.choice(available_options)
                        bdaymonth.select_by_visible_text(random_option.text)

                        bdateyear = wait.until(EC.presence_of_element_located((By.XPATH, 'element')))
                        byear = str(random.randint(1990, 2005))
                        human_like_typing(bdateyear, byear)
                        time.sleep(random.uniform(0.5, 1.5))

                        genders = [
                            'male',
                            'female',
                            'other'
                        ]

                        random_gender_xpath = random.choice(genders)
                        gender = wait.until(EC.element_to_be_clickable((By.XPATH, random_gender_xpath)))
                        gender.click()
                        time.sleep(random.uniform(0.5, 1.5))

                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'element')))
                        next_button.click()
                        time.sleep(random.uniform(2, 3))

                        try:
                            checkbox = driver.find_element(By.XPATH, 'element')
                            checkbox.click()
                            time.sleep(random.uniform(0.5, 1.5))
                        except:
                            pass

                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'element')))
                        next_button.click()
                        time.sleep(random.uniform(7, 9))

                    except Exception as e:
                        print(f"An error occurred during registration: {e}")
                        # Add a driver quit and repeat of the process to have consistency
                        # Or simply go back to first page and repeat? need to be tested

# Captcha handling
                    try:
                        captcha = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "element")))

                        site_key = captcha.get_attribute("sitekey")
                        url = driver.current_url

                        iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
                        driver.switch_to.frame(iframe)

                        solve_captcha(driver, site_key, url)
                    except:
                        pass
                        print("No CAPTCHA")

                    time.sleep(3) 

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

# Settings display and social optioning out
                    try:
                        mainpage = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'element"]')))
                        mainpage.click()
                        time.sleep(random.uniform(4, 4.4))
                    except:
                        pass

                    wait.until(EC.presence_of_element_located((By.XPATH, "element"))).click()
                    time.sleep(random.uniform(1, 2))

                    settings_xpath = "element"
                    wait.until(EC.presence_of_element_located((By.XPATH, settings_xpath))).click()
                    time.sleep(random.uniform(2, 3))

                    hide_option_xpath = "element"
                    wait.until(EC.presence_of_element_located((By.XPATH, hide_option_xpath))).click()
                    time.sleep(random.uniform(2, 3))

                    hide_option2_xpath = "element"
                    driver.find_element(By.XPATH, hide_option2_xpath).click()
                    time.sleep(random.uniform(2, 3))

                    hide_option3_xpath = "element"
                    driver.find_element(By.XPATH, hide_option3_xpath).click()
                    time.sleep(random.uniform(2, 3))
                    
# Search & find
                    driver.find_element(By.XPATH, "element").click()
                    search = driver.find_element(By.XPATH, "element")
                    name = ("name")
                    human_like_typing(search, name)
                    time.sleep(random.uniform(2, 3))
                    
                    # Filter
                    driver.find_element(By.XPATH, 'filtering element').click()
                    time.sleep(random.uniform(1, 3))
                
                    # Determine the id before usage
                    wait.until(EC.presence_of_element_located(
                        (By.XPATH, 'unique element')
                    )).click()
                    time.sleep(random.uniform(1, 3))

                    found_xpath = "element"
                    found = wait.until(EC.presence_of_element_located((By.XPATH, found_xpath)))

                    if found and random.random() < 0.6:
                        found.click()
                    else :
                        pass
                    
                    time.sleep(1)

# Probable paths
                    # List of rows
                    row_probabilities = [1, 2, 3, 4]

                    random.shuffle(row_probabilities)

                    # Loop through each randomly shuffled index
                    for row in row_probabilities:
                        # Introduces randomness with a probability of clicks
                        if random.random() > 0.5:  # 50% chance of liking a song
                            touch_xpath = f"element'{row}']element"
                            
                            try:
                                touch = driver.find_element(By.XPATH, touch_xpath)
                                
                                if touch.get_attribute("element") == 'false':
                                    touch.click()
                                else:
                                    pass
                                time.sleep(random.uniform(1, 3))
                            
                            except Exception as e:
                                print(f"Could not touch row {row}: {e}")
                                continue

                    path_choice = random.choice([1, 2, 3, 4])

                    # Alternate Path 1
                    if path_choice == 1:
                        # Determine name before usage
                        more_button = driver.find_element(By.XPATH, 'element with name')
                        more_button.click()
                        time.sleep(random.uniform(0.5, 1))

                        another_button = driver.find_element(By.XPATH, 'element')
                        another_button.click()

                    # Alternate Path 2, random one path within four options
                    elif path_choice == 2:

                        selected_row = random.choice(row_probabilities)

                        go_to_somewhere_xpath = f"element'{selected_row}'element"
                        
                        driver.find_element(By.XPATH, go_to_somewhere_xpath).click()
                        time.sleep(random.uniform(2, 3))

                        driver.find_element(By.XPATH, "element").click()
                        time.sleep(random.uniform(2, 3))

                    # Alternate Path 3
                    elif path_choice == 3:

                        # Random list from the file Determine the name before usage
                        with open('list.txt', 'r') as file:
                            links = [line.strip() for line in file if line.strip()]

                        random_link = random.choice(links)

                        driver.get(random_link)
                        time.sleep(random.uniform(2.2, 2.9))

                    # Alternate Path 4 
                    elif path_choice == 4:

                        # Just does the action
                        pass

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

# Save credentials
                    save_credentials(country, username, password)
                    print(f"Credentials saved for {country}: {username}:{password}")

                    time.sleep(1)
                    
                    drivers.append(driver)

                except Exception as e:
                    print(Colors.red, "An error occurred", str(e))

                time.sleep(4)

            while True:
                schedule.run_pending()
                time.sleep(1)

if __name__ == "__main__":
        main()