# Spike Easy Scanner


## spike is fast scanner 

<sub>Spike can help you scan all IP ranges by country code only with multithreading and you can write the exploit yourself on an existing packet to scan with it!</sub>


<p align="center">
  <img src="https://images.vexels.com/media/users/3/145266/raw/0c5d8ff5814fa9ac97c195559eccbbad-flat-rocket-illustration-badge.jpg" />
</p>

***Look on scripts in examples***

# Downlaod and install Spike Project

### Downlaod Project
```bash
git clone https://github.com/BarakIL/spike.git
```

### install Project
```bash
cd spike; python3 setup.py install
```

# Example Get All Domain in Iran

```python3
from spike import ScanIP
import socket

def resolver(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f'{ip} ->> {host[0]}')
    except:
        pass
if __name__ == "__main__":
    s = ScanIP("ir")
    s.scan(resolver)
    
```
