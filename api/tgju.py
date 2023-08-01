import requests
import time

for _ in range(1000):
    try:
        response = requests.get("http://www.tgju.org/?act=sanarateservice&client=tgju&noview&type=json")
    except Exception as error:
        print ('error')
        break
        
    else: 
        print(response.status_code)
        if response.status_code == 200:
            dict_ = response.json()
        
            keys = list(dict_.keys())
            for i in keys:
                print(dict_[i]['title'], dict_[i]['price'])
        
            #print(mydict)
            time.sleep(30)
