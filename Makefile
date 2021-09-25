clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

deploy:
	git push heroku master

migrate:
	heroku run --app olist-integration-models "./integration-models/manage.py migrate"

shell:
	heroku run --app olist-integration-models "./integration-models/manage.py shell"

config:
	heroku config -s --app olist-integration-models

logs:
	heroku logs --tail --app olist-integration-models

info:
	heroku info --app olist-integration-models

lint:
	pipenv run pre-commit run -a -v

test:
	pipenv run pytest -sx integration-models

runserver:
	pipenv run ./integration-models/manage.py runserver 0:8001

check-dead-fixtures:
	pipenv run pytest --dead-fixtures -x integration-models

pip-install:
	pipenv install --dev

pyformat:
	black .
