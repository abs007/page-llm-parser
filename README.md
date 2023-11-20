# Web Scraping and HTML Modification Script

## Overview

This Python script performs web scraping on a specified GitHub profile page and modifies the HTML content by removing, replacing, and keeping specific HTML tags and their attributes.

## Language and Libraries

1. **Python** was chosen as it is a simple language with support for web scraping and also has useful libraries for parsing a html document

2. **BeautifulSoup:** was chosen for it providing a simple interface to parse the html document
3. **Requests:** was used for making HTTP requests to get the page content
4. **re** was used for data manipulation to change tag instances through regex

## Strategy

1. **Table data:** The table data present in the page was modified to keep count of the unique "aria-describedby" values alongside removing the thead tag in the table.
2. **Tag Removal:** Identified and removed specific HTML tags using `decompose()` method based on the provided `tags_to_remove` list.

3. **Tag Replacement:** Replaced selected tags with new tags according to the mappings specified in the `tags_to_replace` dictionary
4. **Attribute Preservation:** Retained specific attributes for specified tags from the HTML document as specified in the `tags_to_store` dictionary.
5. **Regex:** Used regex to replace all ending tags in the document with "</>" to signify a shorter closing tag

## Usage

To utilize this script:

1. Clone the repository.
2. Run `python3 main.py > out.html`
3. View the modified page contents in `out.html`

## Dependencies

- **Python 3:** [Link to Python](https://www.python.org/)
- **BeautifulSoup:** [Link to BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- **Requests:** [Link to Requests](https://docs.python-requests.org/)