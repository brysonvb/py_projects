import sys
from lib.config import AppConfig

print(__file__)


class Test:
    x = 0


print('__file__' in locals())
print('__file__' in globals())
print(hasattr(locals(), '__file__'))
print(hasattr(Test, 'x'))
a = Test()
a.y = "yes"
print(hasattr(a, 'y'))
print(getattr(a, 'x'))
print(sys.path)
