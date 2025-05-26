import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_create_article():
    author = Author(name="Art Author")
    author.save()
    mag = Magazine(name="Art Mag", category="Lifestyle")
    mag.save()

    article = Article(title="New Article", author_id=author.id, magazine_id=mag.id)
    article.save()
    assert article.id is not None

def test_find_by_id_and_title():
    author = Author(name="Find Author")
    author.save()
    mag = Magazine(name="Find Mag", category="Lifestyle")
    mag.save()

    article = Article(title="Unique Title", author_id=author.id, magazine_id=mag.id)
    article.save()

    found_by_id = Article.find_by_id(article.id)
    assert found_by_id.title == "Unique Title"

    found_by_title = Article.find_by_title("Unique Title")
    assert found_by_title.id == article.id

def test_find_by_author_and_magazine():
    author = Author(name="Auth A")
    author.save()
    mag = Magazine(name="Mag A", category="Health")
    mag.save()

    # Add multiple articles
    for i in range(2):
        Article(title=f"Article {i+1}", author_id=author.id, magazine_id=mag.id).save()

    articles_by_author = Article.find_by_author(author.id)
    assert len(articles_by_author) == 2

    articles_by_magazine = Article.find_by_magazine(mag.id)
    assert len(articles_by_magazine) == 2
