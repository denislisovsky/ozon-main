from selenium import webdriver
from selenium.webdriver.common.by import By
import random, requests, time
import pytest


class Pars:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        print("Start")
        self.driver_()


    def driver_(self): 
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
       # self.wait = WebDriverWait(self.driver, 15)

    def open_page(self): 
        url = random.choice(self._get_links())
        self.driver.get(url)

    # Добавление вещей в корзину
    def add_to_cart(self): 
        items = self._get_items_id()
     
        rand_items = random.choices(items, k=len(items)-random.randint(1, len(items)-1))
        
        for item in rand_items: 
            self.session.post(f"https://regem.store/catalog/cart/sku/{item}/addMini", headers=self.headers, params={"quantity": 1})

    # Получение корзины
    def get_cart(self):
        response = self.session.get("https://regem.store/catalog/cart/sku", headers=self.headers).json()
        self.set_cookies_selen()
        total_price = response["total_price"]
        return total_price

    # Добавление куки файлов из selenium -> requests.Session
    def set_cookies_req(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies: 
            self.session.cookies.set(cookie["name"], cookie["value"])

    # Добавление куки из requests в selenium
    def set_cookies_selen(self): 
        self.driver.delete_all_cookies()
        cookies = self.session.cookies
        for cookie in cookies: 
            cookie_dict = {
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
            'secure': cookie.secure,
        }
        # Необязательные поля (если есть)
        if cookie.expires:
            cookie_dict['expiry'] = cookie.expires
        if hasattr(cookie, 'http_only'):
            cookie_dict['httpOnly'] = cookie.http_only
        
        try:
            self.driver.add_cookie(cookie_dict)
            self.driver.refresh()
            # Для проверки можем раскомментить sleep
            time.sleep(15)
        except Exception as e:
            print(f"Не удалось добавить куки {cookie.name}: {e}")

    def _get_items_id(self) -> dict: 
        try: 
            elements_lst = []
            elements = self.driver.find_elements(By.CLASS_NAME, "js-designEditor-cart-icon")
            for i in elements: 
                elem = i.get_attribute("data-sku")
                elements_lst.append(elem)
            return elements_lst
        except Exception as e:
            print(e)

    def _get_links(self) -> dict:
        links = []
        for i in range(1, 7):
            url = f"https://regem.store/?page={i}&sort=sort"
            links.append(url)
        return links

@pytest.fixture
def parser():
    parsing = Pars()
    parsing.open_page()
    parsing.set_cookies_req()
    yield parsing
    parsing.driver.quit()

def test_add_to_cart(parser):
    parser.add_to_cart()
    total_price = parser.get_cart()
    assert isinstance(total_price, (int, float)), "Total price should be a number"
    assert total_price > 0, "Total price should be greater than 0"

if __name__ == "__main__": 
    # Для ручного тестирования
    p = Pars()
    p.open_page()
    p.set_cookies_req()
    p.add_to_cart()
    print("Total price:", p.get_cart())
    p.driver.quit()