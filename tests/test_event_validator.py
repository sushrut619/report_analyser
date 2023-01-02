"""Test suite for event validator"""
import unittest

from event_validator import validate_event_type, validate_imei

class TestEventValidator(unittest.TestCase):
    """Unit tests for event validator"""
    def setUp(self) -> None:
        return super().setUp()

    def test_null_event_type(self):
        """Verify that null event type return false"""
        is_valid_event_type = validate_event_type("")
        self.assertEqual(is_valid_event_type, False)

    def test_valid_event_type(self):
        """Verify that valid event type returns result as true"""
        is_valid = validate_event_type("SEND")
        self.assertEqual(is_valid, True)

    def test_invalid_event_type(self):
        """Verify that invalid event type returns false"""
        is_valid = validate_event_type("TEST")
        self.assertEqual(is_valid, False)

    def test_null_imei(self):
        """Verify that null imei return false"""
        is_valid = validate_imei("")
        self.assertEqual(is_valid, False)

    def test_valid_imei(self):
        """Verify that valid imei returns True"""
        is_valid = validate_imei("490154203237518")
        self.assertEqual(is_valid, True)

    def test_invalid_imei(self):
        """Verify that invalid imei return False"""
        is_valid = validate_imei("490154203237517")
        self.assertEqual(is_valid, False)