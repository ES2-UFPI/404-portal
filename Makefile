all: clean pyflakes

run:
	./manage.py runserver

pyflakes:
	find -L . -name "*.py" | grep -v __init__ | xargs pyflakes
migrate:
	./manage.py makemigrations
	./manage.py migrate
mm:
	django-admin makemessages -l pt_BR
cm:
	django-admin compilemessages
test:
	./manage.py test
clean:
	find . -name *.pyc | xargs rm -f
	find . -name __pycache__ | xargs rm -Rf
upgrade_pip:
	pip install -U pip
	cat requirements.txt | awk -F '=' '{print $$1}' | xargs pip install -U
