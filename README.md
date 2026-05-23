# whatsapp-message-sender

Two approaches to automating WhatsApp message sending in Python — one via the WhatsApp public API (slower), one via Selenium browser automation (faster).

---

## Approaches

### pywhatkit (`pywhatkit_main.py`)

Uses the `pywhatkit` library which wraps the WhatsApp web API. Opens WhatsApp Web in the browser, sends the message instantly, then closes the tab. `pyautogui` and `pynput` handle the window focus click and Enter key press.

```python
send_wapp_msg('+40123456789', 'your message here')
```

- Phone number must include country code (e.g. `+40123456789`)
- Slower due to API overhead and sleep delays
- No QR scan required after initial WhatsApp Web login

### Selenium (`selenium_main.py`)

Drives Chrome directly via `selenium`, navigates to `web.whatsapp.com`, searches for the contact by name, and sends the message. Browser runs in detach mode (stays open after script ends).

```python
whatsapp = WhatsAppSelenium()
whatsapp.select_message_box('Contact Name')
whatsapp.send_wapp_msg('your message here')
whatsapp.close()
```

- Requires QR code scan on first run (prompts in terminal)
- Faster than pywhatkit once logged in
- CSS selectors target WhatsApp Web's DOM directly — may break if WhatsApp updates their frontend

---

## Installation

```bash
pip install -r requirements.txt
```

For Selenium, also download [ChromeDriver](https://chromedriver.chromium.org/) matching your Chrome version.

---

## Usage

```bash
# pywhatkit approach
python pywhatkit_main.py

# Selenium approach
python selenium_main.py
```

Edit the phone number / contact name and message directly in the `__main__` block of each file.
