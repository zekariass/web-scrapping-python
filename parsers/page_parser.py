import requests
import logging

from pages.site import SiteLocator
from bs4 import BeautifulSoup
from locators.page_locator import PageLocator


class PageParser:

    logger = logging.getLogger("medium_blog_logger.page_parser")

    def __init__(self, tag, topic):
        self.root_site_locator = SiteLocator(tag, topic)
        self.site = self.root_site_locator.target_url

    def parse_page(self):
        PageParser.logger.info(f"Getting the page from {self.site}")
        html_string = requests.get(self.site)
        PageParser.logger.info("Creating a BeautifulSoup object to parse the page HTML tags")
        soup = BeautifulSoup(html_string.content, "html.parser")
        return soup.select(PageLocator.TOP_LOCATOR)




