from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class Buttons(Base):
    @property
    def double_click_button(self) -> ElementHandle:
        return self.page.wait_for_selector("#doubleClickBtn")

    @property
    def right_click_button(self) -> ElementHandle:
        return self.page.wait_for_selector("#rightClickBtn")

    @property
    def dynamic_click_button(self) -> ElementHandle:
        return self.page.wait_for_selector('button >> text="Click Me"')

    def navigate(self) -> None:
        """Navigate to the Buttons page."""
        self.page.goto(f"{self.base_url}/buttons")
