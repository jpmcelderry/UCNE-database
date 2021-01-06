#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    chr = form.getvalue('term')
        
    #Insert SQL login info here
    conn = mysql.connector.connect(user='', password='', host='', database='')
    cursor = conn.cursor()
    
    qry = """
          SELECT DISTINCT chromosome
            FROM UCE
           WHERE chromosome LIKE %s
        LIMIT 0,5
	"""

    cursor.execute(qry, ('%' + str(chr) + '%', ))

    results = []
    for (chromosome) in cursor:
        results.append({'value': chromosome})

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()