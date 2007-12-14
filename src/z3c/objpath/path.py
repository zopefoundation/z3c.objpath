from zope.interface import implements
from z3c.objpath.interfaces import IObjectPath

class ObjectPath(object):
    """
    Implementation of IObjectPath.

    Applications can register this as a global (or local) utility. Libraries
    can then make use of this by looking up the utility.
    """
    implements(IObjectPath)

    def path(self, root, obj):
        steps = []
        orig_obj = obj
        while obj is not None:
            steps.append(obj.__name__)
            if obj is root:
                break
            obj = obj.__parent__
        else:
            raise ValueError("Cannot create path for %s" % orig_obj)
        steps.reverse()
        return '/' + '/'.join(steps)

    def resolve(self, root, path):
        steps = path.split('/')
        assert steps[0] == ''
        obj = root
        assert steps[1] == root.__name__
        steps = steps[2:]
        for step in steps:
            try:
                obj = obj[step]
            except KeyError:
                raise ValueError("Cannot resolve path %s" % path)
        return obj

        
