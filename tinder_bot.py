from selenium import webdriver
from time import sleep, time
from selenium.webdriver.common.keys import Keys

from login_details import email, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_tinder(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        login = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
        login.click()
        sleep(1)
        self.facebook_login()
        sleep(6)
        try:
            allow_location_button = self.driver.find_element('xpath', '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
            allow_location_button.click()
        except:
            print('No location popup')

        try:
            notifications_button = self.driver.find_element('xpath', '/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
            notifications_button.click()
        except:
            print('No notification popup')

    def facebook_login(self):
        login_with_facebook = self.driver.find_element('xpath', '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
        login_with_facebook.click()
        sleep(2)
        base_window = self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_popup_window)
        email_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        pw_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login_button = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        email_field.send_keys(email)
        pw_field.send_keys(password)
        login_button.click()
        self.driver.switch_to.window(base_window)

    def right_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_RIGHT)

    def left_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_LEFT)

    def close_match(self):
        try:
            match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]//a')
            match_popup.click()
        except:
            print('No match popup')

        # Check for super like popup and handle it
        try:
            super_like_popup = self.driver.find_element('xpath', '/html/body/div[2]/div/div/button[2]/div[2]/div[2]')
            super_like_popup.click()
            print('Super like popup handled: No Thanks clicked.')
        except:
            print('No super like popup')

    def auto_swipe(self):
        keywords = ["insta", "gramm", "@", "inzztagrm", "i n t s a", "snap", "igggg", "iggg", "igg" "SC", "smapp", "intsa", "snepchat", "i n t s a"]
        swipe_duration = 20 * 60  # 20 minutes in seconds
        break_duration = 15 * 60  # 15 minutes in seconds

        while True:
            start_time = time()
            while time() - start_time < swipe_duration:
                sleep(2)
                try:
                    # Swipe up to view the bio
                    doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
                    doc.send_keys(Keys.ARROW_UP)
                    sleep(1)  # Wait a moment to load bio

                    # Check the bio for keywords
                    try:
                        bio_element = self.driver.find_element('xpath', '//div[contains(@class, "BreakWord") and contains(@class, "Whs(pl)")]')
                        bio_text = bio_element.text.lower()
                    except:
                        bio_text = ""

                    # Check the additional info section for keywords
                    try:
                        additional_info_element = self.driver.find_element('xpath', '//div[contains(@class, "Us(t)") and contains(@class, "Va(m)") and contains(@class, "D(ib)") and contains(@class, "NetWidth(100%,20px)") and contains(@class, "C($c-ds-text-secondary)")]')
                        additional_info_text = additional_info_element.text.lower()
                    except:
                        additional_info_text = ""

                    # Determine swipe direction based on keyword presence
                    if any(keyword in bio_text or keyword in additional_info_text for keyword in keywords):
                        self.left_swipe()
                    else:
                        self.right_swipe()

                except Exception as e:
                    print(f'Error: {e}')
                    self.close_match()

            print("Taking a break...")
            sleep(break_duration)

    def get_matches(self):
        match_profiles = self.driver.find_elements('class name', 'matchListItem')
        message_links = [profile.get_attribute('href') for profile in match_profiles if profile.get_attribute('href') not in ['https://tinder.com/app/my-likes', 'https://tinder.com/app/likes-you']]
        return message_links

    def send_messages_to_matches(self):
        links = self.get_matches()
        for link in links:
            self.send_message(link)

    def send_message(self, link):
        self.driver.get(link)
        sleep(2)
        text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div/div[1]/div/div/div[3]/form/textarea')
        text_area.send_keys("You know what's interesting about your pics?")
        text_area.send_keys(Keys.ENTER)

bot = TinderBot()
bot.open_tinder()
sleep(10)
bot.auto_swipe()
bot.send_messages_to_matches()
