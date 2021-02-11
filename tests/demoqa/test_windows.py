import pytest
from playwright.sync_api import Page
from playwright.sync_api._generated import ElementHandle
from pytest import fixture

from pages import BrowserWindows


@pytest.mark.browser_windows
@pytest.mark.windows
class TestBrowserWindows:
    def test_new_browser_window(self, page: Page) -> None:
        """Test that a new window may be opened.
        
        :param page: A Playwright browser page.
        """
        window_text: str = "This is a sample page"
        browser_windows: BrowserWindows = BrowserWindows(page)
        browser_windows.navigate()

        with page.context.expect_page() as window:
            browser_windows.window_button.click()

        new_window: Page = window.value
        heading: ElementHandle = new_window.wait_for_selector(
            "#sampleHeading"
        )
        visible: bool = heading.is_visible()
        text: str = heading.inner_text()

        assert visible and window_text in text
