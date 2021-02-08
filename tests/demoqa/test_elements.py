import pytest
from playwright.sync_api import Page
from playwright.sync_api._generated import ElementHandle
from pytest import fixture

from pages import Buttons, CheckBox, TextBox

base_url: str = "https://www.demoqa.com"


@pytest.mark.elements
class TestBase:
    def test_visit_elements_page(self, page: Page) -> None:
        """Test that the Elements page can be navigated to.

        :param page: A Playwright browser page.
        """
        page.goto(f"{base_url}/elements")
        header_text: str = page.inner_text(".main-header")

        assert "Elements" in header_text

    def test_collapse_elements_container(self, page: Page) -> None:
        """Test that the Elements container may be collapsed by a user.

        :param page: A Playwright browser page.
        """
        page.goto(f"{base_url}/elements")
        element_group: ElementHandle = page.wait_for_selector(".element-group")

        page.click(".header-right")

        element_list_class: str = element_group.eval_on_selector(
            ".element-list", "el => el.className"
        )

        assert "show" not in element_list_class


@pytest.mark.elements
@pytest.mark.text_box
class TestTextBox:
    user: dict = {
        "name": "Test Tester",
        "email": "test@test.com",
        "currentAddress": "3930 N Pine Grove Ave, Chicago, IL 60613",
        "permanentAddress": "24 Girard St, Rochester, NY 14610",
    }

    def test_submit_valid_data(self, page: Page) -> None:
        """Test that valid data may be submitted.

        :param page: A Playwright browser page.
        """
        text_box_page = TextBox(page)

        text_box_page.navigate()
        text_box_page.fill_form(self.user)

        text_box_page.submit_button.click()

        output_field: ElementHandle = page.wait_for_selector("#output")
        for key, value in self.user.items():
            ele_value: str = output_field.eval_on_selector(
                f"#{key}", "el => el.innerText"
            )
            assert value in ele_value

    def test_error_when_invalid_email(self, page: Page) -> None:
        """Test that invalid data may not be submitted.

        :param page: A Playwright browser page.
        """
        text_box_page = TextBox(page)

        text_box_page.navigate()
        text_box_page.email_field.fill("test")

        text_box_page.submit_button.click()

        email_class: str = text_box_page.user_form.eval_on_selector(
            "#userEmail", "el => el.className"
        )
        assert "field-error" in email_class


@pytest.mark.elements
@pytest.mark.check_box
class TestCheckBox:
    def test_expansion(self, page: Page) -> None:
        """Test that the checkbox list may be expanded.

        :param page: A Playwright browser page.
        """
        check_box_component = CheckBox(page)

        check_box_component.navigate()
        check_box_component.expand_all_button.click()

        list_class: str = check_box_component.check_box_list.evaluate(
            "el => el.className"
        )
        assert "rct-node-expanded" in list_class

    def test_select_check_box(self, page: Page) -> None:
        """Test that a specific checkbox may be selected.

        :param page: A Playwright browser page.
        """
        check_box_text: str = "notes"

        check_box_component = CheckBox(page)

        check_box_component.navigate()
        check_box_component.expand_all_button.click()

        check_box: ElementHandle = check_box_component.check_box(
            text=check_box_text
        )
        check_box.click()

        icon: ElementHandle = check_box.wait_for_selector(".rct-icon-check")

        visible: bool = icon.is_visible()

        result: str = check_box_component.result_field.evaluate(
            "el => el.innerText"
        )
        assert visible and check_box_text in result


@pytest.mark.elements
@pytest.mark.buttons
class TestButtons:
    @pytest.mark.parametrize(
        "button_type",
        [
            ("Double Click", "doubleClickMessage"),
            ("Right Click", "rightClickMessage"),
            ("Click", "dynamicClickMessage"),
        ],
    )
    def test_click_types(self, button_type: fixture, page: Page) -> None:
        """Test that specific click actions provide a result.

        :param button_type: A tuple containing click action and result.
        :param page: A Playwright browser page.
        """
        click_action, result = button_type
        buttons_page = Buttons(page)

        buttons_page.navigate()

        if click_action == "Double Click":
            buttons_page.double_click_button.dblclick()
        elif click_action == "Right Click":
            buttons_page.right_click_button.click(button="right")
        else:
            buttons_page.dynamic_click_button.click()

        message: ElementHandle = page.is_visible(f"#{result}")

        assert message
