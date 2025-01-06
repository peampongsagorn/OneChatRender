import requests
#import pymssql
import json

def send_quick_reply_start_date():
    token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
    url ="https://chat-api.one.th/message/api/v1/push_quickreply"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    }

    parameter = {
        "to" : "G2a371f7b1f7d4283b467ce1f94583300ab05b72bb0664ce5a239d9bb0787094f",
        #"to" : "Ua7c02205a2f24bf38244f22c27761fca",
        "bot_id" : "B334b547016f659f5b75ec45af18f3e38",
        #"type" : "text",
        "message" : "Select Start Date",
        "quick_reply" : [
            {
        "label" : "เลือกวันที่เริ่มต้น",
        "type" : "datepicker",
        "min" : "2024-10-01",
        "initial" : "2018-01-24",
        "max" : "2025-02-28",
        "payload" : "meeting"
        }
        ],
        "custom_notification" : "เปิดอ่านข้อความใหม่จากทางเรา" 
    }
    response = requests.post(url, headers=headers, data= json.dumps(parameter))

def send_quick_reply_end_date():
    token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
    url ="https://chat-api.one.th/message/api/v1/push_quickreply"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    }

    parameter = {
        "to" : "G2a371f7b1f7d4283b467ce1f94583300ab05b72bb0664ce5a239d9bb0787094f",
        #"to" : "Ua7c02205a2f24bf38244f22c27761fca",
        "bot_id" : "B334b547016f659f5b75ec45af18f3e38",
        #"type" : "text",
        "message" : "Select End Date",
        "quick_reply" : [
            {
        "label" : "เลือกวันที่สิ้นสุด",
        "type" : "datepicker",
        "min" : "2024-10-01",
        "initial" : "2018-01-24",
        "max" : "2025-02-28",
        "payload" : "meeting"
        }
        ],
        "custom_notification" : "เปิดอ่านข้อความใหม่จากทางเรา" 
    }

    response = requests.post(url, headers=headers, data= json.dumps(parameter))


def send_quick_reply_select_data():
    token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
    url ="https://chat-api.one.th/message/api/v1/push_quickreply"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    }

    parameter = {
        "to" : "G2a371f7b1f7d4283b467ce1f94583300ab05b72bb0664ce5a239d9bb0787094f",
        #"to" : "Ua7c02205a2f24bf38244f22c27761fca",
        "bot_id" : "B334b547016f659f5b75ec45af18f3e38",
        #"type" : "text",
        "message" : "Select table",
        "quick_reply" : [
            {
        "label" : "LastUpdate",
        "type" : "text",
        "message" : "LastUpdate",
        "payload" : "table"
        },
           {
        "label" : "Hospital",
        "type" : "text",
        "message" : "Hospital",
        "payload" : "table"
        },
           {
        "label" : "Province",
        "type" : "text",
        "message" : "Province",
        "payload" : "table"
        },
           {
        "label" : "ServiceAreaHealth",
        "type" : "text",
        "message" : "ServiceAreaHealth",
        "payload" : "table"
        }
        ],
        "custom_notification" : "เปิดอ่านข้อความใหม่จากทางเรา" 
    }

    response = requests.post(url, headers=headers, data= json.dumps(parameter))

def send_quick_reply_select_job():
    token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
    url ="https://chat-api.one.th/message/api/v1/push_quickreply"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {token}"
    }

    parameter = {
        "to" : "G2a371f7b1f7d4283b467ce1f94583300ab05b72bb0664ce5a239d9bb0787094f",
        #"to" : "Ua7c02205a2f24bf38244f22c27761fca",
        "bot_id" : "B334b547016f659f5b75ec45af18f3e38",
        #"type" : "text",
        "message" : "Select table",
        "quick_reply" : [
            {
        "label" : "HealthIDMOPH_Test",
        "type" : "text",
        "message" : "HealthIDMOPH_Test",
        "payload" : "table"
        },
           {
        "label" : "HealthIDMOPH_Test_1",
        "type" : "text",
        "message" : "HealthIDMOPH_Test_1",
        "payload" : "table"
        },
           {
        "label" : "HealthIDMOPH_Test_2",
        "type" : "text",
        "message" : "HealthIDMOPH_Test_2",
        "payload" : "table"
        },
           {
        "label" : "HealthIDMOPH_Test_3",
        "type" : "text",
        "message" : "HealthIDMOPH_Test_3",
        "payload" : "table"
        }
        ],
        "custom_notification" : "เปิดอ่านข้อความใหม่จากทางเรา" 
    }

    response = requests.post(url, headers=headers, data= json.dumps(parameter))


    # response_text = response.text  # เก็บข้อความจาก response
    # try:
    #     decoded_response = json.loads(response_text)  
    #     print(f"Status: {response.status_code}, Response: {decoded_response}")
    # except json.JSONDecodeError as e:
    #     print(f"Status: {response.status_code}, Response: {response_text}")
    #     print(f"JSONDecodeError: {e}")


