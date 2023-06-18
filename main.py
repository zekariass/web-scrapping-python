import pprint
import logging

from parsers.parser import Parser

logging.basicConfig(format="%(asctime)s %(levelname)-8s: [%(filename)s: %(lineno)s] %(message)s",
                    datefmt= "%Y:%m:%d %H:%M:%S",
                    filename="blog.log",
                    level=logging.DEBUG)
logger = logging.getLogger("medium_blog_logger")


TOPIC_CHOICE = """

            WELCOME TO MEDIUM BLOG INFO!
    ***********************************************
        You can see medium blogs summary, here.
    
            What topic are you looking for?
    ************************************************
    *   Press p or P to see Python related blogs,  *
    *   Press c or C to see coding blogs,          *
    ************************************************
    
    
"""

logger.info("Getting user choice, 'c' for coding, 'p' for python")
inp = input(TOPIC_CHOICE).lower()
logger.info(f"User choice accepted: {inp}")

topic_choice = {
    "p": "python",
    "c": "coding",
}

if __name__ == "__main__":
    logger.info("Creating main page parser....")
    page = Parser.page_parser(topic=topic_choice[inp])
    logger.info("Page parser created!")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(Parser.blog_parser(page, topic_choice[inp]))
