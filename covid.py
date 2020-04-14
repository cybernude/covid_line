import requests
import schedule
import time

response = requests.get("https://covid19.th-stat.com/api/open/today")
data =  response.json()

def lineNotify():
    message = 'สถานการณ์การระบาดโควิด19ในประเทศไทย \n'\
    'ติดเชื้อสะสม : ' + str(data["Confirmed"]) + ' ราย\n'+'หายแล้ว : ' + str(data["Recovered"]) + ' ราย\n' \
                            'รักษาอยู่ใน รพ : ' + str(data["Hospitalized"]) + ' ราย\n' \
                            'ตายทั้งหมด : ' + str(data["Deaths"]) + ' ราย\n' \
                            'ตายเพิ่ม : ' + str(data["NewDeaths"]) + ' ราย\n' \
                            'ติดเชื่อเพิ่ม : ' + str(data["NewConfirmed"]) + ' ราย\n' \
                            'อัพเดทล่าสุด : ' + str(data["UpdateDate"]) + ' \n' \
                            'ข้อมูลจาก : https://covid19.th-stat.com/th (กรมควบคุมโรค)' 
    payload = {'message': message}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    # token = ''	#ญาติโก
    token = ''	#q รพ

    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

schedule.every().day.at("13:00").do(lineNotify)

while True:
    schedule.run_pending()
    time.sleep(1)


