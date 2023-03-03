export DJANGO_SETTINGS_MODULE=config.settings.local

python3 -m venv venv
source venv/bin/activate

cd project
mkdir apps-static

pip3 install -r requirements.txt

python3 manage.py migrate --settings=config.settings.local
python3 manage.py loaddata ../fixtures/admin.json
python3 manage.py collectstatic --noinput