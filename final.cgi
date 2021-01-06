#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    
    #Base query skeleton
    qry = """
          SELECT UCNE_id, name, UCRB, organism, chromosome, start, stop, length, identity
           FROM UCE
           WHERE 
    """
    
    #Series of statements to customize the query based on user inputs
    params = [] #this array will hold the params to feed to the placeholders
    if "UCNE_id" in form:
        qry += """UCNE_id = %s"""
        params.append(int(form.getvalue('UCNE_id')))
    if "UCNE_name" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """name LIKE %s"""
        params.append('%' + str(form.getvalue('UCNE_name')) + '%')
    if "UCRB" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """UCRB LIKE %s"""
        params.append('%' + str(form.getvalue('UCRB')) + '%')
    if "organism" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """organism = %s"""
        params.append(str(form.getvalue('organism')))
    if "chromosome" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """chromosome = %s"""
        params.append('%' + str(form.getvalue('chromosome')) + '%')
    if "chromosome_start" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """start >= %s"""
        params.append(int(form.getvalue('chromosome_start')))
    if "chromosome_stop" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """stop <= %s"""
        params.append(int(form.getvalue('chromosome_stop')))
    if "identity" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """identity >= %s"""
        params.append(float(form.getvalue('identity')))
    if "length" in form:
        if len(params)>0:
            qry += """ AND """
        qry += """length >= %s"""
        params.append(int(form.getvalue('length')))
    if len(params)==0:
        qry += """organism = %s"""
        params.append("human")
    
    #Insert SQL login info here
    conn = mysql.connector.connect(user='', password='', host='', database='')
    cursor = conn.cursor()
    
    cursor.execute(qry, tuple(params))

    #iterate over matches and format to json
    results = { 'match_count': 0, 'matches': list() }
    for (UCNE_id, name, UCRB, organism, chromosome, start, stop, length, identity) in cursor:
        results['matches'].append({'UCNE_id': int(UCNE_id), 'name': name, 'UCRB': UCRB, 'organism': organism, 'chromosome': chromosome, 'chr_start': int(start), 'chr_stop': int(stop), 'length': int(length) , 'identity': float(identity)})
        results['match_count'] += 1

    conn.close()

    print(json.dumps(results))

if __name__ == '__main__':
    main()