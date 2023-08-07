import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

# pywhatkit uses WhatsApp API to automate sending a message
def send_wapp_msg(phone_number: str, message: str):
    try:
        # Use API to send request for sending a message
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            tab_close=True
        )
        # Click on the screen to ensure the correct window/tab is selected and wait a little bit
        pyautogui.click()
        time.sleep(0.5)

        # Press enter to send message
        Controller().press(Key.enter)
        Controller().release(Key.enter)

        print('Message sent!')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    # Write phone number with country included (e.g. +40123456789) and enter message to send
    send_wapp_msg('+40123456789', 'Mock message noroc')
