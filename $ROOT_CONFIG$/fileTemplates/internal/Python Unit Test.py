"""
    $NAME
    ~~~~~~~~~~~~~~~~~~~~~~~

    Unit test cases for the :py:mod:'<TODO: insert module>' module.

    :copyright: (c) $YEAR by Evidera.
"""

__author__ = 'Andrew van Herick'

from hamcrest import *


class TestMyClass(object):
    """
    Unit test for :py:class:'MyClass'.
    
    TODO: Update class name in code and docstring.
    """

    ########################################
    # Static methods
    
    ########################################
    # Class methods
    
    # Class set up / tear down
    
    @classmethod
    def setup_class(cls):
        """
        Called before any of the other methods in this class.
        """
        # TODO: Needs implementation or delete if unnecessary
 
    @classmethod
    def teardown_class(cls):
        """
        Called after all of the other methods in this class.
        """
        # TODO: Needs implementation or delete if unnecessary

    ########################################
    # Instance methods
    
    def __init__(self):
        "Class initializer."
        pass
    
    # Instance set up / tear down
    
    def setup(self):
        """
        Called before each method in this class with a name of the form test_*().
        """
        # TODO: Needs implementation or delete if unnecessary
 
    def teardown(self):
        """
        Called after each method in this class with a name of the form test_*().
        """
        # TODO: Needs implementation or delete if unnecessary
 
    # Test cases
    
    def test_some_method(self):
        """
        Unit test case for :py:method:'<TODO: insert method>'.
        """
        # TODO:  Needs implementation
        assert_that(True, is_(False))
 