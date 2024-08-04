import requests
import json
import random
import string
from api.proxy import WorkingProxy
import json
import time
import os 
import base64
from faker import Faker
fake = Faker()

def update():
    pass

def Ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def ip_list(num_ips):
  return ", ".join(Ip() for _ in range(num_ips))

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
    "Mozilla/5.3 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.2 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/4.3 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/2.2 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/3.2 (Macintosh; Intel Mac OS X 10_15_7) Gecko/20100101 Firefox/88.0",
    "Mozilla/3.5 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.5 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/90.0.818.49",
    "Mozilla/1.2 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.2 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.4 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/6.8 (Linux; Android 11; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/2.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    "Mozilla/23.3 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/4.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; U; Android 10; en-us; SM-G960U Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
    "Mozilla/3.0 (iPad; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
]


sec_ch_ua_list = [
    '"Mozilla Firefox";v="89", "(Not; A Brand";v="99", "Google Chrome";v="90"',
    '"Apple Safari";v="15", "(Not; A Brand";v="99", "Microsoft Edge";v="91"',
    '"Opera";v="77", "(Not; A Brand";v="99", "Blink";v="110"',
    '"Chromium";v="105", "(Not; A Brand";v="99", "Vivaldi";v="5.4"',
    '"Brave";v="1", "(Not; A Brand";v="99", "Blink";v="110"',
    '"SeaMonkey";v="2.53", "(Not; A Brand";v="99", "Gecko";v="20100101"',
    '"K-Meleon";v="5.4", "(Not; A Brand";v="99", "Gecko";v="20100101"',
    '"Midori";v="0.5.13", "(Not; A Brand";v="99", "WebKit";v="537.36"',
    '"Dillo";v="3.0.5", "(Not; A Brand";v="99", "Presto";v="2.12.388"',
    '"Arora";v="27.1.152", "(Not; A Brand";v="99", "Blink";v="110"'
]

sec_ch_ua_platform_list = [
    "Android",
    "Chrome OS",
    "Fuchsia",
    "iOS",
    "Linux",
    "macOS",
    "Windows",
    "Unknown",
    "Android",
    "Windows"
]
def random_os():
    os_list = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 6.1; WOW64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "iPhone; CPU iPhone OS 13_5 like Mac OS X",
        "Android 10; Mobile"
    ]
    return random.choice(os_list)
def random_browser():
    browsers = [fake.chrome, fake.firefox, fake.safari, fake.opera]
    return random.choice(browsers)()

styles={
    'Comics': {
        'stylePrompt': ' ,comics, comics art, American comics, comics styles, professional comics art, wonderful comics',
        'styleNegative': ' , Realistic, 3d, Ultra Realistic, Ugly, Blurry, Destroyed, Unprofessional'
    },
    'Fantasy': {
        "styleNegative" : ' ,(bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities:1.3),poorly drawn,deformed hands,deformed fingers,deformed faces,deformed eyes,mutated fingers,deformedbody parts,mutated body parts,mutated hands, disfigured,oversaturated,bad anatom,cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, deformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,deformed eyes',
        "stylePrompt" : " ,ethereal fantasy concept art . magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy"
    },
    'Cinematic' : {
        "styleNegative" : ' ,(bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities:1.3),poorly drawn,deformed hands,deformed fingers,deformed faces,deformed eyes,mutated fingers,deformedbody parts,mutated body parts,mutated hands, disfigured,oversaturated,bad anatom,cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, deformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,deformed eyes',
        "stylePrompt" : " ,cinematic film still. shallow depth of field, vignette, highly detailed, high budget, cinemascope, moody, epic, gorgeous, film grain, grainy"  
    },
    'Photography': {
        "stylePrompt" : ' , realistic photo 35mm photograph, film, professional, 4k, highly detailed',
        "styleNegative" : ' ,(bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities:1.3),poorly drawn,deformed hands,deformed fingers,deformed faces,deformed eyes,mutated fingers,deformedbody parts,mutated body parts,mutated hands, disfigured,oversaturated,bad anatom,cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, deformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,deformed eyes'
    },
    'Cartoon': {
        "stylePrompt" : ' , cartoon, 2d cartoon, cartoon art, cartoon drawing, high quality cartoon',
        "styleNegative" : ' , Realistic, 3d, Ultra Realistic, Real Image, Ugly, Low Quality'

    },
    'No' : {
        'stylePrompt': '',
        'styleNegative': ''
    },
    '3d': {
        'stylePrompt': ', 3d cartoon, 3d model, 3d style, 3d, high quality',
        'styleNegative': ', 2d'
    },
    'Anime': {
        'stylePrompt': ' ,Anime style ,vibrant colors, dynamic colors, anime , high quality, cartoony',
        'styleNegative': ' ,realistic ,(bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities:1.3),poorly drawn,deformed hands,deformed fingers,deformed faces,deformed eyes,mutated fingers,deformedbody parts,mutated body parts,mutated hands, disfigured,oversaturated,bad anatom,cropped, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, deformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,deformed eyes'
    }
}




