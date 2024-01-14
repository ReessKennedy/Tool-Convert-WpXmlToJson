# Convert-WPXMLtoSimpleJSON

[Github link](https://github.com/ReessKennedy/Convert-WPXMLtoSimpleJSON)

## What ⚡
Simple python script to convert exports Wordpress XML into a simplified JSON file. 

See same before and after below. 
## Why 🤷‍♂️
I've tried many ways to handle this and most of the default XML to JSON conversion options create this huge JSON file that attempts to include all the meta from the Wordpress XML file. I just wanted a simplified version so I could export these Wordpress-based notes to text files or insert into a new database and I wanted to just specify that all I care to preserve is the creation date, content (title and content) and taxnomy info (catgeories and tags). I didn't create or attach featured images in this Wordpress instance so I skipped including these associations. 
## How 📋
If you need to do something like this too just edit the variable `wordpress_xml_file` in the script to hit your Wordpress export file and edit `output_json_file` to define where you want the new, simplified JSON to land. 
## Before and After 💫 🧹
This was from a log of business or product ideas I've had ... below is one idea that is supposed to be like a better Stackoverlow interface since I've often been annoyed looking for "the best" and thought a better system for vetting the best method or answering something can and should be designed. 
### Default as WP XML
```xml
	<item>
		<title>Being able to piece together pieces of code ...</title>
		<link>http://r.localhost.com/being-able-to-piece-together-pieces-of-code/</link>
		<pubDate>Sat, 01 Sep 2012 00:00:00 +0000</pubDate>
		<dc:creator><![CDATA[kennedrw]]></dc:creator>
		<guid isPermaLink="false">http://r.localhost.com/being-able-to-piece-together-pieces-of-code/</guid>
		<description></description>
		<content:encoded><![CDATA[Being able to piece together pieces of code to form things … a public repo and people vote on the best way to do things …]]></content:encoded>
		<excerpt:encoded><![CDATA[]]></excerpt:encoded>
		<wp:post_id>9698</wp:post_id>
		<wp:post_date><![CDATA[2012-09-01 00:00:00]]></wp:post_date>
		<wp:post_date_gmt><![CDATA[2012-09-01 00:00:00]]></wp:post_date_gmt>
		<wp:comment_status><![CDATA[open]]></wp:comment_status>
		<wp:ping_status><![CDATA[open]]></wp:ping_status>
		<wp:post_name><![CDATA[being-able-to-piece-together-pieces-of-code]]></wp:post_name>
		<wp:status><![CDATA[publish]]></wp:status>
		<wp:post_parent>0</wp:post_parent>
		<wp:menu_order>0</wp:menu_order>
		<wp:post_type><![CDATA[post]]></wp:post_type>
		<wp:post_password><![CDATA[]]></wp:post_password>
		<wp:is_sticky>0</wp:is_sticky>
		<category domain="category" nicename="business-ideas"><![CDATA[-business ideas]]></category>
		<category domain="post_tag" nicename="idea2"><![CDATA[-idea2]]></category>
		<category domain="post_tag" nicename="newlyaddedproductidea"><![CDATA[newlyaddedproductidea]]></category>
		<wp:postmeta>
			<wp:meta_key><![CDATA[note1]]></wp:meta_key>
			<wp:meta_value><![CDATA[]]></wp:meta_value>
		</wp:postmeta>
		<wp:postmeta>
			<wp:meta_key><![CDATA[note2]]></wp:meta_key>
			<wp:meta_value><![CDATA[]]></wp:meta_value>
		</wp:postmeta>
	</item>
```

### As Simplified JSON
```json
  {
    "title": "Being able to piece together pieces of code ...",
    "content": "Being able to piece together pieces of code to form things \u2026 a public repo and people vote on the best way to do things \u2026",
    "date_created": "Sat, 01 Sep 2012 00:00:00 +0000",
    "date_created_gmt": "2012-09-01 00:00:00",
    "taxonomies": [
      "-business ideas",
      "-idea2",
      "newlyaddedproductidea"
    ]
  },
```

