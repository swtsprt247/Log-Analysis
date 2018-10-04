#! /usr/bin/env python
# coding: utf-8

import psycopg2
DBNAME = "news"


def get_data(query):
    # """Connects to the database, runs the query,
    # and returns the results"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def list_popular_articles():
    """ Display Popular Articles """ 
    query = """
    select title, count(*) as num
    from articles, log
    where log.path like '%' || articles.slug
    group by title
    order by num desc
    """
    results = get_data(query)[:3]
    print('⋅The Most Popular Three Articles of all time:')
    number = 1
    for record in results:
        print(str(number) + '. ' +'"{}" - {} views'.format(record[0], record[1]))
        number += 1


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
    """

    results = get_data(query)[:3]

    print('\nTop Three Popular Authors:')
    number = 1
    for record in results:
        print(str(number) + '. ' +'"{}" - {} views'.format(record[0], record[1]))
        number += 1


def get_days_with_errors():
    """Days with more than 1% errors"""

    query = """
            WITH num_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), num_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT num_requests.day,
                  num_errors.count::float / num_requests.count::float * 100
                  AS error_pc
                FROM num_requests, num_errors
                WHERE num_requests.day = num_errors.day
              )
            SELECT * FROM error_rate WHERE error_pc > 1;
    """

    results = get_data(query)

    print('\nDays With More Than 1% Errors:')
    for x in results:
        date_time = x[0].strftime('%B %d, %Y')
        errors = str(round(x[1]*100, 1)) + "%" + " Errors!"
        print(date_time + " - " + errors)


print('Gathering Analysis...\n')
list_popular_articles()
get_top_article_authors()
get_days_with_errors()
