from lib.db.connection import get_connection
from lib.models.magazine import Magazine

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name  # This calls the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            self._name = None
        elif not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        else:
            self._name = value.strip()

    def save(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if self.id:
                cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
            else:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
                self.id = cursor.lastrowid
            conn.commit()
        except Exception as e:
            print(f"Error saving author: {e}")
            raise
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(*row) if row else None

    def articles(self):
        """Return list of Article objects written by this author."""
        from lib.models.article import Article  # moved import here to avoid circular import
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in rows]

    def magazines(self):
        """Return list of distinct Magazine objects this author has articles in."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT m.id, m.name, m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        ''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(*row) for row in rows]

    def add_article(self, magazine, title):
        from lib.models.article import Article  # local import to avoid circular import
        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    def topic_areas(self):
        """Return distinct categories of magazines where this author has articles."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        ''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows]
