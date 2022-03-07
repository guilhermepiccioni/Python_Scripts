from selenium import webdriver
from time import sleep

from dotenv import dotenv_values

driver = webdriver.Chrome(
    executable_path="/home/guilherme/apps/VirtualEnv/Scripts/chromedriver_linux64_2/chromedriver"
)

"""
CREATE A DECORATOR TO MAKE THE PASSWORD SECURE
USE A .ENV FILE TO STORE YOUR PASSWORD
USE KIVY TO CREATE AN USER INTERFACE
"""


class Scripts:

    env = dotenv_values(".env")

    def __init__(self):
        pass

    @staticmethod
    def create_tabs():
        """Script for create necessary tabs"""
        driver.get("https://login.yahoo.com/")
        sleep(2)
        driver.execute_script("window.open('https://www.linkedin.com/')")
        sleep(2)
        driver.execute_script("window.open('https://web.telegram.org/k/')")
        sleep(2)
        driver.execute_script("window.open('https://www.instagram.com/')")
        sleep(5)

    @staticmethod
    def login_yahoo_email():
        """Script for login in the email yahoo."""
        values = Scripts.env

        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(
            f'{values.get("YAHOO_EMAIL")}'
        )
        driver.find_element_by_xpath('//*[@id="login-signin"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(
            f'{values.get("YAHOO_PASSWORD")}'
        )
        sleep(1)
        driver.find_element_by_xpath('//*[@id="login-signin"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="ybar-navigation-item-mail"]/a').click()
        sleep(2)

    @staticmethod
    def login_linkedin():
        """Script for login in linkedin"""
        values = Scripts.env

        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_xpath("/html/body/nav/div/a[2]").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(
            f'{values.get("LINKEDIN_LOGIN")}')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            f'{values.get("LINKEDIN_PASSWORD")}')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

    @staticmethod
    def login_telegram():
        """Script for login in telegram"""
        values = Scripts.env

        driver.switch_to.window(driver.window_handles[-2])
        sleep(1)
        driver.find_element_by_xpath('//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[2]/button[1]/div').click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]").send_keys(
            f'{values.get("LOCAL_COUNTRY")}')
        sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[3]/div/ul/li[29]/span[1]").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]").send_keys(
            f'{values.get("TELEGRAM_PHONE")}')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/button[1]/div').click()
        sleep(5)

    @staticmethod
    def login_instagram():
        """Script for login in the instagram."""
        values = Scripts.env

        sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(
            f'{values.get("INSTAGRAM_LOGIN")}')
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(
            f'{values.get("INSTAGRAM_PASSWORD")}')
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(8)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()


if __name__ == "__main__":
    sp = Scripts()
    sp.create_tabs()
    sp.login_yahoo_email()
    sp.login_linkedin()
    sp.login_telegram()
    sp.login_instagram()
