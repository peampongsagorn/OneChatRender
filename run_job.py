import pymssql
import re
import json

def run_job(job_name):
    try:
        server = "192.168.132.44"
        user = "sa"
        password = "Ny#Z!{o&p%>05"
        database = "msdb"
        conn = pymssql.connect(server, user, password, database)
        cursor = conn.cursor()

        cursor.execute("EXEC msdb.dbo.sp_start_job %s", job_name)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error running job: {e}")
        return False
    finally:
        cursor.close()
        conn.close()