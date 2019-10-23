link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_item_add_to_basket(browser):
    browser.get(link)
    add_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert add_button, "Could not find an add button"