def Headers(origin):
    ip = Ip()
    headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": origin,
        "Referer": f"{origin}/",
        "Sec-CH-UA": random_browser(),
        "Sec-CH-UA-Platform": random_browser(),
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": random.choice(user_agents),
        "Device": random.choice(sec_ch_ua_platform_list),
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
        "Cookie": "",
        "Cookies": None,
        "X-Forwarded-For": ip_list(3),
        "X-Real-IP": ip,
        "X-Client-IP": ip,
        "X-Forwarded": ip,
        "Forwarded-For": ip,
        "Forwarded": ip,
        "X-Cluster-Client-IP": ip,
        "Client-IP": ip,
        "CF-Connecting-IP": ip,
        "True-Client-IP": ip,
        "Sec-CH-UA-Mobile": "?0"
    }
    return headers




    
def rvx(prompt, negative='', width=1024, height=1024, scale=7, steps=20, style='Cinematic', shash='wefewjdi'):
    try:
        prompt += styles[style]['stylePrompt']
        negative += styles[style]['styleNegative']
    except (KeyError, IndexError):
        yield {'progress': 'style not found!'}
        
        return
    steps = min(int(steps), 50)
    proxy = WorkingProxy()
    sess_hash =  ''.join(random.choices(string.ascii_letters, k=11))

    proxy_config = {'http': proxy, 'https': proxy}
    data_payload = {
        "data": [prompt, negative, random.randint(0, 10000), width, height, scale, steps, "DPM++ 2M SDE Karras", "Custom", False, 0.55, 1.5],
        "event_data": None,
        "fn_index": 9,
        "trigger_id": 7,
        "session_hash": sess_hash,
        
    }
    headers = Headers(origin="https://artificialguybr-realvisxl-free-demo.hf.space")
    try:
        session = requests.Session()
        ini = session.post(
            'https://artificialguybr-realvisxl-free-demo.hf.space/queue/join?',
            json=data_payload,
            headers = headers, 
            verify=False,
            cookies=None,
            proxies=proxy_config
        )
        #yield f"data: {{'progress' : {ini.text}, 'head' : {headers} }}"
        response = session.get(
            f'https://artificialguybr-realvisxl-free-demo.hf.space/queue/data?session_hash={sess_hash}',
            headers = headers, 
            stream=True,
            verify=False,
            cookies=None,
            proxies=proxy_config
        )
        
        
        for data in response.iter_lines(chunk_size=1024):
            data = data.decode()
            #yield f"data: {{'info' : {data}, 'pr' : {proxy}}}"
            if data.startswith("data: "):
                data = data[6:]
                if len(data) > 10:
                    try:
                        data = json.loads(data)
                        if data.get('msg') == 'process_completed':
                            try:

                                img = data['output']['data'][0][0]['image']['path']
                            except (KeyError) as e:
                                
                                yield f"data: {{'prog' : {data}, 'err' : {proxy} }}"
                                return
                                
                            img_url = f"https://artificialguybr-realvisxl-free-demo.hf.space/file={img}"
                            yield {"progress": "done", "img": img_url, "width": width, "height": height}
                            return
                        else:
                            progress_index = data["progress_data"][0]["index"]
                            progress_percent = (progress_index / steps) * 100
                            yield {"progress": str(progress_percent)[:4]}
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue

        
    except requests.exceptions.RequestException as e:
        
        yield {'prog': str(e), 'error': True}


        
    

