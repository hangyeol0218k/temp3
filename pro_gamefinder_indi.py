import json
import requests
from prettytable import PrettyTable

Char_file = open("metadata/character.json", "r", encoding="UTF-8")
fPet_file = open("metadata/flyingPet.json", "r", encoding="UTF-8")
gType_file = open("metadata/gameType.json", "r", encoding="UTF-8")
Kart_file = open("metadata/kart.json", "r", encoding="UTF-8")
Pet_file = open("metadata/pet.json", "r", encoding="UTF-8")
Track_file = open("metadata/track.json", "r", encoding="UTF-8")
user_file=open("ID.json", "r", encoding="UTF-8")
IDlist_file=open("IDlist.json", "r", encoding="UTF-8")

Char_data = json.load(Char_file)
fPet_data = json.load(fPet_file)
gType_data = json.load(gType_file)
Kart_data = json.load(Kart_file)
Pet_data = json.load(Pet_file)
Track_data = json.load(Track_file)
user_data = json.load(user_file)
IDlist_data=json.load(IDlist_file)

def endday(month, year) :
    if month in [1, 3, 5, 7, 8, 10, 12] :
        return 31
    elif month in [4, 6, 9, 11] :
        return 30
    elif year%4==0 :
        if year%100>0 :
            return 29
    else :
        return 29
def same(var1, var2) :
    if var1==var2 :
        return 1
    else :
        return 0
def isprogame(res):
    cnt=0
    playercnt=0
    for player in range(0,8):
        try:
            if '/' in res['players'][player]['characterName'] :
                cnt+=1
            if '"' in res['players'][player]['characterName'] :
                cnt+=1
            playercnt+=1
        except:
            pass
    if cnt==playercnt:
        return True
    else:
        return False

def char_name(charid):
    try:
        for char in Char_data:
            if char['id'] == charid:
                return char['name']
    except:
        return "Error 0 : cannot find id"
def fPet_name(fPetid):
    try:
        for fPet in fPet_data:
            if fPet['id'] == fPetid:
                return fPet['name']
    except:
        return "Error 0 : cannot find id"
def gType_name(gTypeid):
    try:
        for gType in gType_data:
            if gType['id'] == gTypeid:
                return gType['name']
    except:
        return "Error 0 : cannot find id"
def kart_name(kartid) :
    try:
        for kartbody in Kart_data:
            if kartbody['id'] == kartid:
                return kartbody['name']
    except:
        return "Error 0 : cannot find id"
def pet_name(petid):
    try:
        for pet in Pet_data:
            if pet['id'] == petid:
                return pet['name']
    except:
        return "Error 0 : cannot find id"
def track_name(trackid):
    try:
        for track in Track_data:
            if track['id'] == trackid:
                return track['name']
    except:
        return "Error 0 : cannot find id"
def rank(num):
    if num=='99':
        return "retire"
    else :
        return num
def gType_id(gTypename):
    try:
        for gType in gType_data:
            if gType['name'] == gTypename:
                return gType['id']
    except:
        return "Error 1 : cannot find name"
def result(res):
    if res == '1':
        return '\033[30m'+'\033[48;5;178m'+'    1    '+'\033[0m'
    elif res == '2':
        return '\033[38;5;253m'+'\033[48;5;236m' '    2    ' + '\033[0m'
    elif res == '3':
        return '\033[38;5;253m'+'\033[48;5;160m'+ '    3    ' + '\033[0m'
    elif res == '4':
        return '\033[30m'+'\033[48;5;253m' + '    4    ' + '\033[0m'
    elif res == '5':
        return '\033[38;5;253m'+'\033[48;5;92m' + '    5    ' + '\033[0m'
    elif res == '6':
        return '\033[38;5;253m'+'\033[48;5;34m' + '    6    ' + '\033[0m'
    elif res == '7':
        return '\033[38;5;253m'+'\033[48;5;33m' + '    7    ' + '\033[0m'
    elif res == '8':
        return '\033[38;5;253m'+'\033[48;5;166m' + '    8    ' + '\033[0m'
    else :
        return '\033[38;5;246m' + " retired " + '\033[0m'

