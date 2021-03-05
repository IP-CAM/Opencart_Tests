from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.products_add_and_edit_page import ProductsAddAndEditPage
import pytest
import allure


@allure.title("Тест на добавление продукта")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.product
def test_add_product(browser):
    LoginPage(browser).login()
    AdminPage(browser)\
        .go_to_product_page()\
        .add_product()
    ProductsAddAndEditPage(browser)\
        .general_info("HA_РОБОфон 2000", "Лучший в мире смартфон", "Робофон 2000", "111", "A", "Notebook")\
        .data_info("2000-ъы")\
        .get_monitor_category_link()\
        .option_add_delivery_date()\
        .save()\
        .should_be_success_alert()


@allure.title("Тест на редактирование продукта")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.product
def test_edit_product(browser):
    LoginPage(browser).login()
    AdminPage(browser)\
        .go_to_product_page()\
        .edit_product(2)
    ProductsAddAndEditPage(browser)\
        .general_info("", "Ноутбук", "", "", "", "")\
        .option_required_no_select()\
        .save()\
        .should_be_success_alert()


@allure.title("Тест на удаление продукта")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.product
def test_delete_product(browser):
    LoginPage(browser).login()
    AdminPage(browser).go_to_product_page()\
        .new_product_choice(3)
    AdminPage(browser).delete_product()\
        .alert_accept()
    ProductsAddAndEditPage(browser).should_be_success_alert()











