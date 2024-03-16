from seleniumbase import BaseCase


class TestHome(BaseCase):

    def test_verify_page_title_and_url(self):
        self.open("https://practice-react.sdetunicorns.com/")

        # Assert url and title contains SDET Unicorns
        self.assert_url_contains('sdetunicorns')
        self.assert_title_contains('SDET Unicorns')


