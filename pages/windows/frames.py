from playwright.sync_api._generated import ElementHandle, Frame

from pages.base import Base


class Frames(Base):
    @property
    def container(self) -> ElementHandle:
        return self.page.wait_for_selector("#framesWrapper")

    @property
    def frame_one(self) -> Frame:
        return self.container.wait_for_selector("#frame1").content_frame()

    @property
    def frame_two(self) -> Frame:
        return self.container.wait_for_selector("#frame2").content_frame()

    def heading(self, frame: Frame) -> ElementHandle:
        """Return a heading for a specific frame.

        :param frame: A Playwright Frame object.
        """
        return frame.wait_for_selector("#sampleHeading")

    def navigate(self) -> None:
        """Navigate to the Frames page."""
        self.page.goto(f"{self.base_url}/frames")
