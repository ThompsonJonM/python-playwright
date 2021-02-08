from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class TextBox(Base):
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

    @property
    def submit_button(self) -> ElementHandle:
        return self.page.wait_for_selector("#submit")

    def fill_form(self, user: dict) -> None:
        """Fill out a Text Box page form.

        :param user: A test user.
        """
        self.username_field.fill(user["name"])
        self.email_field.fill(user["email"])
        self.current_address_field.fill(user["currentAddress"])
        self.permanent_address_field.fill(user["permanentAddress"])

    def navigate(self) -> None:
        """Navigate to the Text Box page."""
        self.page.goto(f"{self.base_url}/text-box")
