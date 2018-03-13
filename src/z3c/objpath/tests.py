import doctest
import unittest


def test_suite():
    optionflags = (
        doctest.ELLIPSIS
        | doctest.REPORT_NDIFF
        | doctest.NORMALIZE_WHITESPACE
    )

    return unittest.TestSuite([
        doctest.DocFileSuite(
            'README.txt', optionflags=optionflags)
    ])
