import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = '/home/alex/Course/ChromeDriver/chromedriver'



class InternetSpeedTwitterBot:

    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

#                       getting internet speed                       #

    def get_internet_speed(self):

        # get a speedtest web-site in to selenium
        self.driver.get('https://www.speedtest.net/')

        #find the go button
        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        # wetting for speed to checked
        time.sleep(60)

        # taking data to variable
        self.download_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.upload_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.ping = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(self.upload_speed, self.upload_speed, self.ping)
        return self.download_speed, self.upload_speed, self.ping


#                      post in twitter                          #

    def post_at_twitter(self, download_speed, upload_speed, ping):

        self.driver.implicitly_wait(10)

        # getting twitter into selenium
        self.driver.get("https://twitter.com")
        self.driver.implicitly_wait(25)

        # click login with email
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
        self.driver.implicitly_wait(10)

        # finding the email field and type email
        email_field = self.driver.find_element(By.NAME, 'text')
        email_field.send_keys('email')
        self.driver.implicitly_wait(10)
        email_field.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(10)

        # finding the password field and type password
        password_pass = self.driver.find_element(By.NAME, "password")
        password_pass.send_keys('password')
        password_pass.send_keys(Keys.ENTER)

        # twitting speed
        twitter_post_field = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        twitter_post_field.send_keys(f'My speed with airtel today:'
                                     f' download: {download_speed}'
                                     f'upload: {upload_speed}, ping: {ping}')

        # click the send button

        send_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_button.click()
        #
        # self.driver.close()


bot = InternetSpeedTwitterBot()
speeds = bot.get_internet_speed()
download_speed = speeds[0]
upload_speed = speeds[1]
ping = speeds[2]
bot.post_at_twitter(download_speed, upload_speed, ping)

