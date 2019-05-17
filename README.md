export FLASK_APP=sniffer_api.py 
flask db init
flask db migrate
flask db update
flask run
