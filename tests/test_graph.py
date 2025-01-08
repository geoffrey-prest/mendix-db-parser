import os
import sys
import unittest
import networkx as nx

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pathfinder')))

from graph import generate_from_relation_map

class TestGraph(unittest.TestCase):

    def test_generate_from_relation_map(self):
        relation_map = {
            'table1': [('intermediate1', 'table2')],
            'table3': [('intermediate2', 'table4')]
        }

        graph = generate_from_relation_map(relation_map)

        expected_edges = [
            ('table1', 'intermediate1'),
            ('intermediate1', 'table2'),
            ('table3', 'intermediate2'),
            ('intermediate2', 'table4')
        ]

        self.assertEqual(sorted(graph.edges()), sorted(expected_edges))
        self.assertTrue(nx.is_directed(graph))

if __name__ == '__main__':
    unittest.main()