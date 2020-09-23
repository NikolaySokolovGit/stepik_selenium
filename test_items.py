import time


def test_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_elements_by_css_selector('.btn-add-to-basket')
