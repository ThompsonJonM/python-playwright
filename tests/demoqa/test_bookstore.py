import pytest
from playwright.sync_api import Page

from credentials import user
from pages import Books, Login, Profile


@pytest.mark.authentication
@pytest.mark.bookstore
class TestLogin:
    def test_valid_login(self, page: Page) -> None:
        """Login with valid credentials.

        :param page: A Playwright browser page.
        """
        page.context.clear_cookies()
        login_page = Login(page)
        profile_page = Profile(page)

        login_page.navigate()
        login_page.fill_form(user)
        login_page.submit_button.click()

        visible: bool = profile_page.username_value_field.is_visible()

        assert "profile" in page.url and visible


@pytest.mark.books
@pytest.mark.bookstore
class TestBooks:
    def test_view_a_book(self, page: Page) -> None:
        """Using a mock, ensure that a single book may be viewed.

        :param page: A Playwright browser page.
        """
        book_title: str = "Designing Evolvable Web APIs with ASP.NET"
        books_page = Books(page)
        page.route(
            "**/BookStore/v1/Books",
            lambda route: route.fulfill(path="./data/books.json"),
        )

        with page.expect_response("**/BookStore/v1/Books") as response:
            books_page.navigate()

        visible: bool = books_page.book(title=book_title).is_visible()

        assert visible and response.value.ok
