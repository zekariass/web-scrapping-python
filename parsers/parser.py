from parsers.page_parser import PageParser
from parsers.blog_parser import BlogParser

import logging


class Parser:
    logger =  logging.getLogger("medium_blog_logger.parser")
    @staticmethod
    def page_parser(tag="", topic="python"):
        Parser.logger.info("Create page parser by passing tag and topic values")
        page_parser = PageParser(tag, topic)
        Parser.logger.info("Parse the retrieved page")
        parsed_page = page_parser.parse_page()
        return parsed_page

    @staticmethod
    def blog_parser(parsed_page, topic_choice):
        Parser.logger.info("Check is parsed page is not none")
        if parsed_page:
            blogs = []

            for b in parsed_page:
                blog_parser = BlogParser(b,topic_choice)
                title_el = blog_parser.parse_title
                Parser.logger.info(f"Parsing blog with title '{title_el.string.strip()}'")
                if title_el:
                    content_el = blog_parser.parse_content
                    time_el = blog_parser.parse_read_time
                    tag_el = blog_parser.parse_tag
                    # blog_time_el = blog_parser.parse_blog_time
                    posted_by_el = blog_parser.parse_posted_by
                    blog_img_el = blog_parser.parse_blog_img_link
                    blogs.append({"title": title_el.string.strip(),
                                  "content": content_el.string,
                                  "read_time": time_el.string,
                                  "tag": tag_el.string,
                                  # "blog_time": blog_time_el.string,
                                  "posted_by": posted_by_el.string,
                                  "blog_image": blog_img_el.attrs["src"]}) if blog_img_el else None
            return blogs
        return None

