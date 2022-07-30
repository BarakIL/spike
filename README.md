# Spike Easy Scanner


## spike is fast scanner can help your scan all range ip
## by only country code wiyh multi-threading

# install 

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
