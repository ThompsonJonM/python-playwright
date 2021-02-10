from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class Books(Base):
    @property
    def books_container(self) -> ElementHandle:
        return self.page.wait_for_selector(".books-wrapper")

    @property
    def search_input(self) -> ElementHandle:
        return self.books_container.wait_for_selector("#searchBox")

    def book(self, title: str) -> ElementHandle:
        """Return a book link.

        :param title: The full title of the intended book.
        """
        return self.books_container.wait_for_selector(f"a >> text={title}")

    def navigate(self) -> None:
        """Navigate to the Books page."""
        self.page.goto(f"{self.base_url}/books")

    def search_for_book(self, title: str) -> None:
        """Search for a specific book.

        :param title: The full title of the intended book.
        """
        self.search_input.fill(title)
