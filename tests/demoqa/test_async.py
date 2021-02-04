import pytest
from playwright.async_api import async_playwright
from playwright.async_api._generated import ElementHandle
from pytest import fixture

base_url: str = "https://www.demoqa.com"


@pytest.mark.asyncio
@pytest.mark.elements
class TestBase:
    async def test_visit_elements_page(self) -> None:
        """Test that the Elements page can be navigated to.

        :param page: A Playwright browser page.
        """
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(f"{base_url}/elements")
            header_text: str = await page.inner_text(".main-header")

            assert "Elements" in header_text

    async def test_collapse_elements_container(self) -> None:
        """Test that the Elements container may be collapsed by a user.

        :param page: A Playwright browser page.
        """
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(f"{base_url}/elements")
            element_group: ElementHandle = await page.wait_for_selector(
                ".element-group"
            )

            await page.click(".header-right")

            element_list_class: str = await element_group.eval_on_selector(
                ".element-list", "el => el.className"
            )

            assert "show" not in element_list_class


@pytest.mark.asyncio
@pytest.mark.elements
@pytest.mark.text_box
class TestTextBox:
    user: dict = {
        "name": "Test Tester",
        "email": "test@test.com",
        "currentAddress": "3930 N Pine Grove Ave, Chicago, IL 60613",
        "permanentAddress": "24 Girard St, Rochester, NY 14610",
    }

    async def test_submit_valid_data(self):
        """Test that valid data may be submitted.

        :param page: A Playwright browser page.
        """
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(f"{base_url}/text-box")
            user_form: ElementHandle = await page.wait_for_selector(
                "#userForm"
            )
            username_field: ElementHandle = await user_form.wait_for_selector(
                "#userName"
            )
            email_field: ElementHandle = await user_form.wait_for_selector(
                "#userEmail"
            )
            current_address_field: ElementHandle = (
                await user_form.wait_for_selector("#currentAddress")
            )
            permanent_address_field: ElementHandle = (
                await user_form.wait_for_selector("#permanentAddress")
            )

            await username_field.fill(self.user["name"])
            await email_field.fill(self.user["email"])
            await current_address_field.fill(self.user["currentAddress"])
            await permanent_address_field.fill(self.user["permanentAddress"])

            await page.click("#submit")

            output_field: ElementHandle = await page.wait_for_selector(
                "#output"
            )
            for key, value in self.user.items():
                ele_value: str = await output_field.eval_on_selector(
                    f"#{key}", "el => el.innerText"
                )
                assert value in ele_value

    async def test_error_when_invalid_email(self):
        """Test that invalid data may not be submitted.

        :param page: A Playwright browser page.
        """
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(f"{base_url}/text-box")
            user_form: ElementHandle = await page.wait_for_selector(
                "#userForm"
            )
            email_field: ElementHandle = await user_form.wait_for_selector(
                "#userEmail"
            )

            await email_field.fill("test")

            await page.click("#submit")

            email_class: str = await user_form.eval_on_selector(
                "#userEmail", "el => el.className"
            )
            assert "field-error" in email_class


@pytest.mark.asyncio
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
    async def test_click_types(self, button_type: fixture):
        """Test that specific click actions provide a result.

        :param button_type: A tuple containing click action and result.
        :param page: A Playwright browser page.
        """
        click_action, result = button_type

        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(f"{base_url}/buttons")

            if click_action == "Double Click":
                await page.dblclick("#doubleClickBtn")
            elif click_action == "Right Click":
                await page.click("#rightClickBtn", button="right")
            else:
                await page.click('button >> text="Click Me"')

            message: ElementHandle = await page.is_visible(f"#{result}")

            assert message
