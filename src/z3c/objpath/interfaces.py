from zope.interface import Interface

class IObjectPath(Interface):
    """Path representation to objects.
    """

    def path(root, obj):
        """Give the path representation of obj relative to root.

        root - should be the root that the object is contained in.
        obj - object in a hierarchy of IContainer objects.

        The path is defined relatively to the root.

        Returns the path.
        
        If no path to the object can be made, raise a ValueError.
        """

    def resolve(root, path):
        """Given a path resolve it from root.

        root - should be the root that the object is contained in.
        path - a path to an object relative to the root.

        Returns the object that the path referred to.

        If the path cannot be resolved to an object, raise a ValueError.
        """

