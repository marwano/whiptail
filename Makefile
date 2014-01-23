pep8:
	pep8 --filename=*.py --exclude=.tox,build

pyflakes:
	pyflakes *.py

audit: pep8 pyflakes

clean:
	rm -vfr dist *.egg-info *.pyc __pycache__ build .coverage htmlcov \
		testsuite/*.pyc testsuite/__pycache__

