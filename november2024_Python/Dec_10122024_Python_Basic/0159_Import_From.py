from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import stop_browser


class TestCase:
    def test_Case(self):
        start_browser()
        print("Hello Running TestCase")
        stop_browser()


obj_tc = TestCase()
obj_tc.test_Case()