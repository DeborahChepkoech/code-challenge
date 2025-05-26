import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author

def test_create_magazine():
    mag = Magazine(name="New Magazine", category="Science")
    mag.save()
    assert mag.id is not None

def test_find_magazine_by_id():
    mag = Magazine(name="Find Magazine", category="Science")
    mag.save()
    found = Magazine.find_by_id(mag.id)
    assert found is not None
    assert found.name == "Find Magazine"

def test_find_magazine_by_name():
    mag = Magazine(name="Unique Mag", category="Science")
    mag.save()
    found = Magazine.find_by_name("Unique Mag")
    assert found is not None
    assert found.id == mag.id

def test_articles_and_contributors():
    author = Author(name="Contributor Author")
    author.save()

    mag = Magazine(name="Contributor Mag", category="Science")
    mag.save()

    article = author.add_article(mag, "Science Article")

    articles = mag.articles()
    assert len(articles) == 1
    assert articles[0].title == "Science Article"

    contributors = mag.contributors()
    assert any(c.name == "Contributor Author" for c in contributors)

def test_article_titles_and_contributing_authors():
    author = Author(name="Author A")
    author.save()
    mag = Magazine(name="Magazine A", category="Tech")
    mag.save()

    # Add multiple articles
    for i in range(3):
        author.add_article(mag, f"Article {i+1}")

    titles = mag.article_titles()
    assert len(titles) == 3
    assert "Article 1" in titles

    contributing_authors = mag.contributing_authors()
    assert any(c.name == "Author A" for c in contributing_authors)
