from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class BrowserWindows(Base):
    @property
    def container(self) -> ElementHandle:
        return self.page.wait_for_selector("#browserWindows")

    @property
    def message_window_button(self) -> ElementHandle:
        return self.container.wait_for_selector("#messageWindowButton")

    @property
    def tab_button(self) -> ElementHandle:
        return self.container.wait_for_selector("#tabButton")

    @property
    def window_button(self) -> ElementHandle:
        return self.container.wait_for_selector("#windowButton")

    def navigate(self) -> None:
        """Navigate to the Browser Windows page."""
        self.page.goto(f"{self.base_url}/browser-windows")
