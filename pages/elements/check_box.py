from playwright.sync_api._generated import ElementHandle

base_url: str = "https://www.demoqa.com"


class CheckBox(object):
    def __init__(self, page):
        self.page = page

    @property
    def check_box_container(self) -> ElementHandle:
        return self.page.wait_for_selector(".react-checkbox-tree")

    @property
    def check_box_list(self) -> ElementHandle:
        return self.check_box_container.wait_for_selector('.rct-node.rct-node-parent')

    @property
    def collapse_all_button(self) -> ElementHandle:
        return self.page.wait_for_selector("[title='Collapse all']")

    @property
    def expand_all_button(self) -> ElementHandle:
        return self.page.wait_for_selector("[title='Expand all']")

    @property
    def result_field(self) -> ElementHandle:
        return self.page.wait_for_selector("#result")

    def check_box(self, text: str) -> ElementHandle:
        """Select a checkbox based on a text node.
        
        :param text: The text for checkbox selection.
        """
        return self.check_box_list.wait_for_selector(f"[for='tree-node-{text}']")

    def navigate(self) -> None:
        """Navigate to the Check Box page."""
        self.page.goto(f"{base_url}/checkbox")
