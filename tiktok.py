import requests, os
import requests, json, time, datetime, html, re
class OOP:
    def __init__(self, TDS_token, tiktokID):
        self.TDS_token = TDS_token
        self.tiktokID = tiktokID
        self.demNV = 0
        self.xuHienTai = 0
        self.STT = 0
        self.s = requests.Session()
    def layThongTinAcc(self):
        url = 'https://traodoisub.com/api/?fields=profile&access_token={0}'.format(self.TDS_token)
        response = self.s.get(url)
        dataLTT =  json.loads(response.text)
        if('error' in dataLTT):
            print('Token tds die !!!')
            exit()
        else:
            user = dataLTT['data']['user']
            xu = dataLTT['data']['xu']
            xudie = dataLTT['data']['xudie']
            self.xuHienTai += int(xu)
            print(f'User : {user} | Xu : {xu} | Xu die : {xudie}')
    def datCauHinh(self):
        url = 'https://traodoisub.com/api/?fields=tiktok_run&id={0}&access_token={1}'.format(self.tiktokID, self.TDS_token)
        response = self.s.get(url)
        dataDCH = json.loads(response.text)
        if('error' in dataDCH):
            print('Kiểm tra lại xem cấu hình tiktok chưa')
            exit()
        else:
            id = dataDCH['data']['id']
            user = dataDCH['data']['uniqueID']
            msg = dataDCH['data']['msg']
            print(f'{id} | {user} | {msg}')
    def layNhiemVu(self):
        while(True):
            url = 'https://traodoisub.com/api/?fields=tiktok_follow&access_token={}'.format(self.TDS_token)
            response = self.s.get(url)
            try:
                data = json.loads(response.text)
                if 'countdown' in data:
                        countdown_value = data['countdown']
                        for i in range(int(countdown_value) + 5, 0, -1):
                            print(f'Thao tác quá nhanh vui lòng chậm lại, đợi {i} giây', end='\r')
                            time.sleep(1)
                        print(" " * 50, end='\r')
                elif 'time_reset' in data:
                    print('Đổi tiktok mới, bị giới hạn nhiệm vụ rồi')
                    exit()
                else:
                    for item in data['data']:
                        link_value = item['link']
                        id_value = item['id']
                        self.guiNhiemVu(id_value)
                        time.sleep(3)
                        self.follow(link_value)
                        self.demNV += 1
                        if self.demNV == 9:
                            self.nhanXu()
                            self.demNV = 0
                            continue
                        # for i in range(len(arr_link_value)):
                        #     link_value = arr_link_value[i]
                        #     print(link_value)
                            # id_value = arr_id_value[i]
                            # self.guiNhiemVu(id_value)
                            # time.sleep(5)
                            # self.follow(link_value)

            except json.JSONDecodeError:
                print("Error decoding JSON response.")
    def guiNhiemVu(self, id_value):
        url = 'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={0}&access_token={1}'.format(id_value, self.TDS_token)
        response = self.s.get(url)
        dataGNV = response.json()
        
        # for i in range(1, dataGNV['cache'] + 1):
        #     self.demNV += 1
        #     if self.demNV == 9:
        #         self.nhanXu()
        #         self.demNV = 0
        #         continue
    def follow(self, link_value):
       os.system(f'termux-open-url {link_value}')
    def nhanXu(self):
        url = 'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={}'.format(self.TDS_token)
        response = self.s.get(url)
        dataNX = response.json()
        if response.status_code == 200:
            if 'data' in dataNX:
                xu = dataNX['data']['xu']
                job_success = dataNX['data']['job_success']
                xuthem = dataNX['data']['xu_them']
                msg = dataNX['data']['msg']
                xuTong = int(re.search(r'\d+', msg).group())
                self.xuHienTai += xuTong
                self.STT+= 1
                print(f"[{self.STT}] | {job_success} | {xuthem} | {msg} | {xuTong} | Xu hiện tại : {self.xuHienTai}")
            else:
                print("eror")
        else:
            print(f"Yêu cầu không thành công. Mã trạng thái: {response.status_code}")
# os.system('termux-open-url https:\/\/tiktok.com\/@nguyenngocquang004')
TDS_token = 'TDSQfikjclZXZzJiOiIXZ2V2ciwiIxETMxgmbhhGdpFGZiojIyV2c1Jye'
tiktokID = '7170579645727867931'
api = OOP(TDS_token, tiktokID)
api.datCauHinh()
api.layNhiemVu()
