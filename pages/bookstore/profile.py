from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class Profile(Base):
    @property
    def profile_container(self) -> ElementHandle:
        return self.page.wait_for_selector(".profile-wrapper")

    @property
    def username_value_field(self) -> ElementHandle:
        return self.profile_container.wait_for_selector("#userName-value")

    def navigate(self) -> None:
        self.page.goto(f"{self.base_url}/profile")
