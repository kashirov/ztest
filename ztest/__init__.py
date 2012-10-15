# -*- coding: utf-8 -*-
from unittest import TestCase


class ZTest(TestCase):

    def __init__(self, methodName='runTest'):
        TestCase.__init__(self, methodName=methodName)
        self.maxDiff = None
        self.eq = self.assertEqual
        self.neq = self.assertNotEqual

        self.true = self.assertTrue
        self.false = self.assertFalse

        self.isin = self.assertIn
        self.not_in = self.assertNotIn
        self.almost_eq = self.assertAlmostEqual