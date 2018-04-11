clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

install-deps:
	pip install -U -r requirements.txt

flake:
	flake8 story_teller/

isort:  ## Check imports
	isort -rc story_teller/

lint: flake isort ## Run code lint

test: clean lint  ## Run tests
	pytest -x -v story_teller/

coverage: clean lint  ## Run coverage tests
	pytest -x -v story_teller/ \
		--cov=story_teller \
		--cov-report term \
		--cov-report html

coverage-browser: clean lint  ## Run coverage tests
	pytest -x -v story_teller/ \
		--cov=story_teller \
		--cov-report term \
		--cov-report html
	xdg-open htmlcov/index.html