def OpenDalle(prompt, negative='', width=1024, height=1024, scale=7, steps=20, style='Cinematic', shash='wefewjdi'):
    try:
        prompt += styles[style]['stylePrompt']
        negative += styles[style]['styleNegative']
    except (KeyError, IndexError):
        yield {'progress': 'style not found!'}
        
        return
    steps = min(int(steps), 100)
    proxy = WorkingProxy()
    sess_hash =  ''.join(random.choices(string.ascii_letters, k=11))

    proxy_config = {'http': proxy, 'https': proxy}
    data_payload = {"data":[prompt,negative,"","",True,False,False,random.randint(0,10000),width,height,scale,scale,steps,steps,False],"event_data":None,"fn_index":7,"trigger_id":5,"session_hash":sess_hash}
    headers = Headers(origin="https://mrfakename-opendallev1-1-gpu-demo.hf.space")
    try:
        session = requests.Session()
        ini = session.post(
            'https://mrfakename-opendallev1-1-gpu-demo.hf.space/--replicas/80xud/queue/join?',
            json=data_payload,
            headers = headers, 
            verify=False,
            cookies=None,
            proxies=proxy_config
        )
        #yield f"data: {{'progress' : {ini.text}, 'head' : {headers} }}"
        response = session.get(
            f'https://mrfakename-opendallev1-1-gpu-demo.hf.space/--replicas/80xud/queue/data?session_hash={sess_hash}',
            headers = headers, 
            stream=True,
            verify=False,
            cookies=None,
            proxies=proxy_config
        )
        
        for data in response.iter_lines(chunk_size=1024):
            data = data.decode()
            #yield f"data: {{'info' : {data}, 'pr' : {proxy}}}"
            if data.startswith("data: "):
                data = data[6:]
                if len(data) > 10:
                    try:
                        data = json.loads(data)
                        if data.get('msg') == 'process_completed':
                            try:

                                img = data['output']['data'][0]['path']
                            except (KeyError) as e:
                                
                                yield f"data: {{'prog' : {data}, 'err' : {proxy} }}"
                                return
                                
                            img_url = f"https://mrfakename-opendallev1-1-gpu-demo.hf.space/--replicas/80xud/file={img}"
                            yield {"progress": "done", "img": img_url, "width": width, "height": height}
                            return
                        else:
                            progress_index = data["progress_data"][0]["index"]
                            progress_percent = (progress_index / steps) * 100
                            yield {"progress": str(progress_percent)[:4]}
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue

        
    except requests.exceptions.RequestException as e:
        yield {'prog': str(e), 'error': True}



