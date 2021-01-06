#!/usr/local/bin/python3

import cgi
import os
import mysql.connector

#Insert SQL login info here
conn = mysql.connector.connect(user='', password='', host='', database='')
cursor = conn.cursor()

hg19_UCE = open("hg19_UCNE_coord.bed",'r')
#hg19_cluster = open("hg19_clusters_coord.bed","r")
danRer7_UCE = open("danRer7_UCNE_orthologs.bed",'r')
#danRer7_cluster = open("danRer7_subclusters.bed","r")
mm10_UCE = open("mm10_UCNE_orthologs.bed",'r')
#mm10_cluster = open("mm10_subclusters.bed","r")

insertNRB = """INSERT INTO UCE (UCNE_id, name, organism, chromosome, start, stop, length, identity)
    VALUES (%s, %s, 'human', %s, %s, %s, %s, %s)
    """

insert = """INSERT INTO UCE (UCNE_id, name, UCRB, organism, chromosome, start, stop, length, identity)
    VALUES (%s, %s, %s, 'human', %s, %s, %s, %s, %s)
    """

for line in hg19_UCE:
    data = line.split()
    
    UCRB = data[3].split("_")[0]
    
    if "chr" in UCRB:
        cursor.execute(insertNRB, (data[4], data[3], data[0], data[1], data[2], abs(int(data[2])-int(data[1]))+1, 0.00))
    else:
        cursor.execute(insert, (data[4], data[3], UCRB, data[0], data[1], data[2], abs(int(data[2])-int(data[1]))+1, 0.00))
        
    print(data[3] + " added successfully")
   
insertNRB = """INSERT INTO UCE (UCNE_id, name, organism, chromosome, start, stop, length, identity)
    VALUES (%s, %s, 'zebrafish', %s, %s, %s, %s, %s)
    """

insert = """INSERT INTO UCE (UCNE_id, name, UCRB, organism, chromosome, start, stop, length, identity)
    VALUES (%s, %s, %s, 'zebrafish', %s, %s, %s, %s, %s)
    """

for line in danRer7_UCE:
    data = line.split(",")
    
    name= data[0] + '_' + data[3]
    UCRB = data[0].split("_")[0]
    
    if "chr" in UCRB:
        cursor.execute(insertNRB, (data[1], name, data[4], data[5], data[6], abs(int(data[6])-int(data[5]))+1, data[9]))
    else:
        cursor.execute(insert, (data[1], name, UCRB, data[4], data[5], data[6], abs(int(data[6])-int(data[5]))+1, data[9]))
    
    print(data[0] + " added successfully")

insertNRB = """INSERT INTO UCE (UCNE_id, name, organism, chromosome, start, stop, length, identity)
    VALUES (%s, %s, 'mouse', %s, %s, %s, %s, %s)
    """

insert = """INSERT INTO UCE (UCNE_id, name, UCRB, organism, chromosome, start, stop, length, identity)
    VALUES (%s, %s, %s, 'mouse', %s, %s, %s, %s, %s)
    """
    
for line in mm10_UCE:
    data = line.split()
    
    UCRB = data[0].split("_")[0]
    
    if "chr" in UCRB:
        cursor.execute(insertNRB, (data[1], data[0], data[3], data[4], data[5], abs(int(data[5])-int(data[4]))+1, data[8]))
    else:
        cursor.execute(insert, (data[1], data[0], UCRB, data[3], data[4], data[5], abs(int(data[5])-int(data[4]))+1, data[8]))
        
    print(data[0] + " added successfully")

conn.commit()