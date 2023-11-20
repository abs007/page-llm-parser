import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

url = 'https://github.com/kaavee315'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# Dictionary storing tags and their associated attributes to keep
tags_to_store = {
    "table": ["class"],
    "input": ["class"],
    "turbo-frame": ["id"],
    "span": ["data-error-text", "data-success-text"],
    "div": ["class", "role"],
    "query-builder": ["class", "id"],
    "label": ["id", "style"],
    "svg": ["class"],
    "meta": ["name"],
    "tool-tip": ["data-type", "for"],
    "form": ["accept-charset", "id", "method"],
    "link": ["href", "type"],
    "qbsearch-input": ["class"],
    "modal-dialog": ["aria-labelledby", "aria-modal", "aria-describedby"],
    "button": ["aria-label", "class"],
    "h3": ["class", "id"],
    "nav": ["aria-label"],
    "img": ["class", "alt"],
    "details": ["class"],
    "a": ["aria-label", "href"]
}

# Dictionary storing tags to replace with new tags
tags_to_replace = {
    ("textarea", "input"): "<i>",
    ("div"): "<p>",
    ("svg", "img", "picture", "form"): "<img>"
}

# List of tags to remove from the HTML content
tags_to_remove = ["style", "span", "class", "circle",
    "meta", "head", "details-dialog", "path",
    "auto-check", "rect", "script", "ellipse"]


# Extracting specific content from table tags and counting occurrences
for table in soup("table"):
    counter = Counter()
    for thead in table('thead'):
        thead.decompose()
    
    for tbody in table('tbody'):
        for tr in tbody('tr'):
            for td in tr('td'):  
                if 'aria-describedby' in td.attrs:
                    counter[td['aria-describedby']] += 1
            tr.decompose()
        tbody.string = str([(k,v) for k,v in counter.items()])


# Function to keep specified attributes for specified tags
def keep_attributes(tags_to_store):
    for tag, attrs_to_keep in tags_to_store.items():
        tags = soup.find_all(tag)
        for tag in tags:
            attrs = list(tag.attrs.keys())
            for attr in attrs:
                if attr not in attrs_to_keep:
                    del tag[attr]


# Function to replace specified tags with new ones
def replace_tags(tags_to_replace, soup):
    for tags, new_tag in tags_to_replace.items():
        for tag in tags:
            for match in soup.find_all(tag):
                match.replace_with(BeautifulSoup(new_tag, 'html.parser'))


# Function to remove specified tags from the HTML content
def remove_tags(tags_to_remove, soup):
    for tag in tags_to_remove:
        for match in soup.find_all(tag):
            match.decompose()


keep_attributes(tags_to_store)
replace_tags(tags_to_replace, soup)
remove_tags(tags_to_remove, soup)

# Remove all ending tags
modified_html_str = re.sub(r'</\w+>', '', str(soup))
modified_html_str = re.sub(r'<\w+\/>', '', modified_html_str)


print(modified_html_str)
