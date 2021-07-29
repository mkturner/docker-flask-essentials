from application import create_app as create_app_base

# import method to access current database
from mongoengine.connection import _get_db

# import testing framework
import unittest

# import model that we want to test
from counter.models import Counter

# import config data
from settings import MONGODB_HOST


# Create test as subclass of unittest
class CounterTest(unittest.TestCase):
    # Set up test factory
    def create_app(self):
        # name of database to use during test
        self.db_name = 'counter_test'

        # create app with project-specific config
        return create_app_base(
            MONGODB_SETTINGS={
                'DB': self.db_name,
                'HOST': MONGODB_HOST
            },
            TESTING=True,
            # Dont verify CSRF tokens
            WTF_CSRF_ENABLED=False,
            SECRET_KEY='',
        )

    # Run before every test
    def setUp(self) -> None:
        # Instantiate factory
        self.app_factory = self.create_app()
        # Use factory to instantiate test client
        self.app = self.app_factory.test_client()

    # Run after every test
    def tearDown(self) -> None:
        # get currently active db using imported method
        db = _get_db()
        db.client.drop_database(db)

    # the actual test case
    def test_counter(self):
        # Test if initial value == 1
        rv = self.app.get('/')
        assert '1' in str(rv.data)
        
        # Test if value increases properly
        rv = self.app.get('/')
        assert '2' in str(rv.data)
