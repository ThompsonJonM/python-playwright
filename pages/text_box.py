from playwright.sync_api._generated import ElementHandle

base_url: str = "https://www.demoqa.com"


class TextBoxPage(object):
    def __init__(self, page):
        self.page = page

    @property
    def user_form(self) -> ElementHandle:
        return self.page.wait_for_selector("#userForm")

    @property
    def username_field(self) -> ElementHandle:
        return self.user_form.wait_for_selector("#userName")

    @property
    def email_field(self) -> ElementHandle:
        return self.user_form.wait_for_selector("#userEmail")

    @property
    def current_address_field(self) -> ElementHandle:
        return self.user_form.wait_for_selector("#currentAddress")

    @property
    def permanent_address_field(self) -> ElementHandle:
        return self.user_form.wait_for_selector("#permanentAddress")

    def fill_form(self, user: dict) -> None:
        self.username_field.fill(user["name"])
        self.email_field.fill(user["email"])
        self.current_address_field.fill(user["currentAddress"])
        self.permanent_address_field.fill(user["permanentAddress"])

    def navigate(self) -> None:
        self.page.goto(f"{base_url}/text-box")
