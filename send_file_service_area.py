import pandas as pd
import pymssql
import requests

def send_file_service_area(start_date, end_date):
    server = "192.168.132.43"
    user = "sa"
    password = "%6^QNu@#04"
    database = "HealthIDMoph_UAT"

    conn = pymssql.connect(server, user, password, database)
    cursor = conn.cursor()

    query = """
    SELECT 
    organization_code,
    name_health,
    service_area_health ,
    count_service_area_all ,
    count_service_area_otp ,
    count_service_area_idc ,
    date_cutoff
    FROM HealthIDMoph_UAT.dbo.ETL_HealthIDMoph_CountPersons_Cutoff_UAT
    WHERE cast(date_cutoff as date) BETWEEN %s AND %s
    """

    cursor.execute(query, (start_date, end_date))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    df_results = pd.DataFrame(results, columns=['organization_code', 'name_health', 'service_area_health', 'count_service_area_all',
                                                 'count_service_area_otp', 'count_service_area_idc', 'date_cutoff'])

    filename = f"HealthID_Count_ServiceArea_{start_date}_{end_date}.csv"
    
    df_results.to_csv(filename, index=False)
    print("บันทึกไฟล์เรียบร้อยแล้ว")

    token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
    url = "https://chat-api.one.th/message/api/v1/push_message"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # เปิดไฟล์ภายนอกบล็อก with เพื่อไม่ให้ไฟล์ถูกปิด
    with open(filename, "rb") as file:

        files = {
            'file': (filename, file, 'application/octet-stream')
        }
        data = {
            "to" : "G2a371f7b1f7d4283b467ce1f94583300ab05b72bb0664ce5a239d9bb0787094f",
            #"to" : "Ua7c02205a2f24bf38244f22c27761fca",
            "bot_id": "B334b547016f659f5b75ec45af18f3e38",
            "type": "file"
        }

        response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 200:
        print("ส่งไฟล์สำเร็จ")
    else:
        print(f"ไม่สามารถส่งไฟล์ได้ รหัสสถานะ: {response.status_code}")
        print(f"ข้อความตอบกลับ: {response.text}")


