from bs4 import BeautifulSoup

from locators.blog_locators import PostLocators


class BlogParser:
    def __init__(self, blog, topic_choice):
        self.soup = BeautifulSoup(str(blog), "html.parser")
        if topic_choice == "python":
            self.blog_topic = PostLocators.PYTHON
        elif topic_choice == "coding":
            self.blog_topic = PostLocators.CODING

    @property
    def parse_title(self):
        title = self.soup.select_one(self.blog_topic["BLOG_TITLE_LOCATOR"])
        return title

    @property
    def parse_content(self):
        content = self.soup.select_one(self.blog_topic["BLOG_CONTENT_LOCATOR"])

        return content

    @property
    def parse_posted_by(self):
        posted_by = self.soup.select_one(self.blog_topic["BLOGGER_LOCATOR"])

        return posted_by

    @property
    def parse_blog_time(self):
        time = self.soup.select_one(self.blog_topic["BLOG_TIME_LOCATOR"])
        return time

    @property
    def parse_blogger(self):
        blogger = self.soup.select_one(self.blog_topic["BLOGGER_LOCATOR"])

        return blogger

    @property
    def parse_tag(self):
        tag = self.soup.select_one(self.blog_topic["BLOG_TAG_LOCATOR"])
        return tag

    @property
    def parse_blog_img_link(self):
        blog_img_link = self.soup.select_one(self.blog_topic["BLOG_IMG_LOCATOR"])

        return blog_img_link

    # @property
    # def parse_blog_link(self):
    #     blog_link = self.soup.select_one(PostLocators.BLO)
    #     return blog_link

    @property
    def parse_read_time(self):
        read_time = self.soup.select_one(self.blog_topic["BLOG_READ_TIME_LENGTH_LOCATOR"])
        return read_time
