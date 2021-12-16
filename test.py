import unittest

import splitargs

class ArgumentSplitterTest(unittest.TestCase):
    def test_splitargs(self):
        assertions = [
            ("foo bar \"foo bar\"", ["foo", "bar", "foo bar"]),
            ("foo\"bar foo\"", ["foobar foo"]),
            ("foo bar\"foo bar\"foo bar", ["foo", "barfoo barfoo", "bar"]),
            ("foo bar\"foo \\\"bar\"foo bar", ["foo", "barfoo \"barfoo", "bar"])
        ]

        for val, args in assertions:
            self.assertEqual(splitargs(val), args)

if __name__ == '__main__':
    unittest.main()