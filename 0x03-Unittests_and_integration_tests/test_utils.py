#!/usr/bin/env python3
"""
Unit tests for the utils.access_nested_map function.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
            expected: The expected value to be returned by the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError for invalid inputs.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception).strip("'"), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """ get_json Test Class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test get_json function """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ test memoize test class """
    def test_memoize(self):
        """ test memoize method """
        class TestClass:
            """ Test class """
            def __init__(self):
                self.called = 0

            def a_method(self):
                """ """
                self.called += 1
                return 42

            @memoize
            def a_property(self):
                """ """
                return self.a_method()

        obj = TestClass()
        with patch.object(obj, 'a_method', side_effect=obj.a_method)\
                as mock_method:
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
            self.assertEqual(obj.called, 1)


if __name__ == '__main__':
    unittest.main()
