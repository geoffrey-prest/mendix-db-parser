import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pathfinder')))

from unittest.mock import patch, mock_open
from relations import generate_relation_map_from_sql, get_tables, get_table_for_column

class TestRelations(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    @patch('relations.get_tables')
    @patch('relations.os.listdir')
    @patch('relations.open', new_callable=mock_open, read_data='CREATE TABLE [dbo].[customermanagement$customer_review] ([customermanagement$customer] [int], [productmanagement$review] [int]);')
    def test_generate_relation_map_from_sql(self, mock_open, mock_listdir, mock_get_tables):
        mock_listdir.return_value = ['exampleTable.sql']
        mock_get_tables.return_value = {
            'customermanagement$customer': 'customermanagement$customer',
            'productmanagement$review': 'productmanagement$review'
        }

        expected_relation_map = {
            'customermanagement$customer': [('customermanagement$customer_review', 'productmanagement$review')],
            'productmanagement$review': [('customermanagement$customer_review', 'customermanagement$customer')]
        }

        relation_map = generate_relation_map_from_sql('doc/example/ddl')
        self.assertEqual(relation_map, expected_relation_map)

    def test_get_table_for_column(self):
        tables = {
            'customermanagement$customer': 'customermanagement$customer',
            'productmanagement$review': 'productmanagement$review'
        }
        self.assertEqual(get_table_for_column('customermanagement$customerid', tables), 'customermanagement$customer')
        self.assertEqual(get_table_for_column('productmanagement$reviewid', tables), 'productmanagement$review')

if __name__ == '__main__':
    unittest.main()