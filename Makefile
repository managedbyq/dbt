.PHONY: install test test-unit test-integration

changed_tests := `git status --porcelain | grep '^\(M\| M\|A\| A\)' | awk '{ print $$2 }' | grep '\/test_[a-zA-Z_\-\.]\+.py'`

install:
	pip install -e .

test:
	@echo "Full test run starting..."
	@time docker-compose run test tox

test-unit:
	@echo "Unit test run starting..."
	@time docker-compose run test tox -e unit-py27,unit-py36,pep8

test-integration:
	@echo "Integration test run starting..."
	@time docker-compose run test tox -e integration-postgres-py27,integration-postgres-py36,integration-redshift-py27,integration-redshift-py36,integration-snowflake-py27,integration-snowflake-py36,integration-bigquery-py27,integration-bigquery-py36

test-quick:
	@echo "Integration test run starting..."
	@time docker-compose run test tox -e integration-postgres-py36 -- -x

clean:
	rm -f .coverage
	rm -rf .eggs/
	rm -rf .tox/
	rm -rf build/
	rm -rf dbt.egg-info/
	rm -f dbt_project.yml
	rm -rf dist/
	rm -f htmlcov/*.{css,html,js,json,png}
	rm -rf logs/
	rm -rf target/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -depth -delete