# 헤더파일에 인증키 필요, chorok307@naver.com 계정으로 발급받은 서비스 API Key
headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTg0NzUxOTE5IiwiYXV0aF9pZCI6IjQiLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4iLCJzZXJ2aWNlX2lkIjoiNDMwMDExMzkzIiwiWC1BcHAtUmF0ZS1MaW1pdCI6IjIwMDAwOjEwIiwibmJmIjoxNjM0NTY4MjU0LCJleHAiOjE2OTc2NDAyNTQsImlhdCI6MTYzNDU2ODI1NH0.2vdxwWQBrohBQzw7ybw-94VCrSJqsCIJaOGKkAuP5S4',
}

"""
ID_url = f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{nickname}"
ID_res = requests.get(ID_url, headers=headers)
access_id = ID_res.json()["accessId"]
"""

gamelist = []
year = 2021
for dlist in [1108] :
    month = dlist/100
    day = dlist%100
    for hour in range(11,14) :
        for min in range(0,60) :
            # 매치 리스트 조회에 필요한 변수
            start_date = '%04d-%02d-%02d %02d:%02d:00' % (year, month, day, hour, min)# 검색 시작 시간, yyyy-mm-dd hh-mm-ss (GMT)
            end_date = '%04d-%02d-%02d %02d:%02d:00' % (year, month+((min+1)/60)*((hour+1)/24)*same(day,endday(month,year)), (1-same(day,endday(month,year))*same(hour,23)*same(min,59))*(day+(same(min,59))*same(hour,23))+same(day,endday(month,year))*same(hour,23)*same(min,59), (hour+same(min,59))%24, (min+1)%60)# 검색 종료 시간, yyyy-mm-dd hh-mm-ss (GMT)
            print(start_date,end_date)
            offset = ''#input('offset? : ')  # 조회 오프셋
            limit = '500'#input('limit? : ')  # 조회 매치 수
            match_types_name = '스피드 개인전'#input('match_types? : ')
            match_types=gType_id(match_types_name)
            match_params = {
                'start_date': start_date,
                'end_date': end_date,
                'offset': offset,
                'limit': limit,
                'match_types': match_types
            }

            # 고유번호와 변수들로 매치 정보 받아오기
            all_match_url = f"https://api.nexon.co.kr/kart/v1.0/matches/all?start_date={match_params['start_date']}&end_date={match_params['end_date']}&offset={match_params['offset']} &limit={match_params['limit']}&match_types={match_params['match_types']}"
            all_match_res = requests.get(all_match_url, headers=headers, params=match_params)
            try :
                for match in all_match_res.json()['matches'][0]['matches'] :
                    #print(match, end = ' ')
                    #print(count, end=' ')
                    #print(len(gamelist))
                    match_id=match
                    match_find_url = f"https://api.nexon.co.kr/kart/v1.0/matches/{match_id}"
                    match_find_res = requests.get(match_find_url, headers=headers)
                    if match_find_res.json()["channelName"] =='speedIndiCombine':
                        if isprogame(match_find_res.json()):
                            print(match)
                            gamelist.append(match_id)
                            #print(match_id,'detected')
            except :
                pass
for game in gamelist :
        match_id=game
        match_find_url = f"https://api.nexon.co.kr/kart/v1.0/matches/{match_id}"
        match_find_res = requests.get(match_find_url, headers=headers)
        print('\n'+track_name(match_find_res.json()['trackId']),str(match_id))
        resulttable = PrettyTable(['Name', 'Kart', ' Rank '])
        resultlist=[]


        for player in range (0,8) :
            try:
                resultlist.append([match_find_res.json()["players"][player]["characterName"],
                                   kart_name(match_find_res.json()["players"][player]["kart"]),
                                   result(rank(match_find_res.json()["players"][player]["matchRank"])),
                                   rank(match_find_res.json()["players"][player]["matchRank"])
                                   ])
            except:
                pass
        for i in range(0,8) :
            for j in range (i+1,8):
                if resultlist[i][3]>resultlist[j][3] :
                    temp = resultlist[i]
                    resultlist[i] = resultlist[j]
                    resultlist[j] = temp
        for i in range(0,8):
            resulttable.add_row(resultlist[i][0:3])
        print(resulttable)
        print('')


Char_file.close()
fPet_file.close()
gType_file.close()
Kart_file.close()
Pet_file.close()
Track_file.close()