import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from lib.models.author import Author

def test_create_author():
    author = Author(name="Test Author")
    author.save()
    assert author.id is not None

def test_find_author_by_id():
    author = Author(name="Find Me")
    author.save()
    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.name == "Find Me"

def test_find_author_by_name():
    author = Author(name="Unique Name")
    author.save()
    found = Author.find_by_name("Unique Name")
    assert found is not None
    assert found.id == author.id

def test_author_articles_and_magazines():
    from lib.models.magazine import Magazine

    author = Author(name="Article Author")
    author.save()

    mag = Magazine(name="Test Mag", category="Test")
    mag.save()

    article = author.add_article(mag, "Test Article")
    assert article.id is not None

    articles = author.articles()
    assert len(articles) == 1
    assert articles[0].title == "Test Article"

    mags = author.magazines()
    assert len(mags) == 1
    assert mags[0].name == "Test Mag"

def test_topic_areas():
    from lib.models.magazine import Magazine

    author = Author(name="Topic Author")
    author.save()

    mag1 = Magazine(name="Tech Mag", category="Tech")
    mag1.save()
    mag2 = Magazine(name="Health Mag", category="Health")
    mag2.save()

    author.add_article(mag1, "Tech Article")
    author.add_article(mag2, "Health Article")

    topics = author.topic_areas()
    assert "Tech" in topics
    assert "Health" in topics
