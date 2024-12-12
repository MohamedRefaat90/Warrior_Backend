cd /home/mohamedrefaat90/Warrior_Backend  
git pull origin main
source /home/mohamedrefaat90/.virtualenvs/Warrior/bin/activate  # Activate virtual environment
pip install -r requirements.txt             
python manage.py makemigrations                    
python manage.py migrate                     
python manage.py collectstatic --noinput    # Collect static files
touch /var/www/your_pythonanywhere_username_wsgi.py  # Restart the app