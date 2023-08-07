import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Uses Selenium to automate sending a message
def send_wapp_msg(name: str, message: str):
    try:
        # Create option to allow browser to run as daemon and not be garbage collected
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        # Create driver, access WhatsApp web endpoint and maximize window
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://web.whatsapp.com/')
        driver.maximize_window()

        # Allow user to scan QR code
        input('Scan the code then press ENTER')

        # Search for receiver's name in the search box and wait for the frontend to return the results
        search_text_area = driver.find_element(By.XPATH, value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
        search_text_area.send_keys(name)
        time.sleep(0.5)

        # Open the contact chat by clicking its picture, also the only picture in an ordered list with the returned
        # contacts that follow the given regex in the search-box
        #
        # Clicking the picture or the body of the div has the same result, opening the chat with the contact
        chat_bubble = driver.find_element(By.CLASS_NAME, value='_1AHcd')
        chat_bubble.click()

        # Add the message to be sent in the chat
        message_text_area = driver.find_element(By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        message_text_area.send_keys(message)

        # Send the message
        send_button = driver.find_element(By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        send_button.click()

        print('Message sent!')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    send_wapp_msg('Mock friend', 'Mock message')