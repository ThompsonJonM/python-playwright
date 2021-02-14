import pytest
from playwright.sync_api import Page
from playwright.sync_api._generated import ElementHandle
from pytest import fixture

from pages import BrowserWindows, Frames, NestedFrames


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
        heading: ElementHandle = new_window.wait_for_selector("#sampleHeading")
        visible: bool = heading.is_visible()
        text: str = heading.inner_text()

        assert visible and window_text in text

    @pytest.mark.tab
    def test_new_browser_tab(self, page: Page) -> None:
        """Test that a new window may be opened.

        :param page: A Playwright browser page.
        """
        window_text: str = "This is a sample page"
        browser_windows: BrowserWindows = BrowserWindows(page)
        browser_windows.navigate()

        with page.context.expect_page() as window:
            browser_windows.tab_button.click()

        new_tab: Page = window.value
        heading: ElementHandle = new_tab.wait_for_selector("#sampleHeading")
        visible: bool = heading.is_visible()
        text: str = heading.inner_text()

        assert visible and window_text in text


@pytest.mark.frames
@pytest.mark.windows
class TestFrames:
    def test_first_frame(self, page: Page) -> None:
        """Test that a frame may be located.

        :param page: A Playwright browser page.
        """
        iframe_text: str = "This is a sample page"
        frames: Frames = Frames(page)
        frames.navigate()

        heading: ElementHandle = frames.heading(frames.frame_one)
        visible: bool = heading.is_visible()
        text: str = heading.inner_text()

        assert visible and iframe_text in text


@pytest.mark.nested_frames
@pytest.mark.windows
class TestNestedFrames:
    def test_child_frame(self, page: Page) -> None:
        """Test that a child frame may be located.

        :param page: A Playwright browser page.
        """
        iframe_text: str = "Child Iframe"
        nested_frames: NestedFrames = NestedFrames(page)
        nested_frames.navigate()

        body: ElementHandle = nested_frames.child_frame.wait_for_selector("p")
        visible: bool = body.is_visible()
        text: str = body.inner_text()

        assert visible and iframe_text in text
