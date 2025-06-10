import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_open_rings_section_and_view_products(driver):
    # Открываем главную страницу
    driver.get("https://regem.store/")
    wait = WebDriverWait(driver, 15)  # Увеличиваем время ожидания
    
    try:
        # Находим и кликаем на раздел "Кольца"
        rings_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'КОЛЬЦА') or contains(text(), 'Кольца')]")))
        rings_link.click()
        
        # Даем время для загрузки страницы
        time.sleep(2)  # Краткая пауза для стабилизации
        
        # Ждем загрузки хотя бы одного товара (пробуем разные варианты селекторов)
        try:
            products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item, .product, .item, .goods-item, .product-card")))
        except:
            # Если не нашли по классам, попробуем найти по структуре
            products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'product') or contains(@class, 'item')]")))
        
        # Проверяем, что товары загрузились
        assert len(products) > 0, "В разделе 'Кольца' не найдено товаров"
        
        print(f"Успешно загружено {len(products)} товаров в разделе 'Кольца'")
        
        # Дополнительная проверка - что мы действительно на странице колец
        assert "кольц" in driver.title.lower() or "кольц" in driver.current_url.lower(), "Не удалось подтвердить переход в раздел колец"
        
    except Exception as e:
        # Делаем скриншот при ошибке
        driver.save_screenshot("rings_error.png")
        pytest.fail(f"Тест не прошел: {str(e)}\nURL: {driver.current_url}\nTitle: {driver.title}")

def test_open_bracelets_section_and_view_products(driver):
    # Открываем главную страницу
    driver.get("https://regem.store/")
    wait = WebDriverWait(driver, 15)  # Увеличиваем время ожидания
    
    try:
        # Находим и кликаем на раздел "Браслеты"
        bracelets_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'БРАСЛЕТЫ') or contains(text(), 'Браслеты')]")))
        bracelets_link.click()
        
        # Даем время для загрузки страницы
        time.sleep(2)  # Краткая пауза для стабилизации
        
        # Ждем загрузки хотя бы одного товара (пробуем разные варианты селекторов)
        try:
            products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item, .product, .item, .goods-item, .product-card")))
        except:
            # Если не нашли по классам, попробуем найти по структуре
            products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'product') or contains(@class, 'item')]")))
        
        # Проверяем, что товары загрузились
        assert len(products) > 0, "В разделе 'Браслеты' не найдено товаров"
        
        print(f"Успешно загружено {len(products)} товаров в разделе 'Браслеты'")
        
        # Дополнительная проверка - что мы действительно на странице браслетов
        assert "браслет" in driver.title.lower() or "браслет" in driver.current_url.lower(), "Не удалось подтвердить переход в раздел браслетов"
        
    except Exception as e:
        # Делаем скриншот при ошибке
        driver.save_screenshot("bracelets_error.png")
        pytest.fail(f"Тест не прошел: {str(e)}\nURL: {driver.current_url}\nTitle: {driver.title}")

def test_open_pendants_section_and_view_products(driver):
    # Открываем главную страницу
    driver.get("https://regem.store/")
    wait = WebDriverWait(driver, 15)  # Увеличиваем время ожидания
    
    try:
        # Находим и кликаем на раздел "Подвески"
        pendants_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'ПОДВЕСКИ') or contains(text(), 'Подвески')]")))
        pendants_link.click()
        
        # Даем время для загрузки страницы
        time.sleep(2)  # Краткая пауза для стабилизации
        
        # Ждем загрузки хотя бы одного товара (пробуем разные варианты селекторов)
        try:
            products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-item, .product, .item, .goods-item, .product-card")))
        except:
            # Если не нашли по классам, попробуем найти по структуре
            products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'product') or contains(@class, 'item')]")))
        
        # Проверяем, что товары загрузились
        assert len(products) > 0, "В разделе 'Подвески' не найдено товаров"
        
        print(f"Успешно загружено {len(products)} товаров в разделе 'Подвески'")
        
        # Дополнительная проверка - что мы действительно на странице подвесок
        assert "подвеск" in driver.title.lower() or "подвеск" in driver.current_url.lower(), "Не удалось подтвердить переход в раздел подвесок"
        
    except Exception as e:
        # Делаем скриншот при ошибке
        driver.save_screenshot("pendants_error.png")
        pytest.fail(f"Тест не прошел: {str(e)}\nURL: {driver.current_url}\nTitle: {driver.title}")

