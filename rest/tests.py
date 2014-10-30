from django.test import TestCase

import unittest
import doctest
from rest import views

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(views))
    return tests