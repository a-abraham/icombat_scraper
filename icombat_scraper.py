import os
import re
import argparse
import requests
from pprint import pprint
from lxml import html

parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="user", help="username",
                    action="store")

def get_content_tree(url):
    page = requests.get(url)
    return html.fromstring(page.content)

def get_quad_dicts(tree):
    #  <span class="quad-title">KDR:</span> <span class="quad-value">1.32</span>
    quad_keys = tree.xpath('//span[@class="quad-title"]/text()')
    quad_vals = tree.xpath('//span[@class="quad-value"]/text()')
    quad_dict = dict(zip(quad_keys, quad_vals))

    quad_sub_keys = tree.xpath('//span[@class="quad-sub-title"]/text()')
    quad_sub_vals = tree.xpath('//span[@class="quad-sub-value"]/text()')
    quad_sub_dict = dict(zip(quad_sub_keys, quad_sub_vals))

    return quad_dict, quad_sub_dict


def main():
    args = parser.parse_args()
    # verify args

    #temp URL for proof of concept
    url = 'http://barracks.icombat.com/Tactical/Player/Overview/1087815'

    # Open Google Doc
    # Create List with links
    # Open Each link
    tree = get_content_tree(url)
    # Populate info dicts
    quad_dict, quad_sub_dict = get_quad_dicts(tree)

    # Print important info for now
    print 'KDR: {0}\nMVPs: {1}\nScore / Min: {2}\n'.format(quad_dict['KDR:'], quad_sub_dict['MVPs:'], quad_dict["Score / Min:"])
    # Update Entries in Google Docs

if __name__ == '__main__':
    main()
