from playwright.sync_api._generated import ElementHandle, Frame

from pages.base import Base


class NestedFrames(Base):
    @property
    def child_frame(self) -> Frame:
        return self.parent_frame.child_frames[0]

    @property
    def container(self) -> ElementHandle:
        return self.page.wait_for_selector("#framesWrapper")

    @property
    def heading(self) -> ElementHandle:
        return self.parent_frame.wait_for_selector("#sampleHeading")

    @property
    def parent_frame(self) -> Frame:
        return self.container.wait_for_selector("#frame1").content_frame()

    def navigate(self) -> None:
        """Navigate to the Frames page."""
        self.page.goto(f"{self.base_url}/nestedframes")
