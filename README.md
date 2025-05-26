#  Code Challenge: Authors, Articles & Magazines (SQL + Python)

## Overview

This project models a publishing system using Python and raw SQL. It includes three primary classes:

- **Author**: Represents writers.
- **Magazine**: Represents publication platforms.
- **Article**: Connects Authors and Magazines through published work.

Each class is backed by an SQLite database with methods for querying and managing data.

---

## Project Structure

```plaintext
code-challenge/
├── lib/
│   ├── models/
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   ├── controllers/
│   └── debug.py
├── scripts/
│   ├── setup_db.py
│   └── run_queries.py
├── tests/
│   ├── test_author.py
│   ├── test_article.py
│   └── test_magazine.py
└── README.md
