import unittest
from test import test_support, string_tests


class StrTest(
    string_tests.CommonTest,
    string_tests.MixinStrUnicodeUserStringTest,
    string_tests.MixinStrUserStringTest
    ):

    type2test = str

    # We don't need to propagate to str
    def fixtype(self, obj):
        return obj

def test_main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StrTest))
    test_support.run_suite(suite)

if __name__ == "__main__":
    test_main()
