from flask import Flask, request, jsonify
import re
from send_message_date import send_quick_reply_start_date, send_quick_reply_end_date, send_quick_reply_select_data, send_quick_reply_select_job
from send_file_last_update import send_file_last_update
from send_file_hospital import send_file_hospital
from send_file_province import send_file_province
from send_file_service_area import send_file_service_area
from run_job import run_job
import requests
import json
import os

app = Flask(__name__)


user_state = {}

def select_date(user_id, text):
    if user_id not in user_state:
        user_status = user_state[user_id]

    user_status = user_state.get(user_id, {})

    if user_status.get("step") == "waiting_selected_table":
        if text in ["LastUpdate", "Hospital", "Province", "ServiceAreaHealth"]:
            user_status["selected_table"] = text
            send_quick_reply_start_date()
            user_status["step"] = "waiting_start_date"
            return jsonify({"status": "success", "message": "Waiting for start date"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid Table Selection"}),400

    elif user_status.get("step") == "waiting_start_date":
        if text:
            user_status["start_date"] = text
            send_quick_reply_end_date()
            user_state[user_id]["step"] = "waiting_end_date"
            return jsonify({"status": "success", "message": "Waiting for end date"}), 200
        else:
            return jsonify({"status": "error", "message": "Start date not received"}), 400
        
    elif user_status.get("step") == "waiting_end_date":
        if text:
            user_status["end_date"] = text
            selected_table = user_status["selected_table"]
            start_date = user_status["start_date"]
            end_date = user_status["end_date"]
            print("Current user_state:", user_state)
            user_state.pop(user_id)  
            
            if selected_table == "LastUpdate":
                send_file_last_update(start_date, end_date)
                return jsonify({
                    "status": "success",
                    "message": "Dates received",
                    "selected_table": selected_table,
                    "start_date": start_date,
                    "end_date": end_date
                }), 200
            elif selected_table == "Hospital":
                send_file_hospital(start_date, end_date)
                return jsonify({
                    "status": "success",
                    "message": "Dates received",
                    "selected_table": selected_table,
                    "start_date": start_date,
                    "end_date": end_date
                }), 200
            elif selected_table == "Province":
                send_file_province(start_date, end_date)
                return jsonify({
                    "status": "success",
                    "message": "Dates received",
                    "selected_table": selected_table,
                    "start_date": start_date,
                    "end_date": end_date
                }), 200
            elif selected_table == "ServiceAreaHealth":
                send_file_service_area(start_date, end_date)
                return jsonify({
                    "status": "success",
                    "message": "Dates received",
                    "selected_table": selected_table,
                    "start_date": start_date,
                    "end_date": end_date
                }), 200
            else:
                return jsonify({"status": "error", "message": "Invalid Table Selection"}), 400
        else:
            return jsonify({"status": "error", "message": "End date not received"}), 400

    else:
        return jsonify({"status": "error", "message": "Invalid state or no action required"}), 400
    
def select_job(user_id,text):
    
    success = run_job(text)

    if success:
        token = "A41118f4c3901504599cd424f489f0bc6f378f8f35e9b45c1b5b5a77d77e14635c345d3bb654c428fa7ac1aa7ddf7f8cc"
        url = "https://chat-api.one.th/message/api/v1/push_message"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}"
        }
        parameter = {
            "to" : "G2a371f7b1f7d4283b467ce1f94583300ab05b72bb0664ce5a239d9bb0787094f",
            #"to" : "Ua7c02205a2f24bf38244f22c27761fca",
            "bot_id" : "B334b547016f659f5b75ec45af18f3e38",
            "type" : "text",
            "message" : f'Start Run Job {text}',
            "custom_notification" : "เปิดอ่านข้อความใหม่จากทางเรา" 
        }
        response = requests.post(url, headers=headers, data= json.dumps(parameter))
        return jsonify({"status": "success", "message": f"Job '{text}' has been started"}), 200
    else:
        return jsonify({"status": "error", "message": f"Failed to start job '{text}'"}), 500

@app.route('/', methods=['POST'])
def webhook():
    try:
        # รับ JSON จาก request
        data = request.json
        # print(data)
        if not data:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400

        source = data.get('source',{})
        #sender = source.get('sender',{})
        user_id = source.get('user_id')
        if not user_id:
            return jsonify({"status": "error", "message": "User ID is missing"}), 400

        message = data.get('message', {})
        text = message.get('text', '')
        print(text)
        if re.search(r'run', text, re.IGNORECASE):  
            send_quick_reply_select_job()
            user_state[user_id] = {"step": "waiting_selected_job"}
            return jsonify({"status": "success", "message": "Waiting for job selection"}), 200
        
        elif re.search(r'select', text, re.IGNORECASE):  
            send_quick_reply_select_data()
            user_state[user_id] = {"step": "waiting_selected_table"}
            return jsonify({"status": "success", "message": "Waiting for table selection"}), 200    

        if user_id in user_state:
            user_status = user_state[user_id]
            if user_status.get("step") == "waiting_selected_job":
                return select_job(user_id, text)
            elif user_status.get("step") == "waiting_selected_table":
                return select_date(user_id, text)   
 
        return select_date(user_id, text)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "An error occurred"}), 500

if __name__ == '__main__':
    # ใช้ตัวแปร PORT หากมี หรือค่าเริ่มต้นเป็น 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)