# Append to PYTHONPATH the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))

# Testing Framework
import unittest

# import factory
from counter.tests import CounterTest


if __name__ == '__main__':
    unittest.main()

