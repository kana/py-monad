#!/usr/bin/env python

__all__ = ['Monad']

class Monad:
  def __init__(self, a):
    '''Haskell equivalent: return'''
    self.value = a
    return

  def bind(self, a_to_m_b):
    '''Haskell equivalent: (>>=) as function'''
    raise NotImplementedError

  def __or__(self, a_to_m_b):
    '''Haskell equivalent: (>>=) as operator'''
    return self.bind(a_to_m_b)




if __name__ == '__main__':
  import doctest
  doctest.testmod()
