import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def clean_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Clear tables before each test
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    
    conn.commit()
    conn.close()
