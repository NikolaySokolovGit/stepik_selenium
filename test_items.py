def test_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert browser.find_elements_by_css_selector('.btn-add-to-basket')
