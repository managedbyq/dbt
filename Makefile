.PHONY: install pep8 test test-unit test-integration

install:
	pip install -e .

pep8:
	@echo "PEP8 test run starting..."
	@time docker-compose run test tox -e pep8

test:
	@echo "Full test run starting..."
	@time docker-compose run test tox

test-unit:
	@echo "Unit test run starting..."
	@time docker-compose run test tox -e unit-py27,unit-py36,pep8

test-integration:
	@echo "Integration test run starting..."
	@time docker-compose run test tox -e integration-postgres-py27,integration-postgres-py36,integration-snowflake-py27,integration-snowflake-py36,integration-bigquery-py27,integration-bigquery-py36
