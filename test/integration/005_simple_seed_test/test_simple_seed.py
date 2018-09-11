from nose.plugins.attrib import attr
from test.integration.base import DBTIntegrationTest

class TestSimpleSeed(DBTIntegrationTest):

    def setUp(self):
        DBTIntegrationTest.setUp(self)

        self.run_sql_file("test/integration/005_simple_seed_test/seed.sql")

    @property
    def schema(self):
        return "simple_seed_005"

    @property
    def models(self):
        return "test/integration/005_simple_seed_test/models"

    @property
    def project_config(self):
        return {
            "data-paths": ['test/integration/005_simple_seed_test/data']
        }

    @attr(type='postgres')
    def test_simple_seed(self):
        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected")

        # this should truncate the seed_actual table, then re-insert
        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected")


    @attr(type='postgres')
    def test_simple_seed_with_drop(self):
        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected")

        # this should drop the seed table, then re-create
        results = self.run_dbt(["seed", "--drop-existing"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected")


class TestSimpleSeedCustomSchema(DBTIntegrationTest):

    def setUp(self):
        DBTIntegrationTest.setUp(self)
        self.run_sql_file("test/integration/005_simple_seed_test/seed.sql")

    @property
    def schema(self):
        return "simple_seed_005"

    @property
    def models(self):
        return "test/integration/005_simple_seed_test/models"

    @property
    def project_config(self):
        return {
            "data-paths": ['test/integration/005_simple_seed_test/data'],
            "seeds": {
                "schema": "custom_schema"
            }
        }

    @attr(type='postgres')
    def test_simple_seed_with_schema(self):
        schema_name = "{}_{}".format(self.unique_schema(), 'custom_schema')

        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected", table_a_schema=schema_name)

        # this should truncate the seed_actual table, then re-insert
        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected", table_a_schema=schema_name)


    @attr(type='postgres')
    def test_simple_seed_with_drop_and_schema(self):
        schema_name = "{}_{}".format(self.unique_schema(), 'custom_schema')

        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected", table_a_schema=schema_name)

        # this should drop the seed table, then re-create
        results = self.run_dbt(["seed", "--full-refresh"])
        self.assertEqual(len(results),  1)
        self.assertTablesEqual("seed_actual","seed_expected", table_a_schema=schema_name)


class TestSimpleSeedDisabled(DBTIntegrationTest):

    @property
    def schema(self):
        return "simple_seed_005"

    @property
    def models(self):
        return "test/integration/005_simple_seed_test/models"

    @property
    def project_config(self):
        return {
            "data-paths": ['test/integration/005_simple_seed_test/data-config'],
            "seeds": {
                "test": {
                    "seed_enabled": {
                        "enabled": True
                    },
                    "seed_disabled": {
                        "enabled": False
                    }
                }
            }
        }

    @attr(type='postgres')
    def test_simple_seed_with_disabled(self):
        results = self.run_dbt(["seed"])
        self.assertEqual(len(results),  1)
        self.assertTableDoesExist('seed_enabled')
        self.assertTableDoesNotExist('seed_disabled')
