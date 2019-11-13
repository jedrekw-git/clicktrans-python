from pages.page import Page

class BasePage(Page):

    _base_url = "https://www.gsmarena.com/"

    @property
    def header(self):
        from pages.regions.header_region import HeaderRegion
        return HeaderRegion(self.get_driver())
