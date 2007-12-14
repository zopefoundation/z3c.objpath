ObjectPath
==========

Let's get the ObjectPath object from somewhere. We could have it registered
as a utility and look it up that way, but in this case we'll just import
it and instantiate it::

  >>> from z3c.objpath.path import ObjectPath
  >>> objpath = ObjectPath()

We'll have a simple item::

  >>> class Item(object):
  ...   __name__ = None
  ...   __parent__ = None
  ...   def __repr__(self):
  ...     return '<Item %s>' % self.__name__

Let's create a simple container-like object::

  >>> class Container(Item):
  ...   def __init__(self):
  ...     self._d = {}
  ...   def __setitem__(self, name, obj):
  ...     self._d[name] = obj
  ...     obj.__name__ = name
  ...     obj.__parent__ = self
  ...   def __getitem__(self, name):
  ...     return self._d[name]
  ...   def __repr__(self):
  ...     return '<Container %s>' % self.__name__

Now let's create a structure::

  >>> root = Container()
  >>> root.__name__ = 'root'
  >>> data = root['data'] = Container()
  >>> a = data['a'] = Container()
  >>> b = data['b'] = Container()
  >>> c = data['c'] = Item()
  >>> d = a['d'] = Item()
  >>> e = a['e'] = Container()
  >>> f = e['f'] = Item()
  >>> g = b['g'] = Item()

We can create a path to ``a`` from ``root``::

  >>> objpath.path(root, a)
  '/root/data/a'

We can also resolve it again::

  >>> objpath.resolve(root, '/root/data/a')
  <Container a>

We can also create a path to ``a`` from ``data``::

  >>> objpath.path(data, a)
  '/data/a'

And resolve it again::

  >>> objpath.resolve(data, '/data/a')
  <Container a>

We can make a deeper path::

  >>> objpath.path(root, f)
  '/root/data/a/e/f'

And resolve it::

  >>> objpath.resolve(root, '/root/data/a/e/f')
  <Item f>

We get an error if we cannot construct a path::

  >>> objpath.path(e, a)
  Traceback (most recent call last):
   ...
  ValueError: Cannot create path for <Container a>

We also get an error if we cannot resolve a path::

  >>> objpath.resolve(root, '/root/data/a/f/e')
  Traceback (most recent call last):
   ...
  ValueError: Cannot resolve path /root/data/a/f/e
