from .pages.product_page import ProductPage
# import time
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# links = list(map(lambda x: link + str(x), range(0, 7)))
# links.append(pytest.param("bugged_link", marks=pytest.mark.xfail))
# links.append(link + str(8))
# links.append(link + str(9))


# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     # time.sleep(10)
#     page.add_message_is_correct()
#     page.basket_price_message_is_correct()


@pytest.mark.xfail(reason="negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappeare_succes_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
