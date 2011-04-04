#!/usr/bin/env python
'''
>>> # Set up
>>> import functools
>>> curry = functools.partial
>>> def flip(f):
...   return lambda x, y: f(y, x)
>>> def safe_div(dividend, divisor):
...   if divisor == 0:
...     return Nothing
...   else:
...     return Just(dividend / divisor)
>>> safe_rdiv = flip(safe_div)

>>> # Typical usage
>>> Just(4) | curry(safe_rdiv, 2)
Just(2)
>>> Just(4) | curry(safe_rdiv, 2) | curry(safe_rdiv, 2)
Just(1)
>>> Just(4) | curry(safe_rdiv, 0)
Nothing
>>> Just(4) | curry(safe_rdiv, 0) | curry(safe_rdiv, 5)
Nothing

>>> # The monad laws
>>> # return a >>= f === f a
>>> `Just(8) | curry(safe_rdiv, 2)` == `curry(safe_rdiv, 2)(8)`
True
>>> # m >>= return === m
>>> `Just(3) | Just` == `Just(3)`
True
>>> # (m >>= f) >>= g === m >>= (\\x -> f x >>= g)
>>> f = curry(safe_rdiv, 2)
>>> g = curry(safe_rdiv, 3)
>>> `(Just(12) | f) | g` == `Just(12) | (lambda x: f(x) | g)`
True
'''

from monad import *

__all__ = ['Maybe', 'Just', 'Nothing']

class Maybe(Monad):
  def bind(self, a_to_m_b):
    if self is Nothing:
      return Nothing
    else:
      return a_to_m_b(self.value)

class Just(Maybe):
  def __repr__(self):
    return 'Just(%r)' % self.value

class Nothing(Maybe):
  def __repr__(self):
    return 'Nothing'
Nothing = Nothing(Nothing)




if __name__ == '__main__':
  import doctest
  doctest.testmod()
