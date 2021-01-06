#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    UCRB = form.getvalue('term')
        
    #Insert SQL login info here
    conn = mysql.connector.connect(user='', password='', host='', database='')
    cursor = conn.cursor()
    
    qry = """
          SELECT DISTINCT UCRB
            FROM UCE
           WHERE UCRB LIKE %s
	   LIMIT 0,5
    """
    
    cursor.execute(qry, ('%' + str(UCRB) + '%', ))

    results = []
    for (UCRB) in cursor:
        results.append({'value': UCRB})

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()