from nose.plugins.attrib import attr
from test.integration.base import DBTIntegrationTest

class TestVarcharWidening(DBTIntegrationTest):

    def setUp(self):
        pass

    @property
    def schema(self):
        return "varchar_widening_002"

    @property
    def models(self):
        return "test/integration/002_varchar_widening_test/models"

    @attr(type='postgres')
    def test__postgres__varchar_widening(self):
        self.use_profile('postgres')
        self.use_default_project()
        self.run_sql_file("test/integration/002_varchar_widening_test/seed.sql")

        results = self.run_dbt()
        self.assertEqual(len(results),  2)

        self.assertTablesEqual("seed","incremental")
        self.assertTablesEqual("seed","materialized")

        self.run_sql_file("test/integration/002_varchar_widening_test/update.sql")

        results = self.run_dbt()
        self.assertEqual(len(results),  2)

        self.assertTablesEqual("seed","incremental")
        self.assertTablesEqual("seed","materialized")

    @attr(type='snowflake')
    def test__snowflake__varchar_widening(self):
        self.use_profile('snowflake')
        self.use_default_project()
        self.run_sql_file("test/integration/002_varchar_widening_test/seed.sql")

        results = self.run_dbt()
        self.assertEqual(len(results),  2)

        self.assertManyTablesEqual(["SEED", "INCREMENTAL", "MATERIALIZED"])

        self.run_sql_file("test/integration/002_varchar_widening_test/update.sql")

        results = self.run_dbt()
        self.assertEqual(len(results),  2)

        self.assertManyTablesEqual(["SEED", "INCREMENTAL", "MATERIALIZED"])
