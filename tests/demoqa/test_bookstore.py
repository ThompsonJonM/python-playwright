import pytest

from credentials import user
from pages import Login, Profile


@pytest.mark.bookstore
class TestLogin:
    def test_valid_login(self, page) -> None:
        page.context.clear_cookies()
        login_page = Login(page)
        profile_page = Profile(page)

        login_page.navigate()
        login_page.fill_form(user)
        login_page.submit_button.click()

        visible: bool = profile_page.username_value_field.is_visible()

        assert "profile" in page.url and visible
