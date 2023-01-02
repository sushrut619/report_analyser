"""Test suite for fault code lister function"""
import unittest
import enum

from fault_codes_lister import fault_codes_lister
from report_parser import read_file, parse_lines, build_word_matrix

class TestFaultCodesLister(unittest.TestCase):
    """Unittests for fault code lister function"""
    def setUp(self) -> None:
        # path is relative to home(root) folder
        self.test_data = read_file("./tests/test_input1.txt")
        self.test_lines = parse_lines(self.test_data)
        self.word_matrix = build_word_matrix(self.test_lines)
        # print("test data: ", self.test_data)
        return super().setUp()

    def test_return_type(self):
        """test return type is enum"""
        fault_code_list = fault_codes_lister("")
        self.assertTrue(isinstance(fault_code_list, enum.EnumType))

    def test_all_fault_codes_present(self):
        """Check that all the fault codes are listed"""
        fault_codes_list = fault_codes_lister(self.word_matrix)
        self.assertEqual(len(fault_codes_list), 3)
