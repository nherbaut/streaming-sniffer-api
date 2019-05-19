# Server Installation

## Devel

```bash
pip install Flask flask-cors flask-migrate flask-sqlalchemy
export FLASK_APP=sniffer_api.py 
flask db init
flask db migrate
flask db update
flask run
```

## Production

it should run as a WSGI app, behind https


# Chrome extension 

## Installation and execution steps

1. Get the latest extension release from [The release webpage](https://github.com/nherbaut/streaming-sniffer-api/releases/tag/0.0.1)
2. Download the crx file
3. Open the [extension page](chrome://extensions/) on chrome by typing the following address in a new tab: chrome://extensions/
4. drag and drop the crx file the extension page
5. accept the installation
6. go to youtube.com
7. while on youtube.com, a colored "streaming sniffer" icon should appear next to your address bar
8. while on youtube.com, click on the streaming sniffer icon
9. enter your email and press submit
10. while on youtube.com, click on the streaming sniffer icon AGAIN
11. Click on "Grab Streaming Info" to get the content id shown on the page
12. click on the "check your logs here" to see all the content ids collected for the email.