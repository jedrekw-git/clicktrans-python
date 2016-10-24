from pages.page import Page

class BasePage(Page):

    _base_url = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/"

    @property
    def header(self):
        from pages.regions.header_region import HeaderRegion
        return HeaderRegion(self.get_driver())
