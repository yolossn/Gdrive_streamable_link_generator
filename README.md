# Gdrive_streamable_link_generator
A python package to get streamable link of videos from google drive.The generated streamable links are supported by jwplayer,video tag etc.

## Requirements
	beautifulsoup4==4.6.x
	requests==2.18.x
	selenium==3.8.x

----------
## Usage
### Import
	from linkGenerator import getLinks
	links=getLinks(url)
Returns a dictionary.
### Command-line
	python3 linkGenerator.py url

----------
## License 
The MIT License (MIT)


