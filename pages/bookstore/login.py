from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class Login(Base):
    @property
    def password_field(self) -> ElementHandle:
        return self.userform.wait_for_selector("#password")

    @property
    def submit_button(self) -> ElementHandle:
        return self.userform.wait_for_selector("#login")

    @property
    def userform(self) -> ElementHandle:
        return self.page.wait_for_selector("#userForm")

    @property
    def username_field(self) -> ElementHandle:
        return self.userform.wait_for_selector("#userName")

    def fill_form(self, user: dict) -> None:
        """Fill out the login form.

        :param user: A user intended for login.
        """
        self.username_field.fill(user["userName"])
        self.password_field.fill(user["password"])

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/login")