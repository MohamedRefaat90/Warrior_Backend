cd /home/mohamedrefaat90/Warrior_Backend
git pull origin main
source /home/mohamedrefaat90/.virtualenvs/Warrior/bin/activate  # Activate virtual environment
pip freeze > requirements.txt
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
touch /var/www/mohamedrefaat90_pythonanywhere_com_wsgi.py  # Restart the app