def mobius(prompt, negative='', width=1024, height=1024, scale=7, steps=20, style='Cinematic', shash='wefewjdi'):
    try:
        prompt += styles[style]['stylePrompt']
        negative += styles[style]['styleNegative']
    except (KeyError, IndexError):
        yield {'progress': 'style not found!'}
        return
    steps = min(int(steps), 50)
    proxy = WorkingProxy()
    proxy_config = {'http': proxy, 'https': proxy}
    sess_hash =  ''.join(random.choices(string.ascii_letters, k=11))
    data_payload = {
        "data": [
            prompt, negative, True, 0, width, height, scale, True],
            "event_data": None,
            "fn_index": 3,
            "trigger_id": 6,
            "session_hash": sess_hash
        }
    headers = Headers(origin='https://ehristoforu-mobius.hf.space')
    try:
        session = requests.Session()
        session.post(
            'https://ehristoforu-mobius.hf.space/--replicas/2sy6s/queue/join?',
            json=data_payload,
            headers=headers,
            verify=False,
            proxies=proxy_config,cookies=None
        )
        response = session.get(
            f'https://ehristoforu-mobius.hf.space/--replicas/2sy6s/queue/data?session_hash={sess_hash}',
            headers=headers,
            stream=True,
            verify=False,
            proxies=proxy_config,cookies=None
        )
        for data in response.iter_lines(chunk_size=1024):
            data = data.decode()
            if data.startswith("data: "):
                data = data[6:]
                if len(data) > 6:
                    try:
                        data = json.loads(data)
                        if data.get('msg') == 'process_completed':
                            try:
                                img = data['output']['data'][0][0]['image']['path']
                            except (KeyError) as e:
                                yield f"data: {{'progress' : {data}, 'error' : {proxy}}}"
                                return
                            img_url = f"https://ehristoforu-mobius.hf.space/--replicas/2sy6s/file={img}"
                            yield {"progress": "done", "img": img_url, "width": width, "height": height}
                            return
                        else:
                            progress_index = data["progress_data"][0]["index"]
                            progress_percent = (progress_index / steps) * 100
                            yield {"progress": str(progress_percent)[:4]}
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue

        
    except requests.exceptions.RequestException as e:
        yield {'progress': str(e), 'error': True}



def sd3(prompt, negative='', width=1024, height=1024, scale=7, steps=20, style='Cinematic', shash='wefewjdi'):
    try:
        prompt += styles[style]['stylePrompt']
        negative += styles[style]['styleNegative']
    except (KeyError, IndexError):
        yield {'progress': 'style not found!'}
        return
    steps = min(int(steps), 50)
    proxy = WorkingProxy()
    proxy_config = {'http': proxy, 'https': proxy}
    data_payload = {
        "data": [prompt, negative, 0, True, width, height, scale, steps],
        "event_data": None,
        "fn_index": 1,
        "trigger_id": 5,
        "session_hash": shash
            }
    headers = Headers(origin="https://stabilityai-stable-diffusion-3-medium.hf.space")
    try:
        session = requests.Session()
        session.post(
            'https://stabilityai-stable-diffusion-3-medium.hf.space/--replicas/177ac/queue/join?',
            json=data_payload,
            headers=headers,
            verify=False,
            proxies=proxy_config,cookies=None
        )
        response = session.get(
            f'https://stabilityai-stable-diffusion-3-medium.hf.space/--replicas/177ac/queue/data?session_hash={shash}',
            headers=headers,
            stream=True,
            verify=False,
            proxies=proxy_config
        )
        for data in response.iter_lines(chunk_size=1024):
            data = data.decode()
            if data.startswith("data: "):
                data = data[6:]
                if len(data) > 10:
                    try:
                        data = json.loads(data)
                        if data.get('msg') == 'process_completed':
                            try:
                                img = data['output']['data'][0]['path']
                            except (KeyError) as e:
                                yield f"data: {{'progress' : {data}, 'error' : {proxy}}}"
                                return
                            yield {"progress": "done", "img": f'https://stabilityai-stable-diffusion-3-medium.hf.space/--replicas/177ac/file={img}', "width": width, "height": height}
                            return
                        else:
                            progress_index = data["progress_data"][0]["index"]
                            progress_percent = (progress_index / steps) * 100
                            yield {"progress": str(progress_percent)[:4]}
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue

        
    except requests.exceptions.RequestException as e:
        yield {'progress': str(e), 'error': True}



