import os
from selenium import webdriver
from time import sleep
from dotenv import load_dotenv  # type: ignore

load_dotenv()

driver = webdriver.Chrome(executable_path=os.getenv("PATH_CHROME"))


class Scripts:
    @staticmethod
    def create_tabs():
        """
        Script to create necessary tabs.
        """

        driver.get(os.getenv("YAHOO"))
        sleep(2)
        driver.execute_script(os.getenv("LINKEDIN"))
        sleep(2)
        driver.execute_script(os.getenv("TELEGRAM"))
        sleep(2)
        driver.execute_script(os.getenv("INSTAGRAM"))
        sleep(5)

    @staticmethod
    def login_yahoo_email():
        """
        Script login in the email yahoo.
        """

        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(
            f'{os.getenv("YAHOO_EMAIL")}'
        )
        driver.find_element_by_xpath('//*[@id="login-signin"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(
            f'{os.getenv("YAHOO_PASSWORD")}'
        )
        sleep(1)
        driver.find_element_by_xpath('//*[@id="login-signin"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="ybar-navigation-item-mail"]/a').click()
        sleep(2)

    @staticmethod
    def login_linkedin():
        """
        Script login in linkedin.
        """

        driver.switch_to.window(driver.window_handles[-1])
        driver.find_element_by_xpath("/html/body/nav/div/a[2]").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(
            f'{os.getenv("LINKEDIN_LOGIN")}'
        )
        sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            f'{os.getenv("LINKEDIN_PASSWORD")}'
        )
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="organic-div"]/form/div[3]/button'
        ).click()

    @staticmethod
    def login_telegram():
        """
        Script to login in telegram.
        """

        driver.switch_to.window(driver.window_handles[-2])
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[2]/button[1]/div'
        ).click()
        sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]"
        ).send_keys(f'{os.getenv("LOCAL_COUNTRY")}')
        sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[3]/div/ul/li[29]/span[1]"
        ).click()
        sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]"
        ).send_keys(f'{os.getenv("TELEGRAM_PHONE")}')
        sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/button[1]/div'
        ).click()
        sleep(5)

    @staticmethod
    def login_instagram():
        """
        Script login in the instagram.
        """

        sleep(3)
        driver.switch_to.window(driver.window_handles[-3])
        driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        ).send_keys(f'{os.getenv("INSTAGRAM_LOGIN")}')
        driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
        ).send_keys(f'{os.getenv("INSTAGRAM_PASSWORD")}')
        sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]"
        ).click()
        sleep(5)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
        ).click()
        sleep(5)
        driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div[3]/button[2]"
        ).click()


if __name__ == "__main__":
    sp = Scripts()
    sp.create_tabs()
    sp.login_yahoo_email()
    sp.login_linkedin()
    sp.login_telegram()
    sp.login_instagram()
