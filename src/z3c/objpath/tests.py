from zope.interface.verify import verifyObject
import doctest
import unittest


class ObjectPathTests(unittest.TestCase):
    """Testing .path.*"""

    def test_module_provides_interface(self):
        from .interfaces import IObjectPath
        from . import _path
        self.assertTrue(verifyObject(IObjectPath, _path))


def test_suite():
    optionflags = (
        doctest.ELLIPSIS
        | doctest.REPORT_NDIFF
        | doctest.NORMALIZE_WHITESPACE
    )

    return unittest.TestSuite([
        unittest.makeSuite(ObjectPathTests),
        doctest.DocFileSuite(
            'README.rst', optionflags=optionflags)
    ])
