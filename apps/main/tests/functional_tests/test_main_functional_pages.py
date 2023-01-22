

from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from test_main_functional_base import MainBaseFunctionalTeste


class MainPageFunctionalTest(MainBaseFunctionalTeste):
    
    # def tearDown(self):
    #     self.browser.quit()
    #     return super().tearDown()
    
    def test_main_login_page_text(self):
        
        self.browser.get('http://127.0.0.1:8000/admin')
        name_field = self.browser.find_element(By.ID, "id_username")
        name_field.send_keys("brunno")
        password_field = self.browser.find_element(By.ID, "id_password")
        password_field.send_keys("12345")
        login_button = self.browser.find_element(By.CLASS_NAME, "submit-row")
        login_button.click()
        
        pass
    
    def test_main_navegation_about_page_text(self):
        
        self.browser.get('http://127.0.0.1:8000/')
        
        assert "Início" in self.browser.title
        
        about_link = self.browser.find_element(By.LINK_TEXT, 'Sobre')
        about_link.click()
        
        assert "Sobre nós" in self.browser.title
        
        pass
    
    def test_main_navegation_contact_page_text(self):
        
        self.browser.get('http://127.0.0.1:8000/')
        
        assert "Início" in self.browser.title
        
        about_link = self.browser.find_element(By.LINK_TEXT, 'Contato')
        about_link.click()
        
        assert "Contato" in self.browser.title
        
        pass
    
    
    def test_main_navegation_login_page_text(self):
        
        self.browser.get('http://127.0.0.1:8000/')
        
        assert "Início" in self.browser.title
        
        about_link = self.browser.find_element(By.LINK_TEXT, 'Login')
        about_link.click()
        
        assert "Login" in self.browser.title
        
        pass
    
    
    def test_main_navegation_registration_page_text(self):
        
        self.browser.get('http://127.0.0.1:8000/')
        
        assert "Início" in self.browser.title
        
        about_link = self.browser.find_element(By.LINK_TEXT, 'Cadastre-se')
        about_link.click()
        
        assert "Cadastrar" in self.browser.title
        
        pass
    
    
    