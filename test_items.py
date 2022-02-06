from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_btnAddToCart_isPresent(browser):
    browser.get(link)
    btnAddToCart= None
    try:
        btnAddToCart = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    except NoSuchElementException:
        assert btnAddToCart is not None, 'There is no button "Add to Cart" on the page'

