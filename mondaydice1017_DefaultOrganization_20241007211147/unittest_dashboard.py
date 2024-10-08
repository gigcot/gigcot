# python
'''
This file contains unit tests for the dashboard module.
'''
import unittest
from dashboard import Dashboard
class TestDashboard(unittest.TestCase):
    def test_init(self):
        # Arrange: Create a new dashboard instance with no initial value
        dashboard = Dashboard()
        # Act: Verify that the initial value is set to None by default
        self.assertIsNone(dashboard.initial_value)
    def test_set_initial_value(self):
        # Arrange: Create a new dashboard instance with an initial value
        dashboard = Dashboard()
        dashboard.set_initial_value(100)
        # Act: Verify that the initial value is set correctly
        self.assertEqual(dashboard.initial_value, 100)