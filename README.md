# Spike Easy Scanner


## spike is fast scanner 

<sub>Spike can help you scan all IP ranges by country code only with multithreading and you can write the exploit yourself on an existing packet to scan with it!</sub>
![This is an logo](https://cdn.dribbble.com/users/1787323/screenshots/9791845/media/81210e0150e626aa9678b53fc46bffa7.png?compress=1&resize=400x300)

***Look on scripts in examples***

# Downlaod and install Spike Project

### Downlaod Project
```bash
git clone https://github.com/BarakIL/spike.git
```

### install Project
```bash
python3 spike/setup.py install
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
