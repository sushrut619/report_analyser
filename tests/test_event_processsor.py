"""Test suite for event processor"""
import unittest

from event_processor import parse_events

class TestEventProcessor(unittest.TestCase):
    """Unit tests for event processor"""
    def setUp(self) -> None:
        return super().setUp()
    
    def test_return_type(self):
        """Check if the function returns a list"""
        result = parse_events()
        self.assertTrue(isinstance(result, list))

