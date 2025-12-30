# This is a simple Article Website - EADD ASSIGNMENT 1 and 2.

## Follow these steps to run this application

1. git clone https://github.com/pokhrelyadav/Article-Website-Django.git
2. cd Article-Website-Django
3. cd 'MultiLayer App'
4. In windows: .venv/Scripts/activate and Linux/mac: source .venv/bin/activate or source .venv/Scripts/activate (if using git bash in windows)
5. pip install -r requirements.txt
6. Do 'ls' or 'dir' to see if manage.py exist. Run this below command on that level

Open two terminal in vs code and run these two separately:

python manage.py tailwind start
python manage.py runserver

This will run the main website.

To use api

1. Go to Multitier frontend folder
2. Open index.html and edit this port to match the port of backend you just run above in step 6.

const API_URL = "http://localhost:8000/api/v1/articles";

3. Do right click and 'Open with live server'