def sdflash(prompt, negative='', width=1024, height=1024, scale=7, steps=8, style='Cinematic', shash='wefewjdi'):
    try:
        prompt += styles[style]['stylePrompt']
        negative += styles[style]['styleNegative']
    except (KeyError, IndexError):
        yield {'progress': 'style not found!'}
        return
    steps = min(int(steps), 16)
    proxy = WorkingProxy()
    proxy_config = {'http': proxy, 'https': proxy}
    data_payload = {"data":[prompt,negative,True,0,width,height,scale,steps,True,1],"event_data":None,"fn_index":2,"trigger_id":5,"session_hash":shash},
    headers = Headers(origin='https://kingnish-sdxl-flash.hf.space')
    try:
        requests.post(
            'https://kingnish-sdxl-flash.hf.space/queue/join?',
            json=data_payload,
            headers=headers,
            verify=False,
            proxies=proxy_config
        )
        response = requests.get(
            f'https://kingnish-sdxl-flash.hf.space/queue/data?session_hash={shash}',
            headers=headers,
            stream=True,
            verify=False,
            proxies=proxy_config
        )
        for data in response.iter_lines(chunk_size=1024):
            data = data.decode()
            if data.startswith("data: "):
                data = data[6:]
                if len(data) > 10:
                    try:
                        data = json.loads(data)
                        if data.get('msg') == 'process_completed':
                            img = data['output']['data'][0][0]['image']['path']
                            img = f"https://kingnish-sdxl-flash.hf.space/file={img}"
                            yield {"progress": "done", "img": img, "width": width, "height": height}
                            return
                        else:
                            progress_index = data["progress_data"][0]["index"]
                            progress_percent = (progress_index / steps) * 100
                            yield {"progress": str(progress_percent)[:4]}
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue

        
    except requests.exceptions.RequestException as e:
        yield {'progress': str(e), 'error': True}




def kivotos(prompt, negative='', width=1024, height=1024, scale=7, steps=20, style='Cinematic', shash='wefewjdi'):
    try:
        prompt += styles[style]['stylePrompt']
        negative += styles[style]['styleNegative']
    except (KeyError, IndexError):
        yield {'progress': 'style not found!'}
        
        return
    steps = min(int(steps), 50)
    proxy = WorkingProxy()
    sess_hash =  ''.join(random.choices(string.ascii_letters, k=11))

    proxy_config = {'http': proxy, 'https': proxy}
    data_payload = {
        "data": [
            prompt, negative,random.randint(0,100000),width,height,scale,steps,
            "Euler a","Custom",False,0.55,1.5,True
  ],
  "event_data": None,
  "fn_index": 6,
  "trigger_id": 41,
  "session_hash":sess_hash
}

    headers = Headers(origin="https://linaqruf-kivotos-xl-2-0.hf.space")
    try:
        session = requests.Session()
        ini = session.post(
            'https://linaqruf-kivotos-xl-2-0.hf.space/queue/join?',
            json=data_payload,
            headers = headers, 
            verify=False,
            cookies=None,
            proxies=proxy_config
        )
        #yield f"data: {{'progress' : {ini.text}, 'head' : {headers} }}"
        response = session.get(
            f'https://linaqruf-kivotos-xl-2-0.hf.space/queue/data?session_hash={sess_hash}',
            headers = headers, 
            stream=True,
            verify=False,
            cookies=None,
            proxies=proxy_config
        )
        
        for data in response.iter_lines(chunk_size=1024):
            data = data.decode()
            #yield f"data: {{'info' : {data}, 'pr' : {proxy}}}"
            if data.startswith("data: "):
                data = data[6:]
                if len(data) > 10:
                    try:
                        data = json.loads(data)
                        if data.get('msg') == 'process_completed':
                            try:

                                img = data['output']['data'][0][0]['image']['path']
                            except (KeyError) as e:
                                
                                yield f"data: {{'prog' : {data}, 'err' : {proxy} }}"
                                return
                                
                            img_url = f"https://linaqruf-kivotos-xl-2-0.hf.space/file={img}"
                            yield {"progress": "done", "img": img_url, "width": width, "height": height}
                            return
                        else:
                            progress_index = data["progress_data"][0]["index"]
                            progress_percent = (progress_index / steps) * 100
                            yield {"progress": str(progress_percent)[:4]}
                    except (json.JSONDecodeError, KeyError, IndexError):
                        continue

        
    except requests.exceptions.RequestException as e:
        yield {'prog': str(e), 'error': True}
