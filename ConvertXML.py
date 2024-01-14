import xml.etree.ElementTree as ET
import json
from html import unescape

def parse_wordpress_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    posts = []

    ns = {'content': 'http://purl.org/rss/1.0/modules/content/',
          'wp': 'http://wordpress.org/export/1.2/'}

    for item in root.findall('.//item'):
        post = {}

        # Extract post title
        post['title'] = item.find('title').text

        # Extract post content
        content_encoded = item.find('.//content:encoded', ns)
        post['content'] = unescape(content_encoded.text) if content_encoded is not None and content_encoded.text is not None else ''

        # Extract date created
        post['date_created'] = item.find('pubDate').text

        # Extract date created GMT
        post_date_gmt = item.find('.//wp:post_date_gmt', ns)
        post['date_created_gmt'] = post_date_gmt.text if post_date_gmt is not None else ''

        # Extract taxonomies (categories and tags)
        taxonomies = []
        for category in item.findall('.//category[@domain="category"]'):
            taxonomies.append(category.text)

        for tag in item.findall('.//category[@domain="post_tag"]'):
            taxonomies.append(tag.text)

        post['taxonomies'] = taxonomies

        posts.append(post)

    return posts

def write_to_json(posts, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(posts, json_file, indent=2)

if __name__ == "__main__":
    wordpress_xml_file = "Files/wp.xml"
    output_json_file = "Files/simple.json"

    parsed_posts = parse_wordpress_xml(wordpress_xml_file)
    write_to_json(parsed_posts, output_json_file)

    print("Conversion completed. Posts saved to:", output_json_file)
