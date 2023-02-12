import os
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_main_functional_base import MainBaseFunctionalTeste


class MainPageFunctionalTest(MainBaseFunctionalTeste):

    # def tearDown(self):
    #     self.browser.quit()
    #     return super().tearDown()

    def test_main_login_page_text(self):

        self.browser.get("http://127.0.0.1:8000/admin")
        name_field = self.browser.find_element(By.ID, "id_username")
        name_field.send_keys("brunno")
        password_field = self.browser.find_element(By.ID, "id_password")
        password_field.send_keys("12345")
        login_button = self.browser.find_element(By.CLASS_NAME, "submit-row")
        login_button.click()

        pass

    def test_main_navegation_about_page_text(self):

        self.browser.get("http://127.0.0.1:8000/")

        assert "Início" in self.browser.title

        about_link = self.browser.find_element(By.LINK_TEXT, "Sobre")
        about_link.click()

        assert "Sobre nós" in self.browser.title

        pass

    def test_main_navegation_contact_page_text(self):

        self.browser.get("http://127.0.0.1:8000/")

        assert "Início" in self.browser.title

        contact_link = self.browser.find_element(By.LINK_TEXT, "Contato")
        contact_link.click()

        assert "Contato" in self.browser.title

        pass

    def test_main_navegation_login_page_text(self):

        self.browser.get("http://127.0.0.1:8000/")

        assert "Início" in self.browser.title

        login_link = self.browser.find_element(By.LINK_TEXT, "Login")
        login_link.click()

        assert "Login" in self.browser.title

        pass

    def test_main_navegation_registration_page_text(self):

        self.browser.get("http://127.0.0.1:8000/")

        assert "Início" in self.browser.title

        register_link = self.browser.find_element(By.LINK_TEXT, "Cadastre-se")
        register_link.click()

        assert "Cadastrar" in self.browser.title

        pass

    def test_main_navegation_registration_page_client_text(self):

        self.browser.get("http://127.0.0.1:8000/register")

        assert "Cadastrar" in self.browser.title

        name_link = self.browser.find_element(By.ID, "id_name")
        name_link.send_keys("brunno")

        last_name_link = self.browser.find_element(By.ID, "id_last_name")
        last_name_link.send_keys("brunno")

        email_link = self.browser.find_element(By.ID, "id_email")
        email_link.send_keys("brunno@gmail.com")

        password_link = self.browser.find_element(By.ID, "id_password")
        password_link.send_keys("12345")

        date_link = self.browser.find_element(By.ID, "id_birth_date")
        date_link.send_keys("22/22/1992")

        icon_link = self.browser.find_element(By.ID, "id_icon")
        icon_link.send_keys(
            os.getcwd() + "/apps/main/tests/functional_tests/pessoa.png"
        )

        register_button = self.browser.find_element(By.CLASS_NAME, "btn")
        register_button.send_keys("\n")

        pass

    def test_main_navegation_registration_page_store_text(self):

        self.browser.get("http://127.0.0.1:8000/register")

        assert "Cadastrar" in self.browser.title

        register_store_link = self.browser.find_element(By.ID, "tab-register-l")
        register_store_link.click()
        time.sleep(2)

        cnpj_link = self.browser.find_element(By.ID, "id_cnpj")
        cnpj_link.send_keys("brunno")

        name_link = self.browser.find_element(By.ID, "id_corporate_name")
        name_link.send_keys("brunno")

        name_link.send_keys(Keys.TAB)
        time.sleep(2)

        actions = ActionChains(self.browser)
        actions.send_keys("example@gmail.com")
        actions.perform()

        time.sleep(2)

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.TAB)
        actions.send_keys("12345")
        actions.perform()

        contact_link = self.browser.find_element(By.ID, "id_contact")
        contact_link.send_keys("9999999")

        segment_link = self.browser.find_element(By.ID, "id_segment")
        segment_link.send_keys("Alimentação")

        logo_link = self.browser.find_element(By.ID, "id_logo")
        logo_link.send_keys(
            os.getcwd() + "/apps/main/tests/functional_tests/pessoa.png"
        )

        register_button = self.browser.find_element(By.CLASS_NAME, "btn")
        register_button.send_keys("\n")

        assert self.browser.current_url == "http://127.0.0.1:8000/login"

        pass
