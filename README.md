# python-abstract

## Python 2.7
```
python abstract_test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## Python 3.7
```
python3 abstract_test.py
..F
======================================================================
FAIL: test_raises_exception (__main__.TestAbstract)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "abstract_test.py", line 23, in test_raises_exception
    self.assertEqual(expected, actual)
AssertionError: "Can'[14 chars]abstract class Abstract with abstract methods say" != "Can'[14 chars]abstract class Abstract with abstract methods num_of_legs, say"
- Can't instantiate abstract class Abstract with abstract methods say
+ Can't instantiate abstract class Abstract with abstract methods num_of_legs, say
?                                                                 +++++++++++++


----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```
