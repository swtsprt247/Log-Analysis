#! /usr/bin/env python
#python

import psycopg2
DBNAME = "news"
def run_query(query):
    # """Connects to the database, runs the query,
    # and returns the results"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows
    # except Exception as e:
    #     print(type(e))
    #     print("Database error: " + str(e))
    #     exit(1)


def get_top_articles():
    """Top 3 read articles"""

    query = """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """

    results = run_query(query)

    print('\nTop Three Articles:')
    count = 1
    for i in results:
        article = str(count) + '. "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(article + title + views)
        count += 1


def get_top_article_authors():
    """Top 3 popular authors"""

    query = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
    """

    results = run_query(query)

    print('\nTop Three Authors:')
    number = 1
    for i in results:
        print(str(number) + '. ' + i[0] + ' with ' + str(i[1]) + " views")
        number += 1


def get_days_with_errors():
    """Days with more than 1% errors"""

    query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM ( SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%' GROUP BY day) 
          AS errors
        JOIN ( SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log GROUP BY day) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > .01)
        ORDER BY percent DESC;
    """

    results = run_query(query)

    print('\nDays With More Than 1% Errors:')
    for x in results:
        date_time = x[0].strftime('%B %d, %Y')
        errors = str(round(x[1]*100, 1)) + "%" + " Errors!"
        print(date_time + " - " + errors)


print('Gathering Analysis...\n')
get_top_articles()
get_top_article_authors()
get_days_with_errors()
