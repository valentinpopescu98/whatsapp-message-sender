import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Uses Selenium to automate sending a message
class WhatsAppSelenium:
    def __init__(self):
        self.driver = None
        self.message_box = None

        try:
            # Create option to allow browser to run as daemon and not be garbage collected
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('detach', True)

            # Create driver, access WhatsApp web endpoint
            self.driver = webdriver.Chrome(chrome_options)
            self.driver.get('https://web.whatsapp.com/')
            # driver.maximize_window()
        except Exception as e:
            print(str(e))

    def select_message_box(self, name: str):
        try:
            # Allow user to scan QR code
            input('Scan the code then press ENTER')

            # Search for receiver's name in the search box and wait for the frontend to return the results
            search_text_area = self.driver.find_element(
                By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="3"]')
            search_text_area.send_keys(name)
            time.sleep(0.5)

            # Open the contact chat by clicking its picture, also the only picture in an ordered
            # list with the returned contacts that follow the given regex in the search-box.
            # Clicking the picture or the body of the div has the same result, opening the chat with the contact
            chat_bubble = self.driver.find_element(By.CLASS_NAME, '_ak8l')
            chat_bubble.click()
            time.sleep(0.5)

            # Add the message to be sent in the chat
            self.message_box = self.driver.find_element(
                By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="10"]')
            time.sleep(0.5)
        except Exception as e:
            print(str(e))

    def send_wapp_msg(self, message: str):
        try:
            # Add the message to be sent in the chat
            self.message_box.send_keys(message)

            # Send the message
            self.message_box.send_keys(Keys.ENTER)
            print(f'Message sent: {message}')
        except Exception as e:
            print(str(e))

    def close(self):
        """Close the browser session."""
        time.sleep(0.5)
        self.driver.quit()

if __name__ == '__main__':
    try:
        whatsapp = WhatsAppSelenium()
        whatsapp.select_message_box('Mock friend')
        whatsapp.send_wapp_msg('Mock message')
    finally:
        whatsapp.close()
