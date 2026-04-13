import psycopg2
conn = None
try:
    conn = psycopg2.connect(config)
    cur = conn.cursor()
    # execute 1st statement
    cur.execute(statement1)
    # execute 2nd statement
    cur.execute(statement2)
    # commit the transaction
    conn.commit()
    # close the cursor
    cur.close()
except psycopg2.DatabaseError as error:
    if conn:
       conn.rollback()
    print(error)
finally:
    if conn:
        conn.close()