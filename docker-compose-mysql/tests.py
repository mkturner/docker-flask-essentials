# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))

# Testing Framework
import unittest

# Poject dependencies
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Project Files
from app import app, db

# add existig models so db.create_all() works
from counter.models import *


class CounterTest(unittest.TestCase):
    # SET UP: run before every test case
    def setUp(self) -> None:
        # Configuration
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DATABASE_NAME'] = 'testcounter'
        self.db_uri = 'mysql+pymysql://%s:%s@%s/' % (
            app.config['DB_USERNAME'],
            app.config['DB_PASSWORD'],
            app.config['DB_HOST']
        )
        app.config['SQLALCHEMY_DATABASE_URI'] = self.db_uri + app.config['DATABASE_NAME']
        
        # Create SQLAlchemy engine & connecgt to it
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()

        # Flush contents w/ initial commit
        conn.execute("commit")

        # Create test DB
        conn.execute("create database " + app.config['DATABASE_NAME'])

        # Create Tables
        db.create_all()

        # Close connection
        conn.close()

        # Define app as test_client
        self.app = app.test_client()

    # TEAR DOWN: run after every test case
    def tearDown(self) -> None:
        # Remove session, if one exists
        db.session.remove()

        # Create new connection, connect
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()

        # Flush database
        conn.execute("commit")

        # Drop database, Close Connection
        conn.execute("drop database " + app.config['DATABASE_NAME'])
        conn.close()

    # Actual test
    def test_counter(self) -> None:
        # Hit page, assert initialization
        req = self.app.get('/')
        assert '1' in str(req.data)

        # Ensure increment on next visit
        req = self.app.get('/')
        assert '2' in  str(req.data)

if __name__ == '__main__':
    unittest.main()

