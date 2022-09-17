from itertools import product
from concurrent.futures import ThreadPoolExecutor
import time
import requests

import progressbar
  

widgets = [' [',
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'),
         '] ',
           progressbar.Bar('*'),' (',
           progressbar.ETA(), ') ',
          ]
  
requests.packages.urllib3.disable_warnings()

class ScanIP(object):
    def __init__(self, tld, verbose=True, thredas=150, delay_threads=0) -> None:
        """
        from spike import ScanIP

        # TLD = Top Level To Domain/Alpha-2 code https://www.iban.com/country-codes
        # verbose = 

        scanner = ScanIP(tld="id")
        """
        self.delay_threads = delay_threads
        self.verbose = verbose
        self.thredas = thredas
        self.executor = ThreadPoolExecutor(max_workers=self.thredas)
        self.tld = tld.upper()
        self.Pthreds = list()
    def table_ips(self, TableRange):
        ips = list()
        end_sig_one, begin_sig_one     =  int(TableRange[0].split(".")[0])+1 , int(TableRange[1].split(".")[0])
        end_sig_two, begin_sig_two     =  int(TableRange[0].split(".")[1])+1, int(TableRange[1].split(".")[1])
        end_sig_three, begin_sig_three =  int(TableRange[0].split(".")[2])+1, int(TableRange[1].split(".")[2])
        end_sig_four, begin_sig_four   =  int(TableRange[0].split(".")[3])+1, int(TableRange[1].split(".")[3])
        for sig_one, sig_two, sig_three, sig_four in product(
            range(begin_sig_one, end_sig_one), range(begin_sig_two, end_sig_two),
            range(begin_sig_three, end_sig_three), range(begin_sig_four, end_sig_four), repeat=1):
            ips.append(f"{sig_one}.{sig_two}.{sig_three}.{sig_four}")
        return ips

    def scan(self, do_it):
        """
        def exploit(ip):
            pass # todo code exploit
        spkie.scan(do_it=exploit)
        requests.exceptions.ConnectionError
        """
        response = requests.get(f'https://cdn-lite.ip2location.com/datasets/{self.tld}.json', verify=False)
        TableIP = [(d[1], d[0]) for d in response.json()["data"]]
        length_tables = len(TableIP)
        for loop, table in enumerate(TableIP):
            range_ip = self.table_ips(table)
            if self.verbose:
                print(f"  {loop}/{length_tables}  scan range from {table[1]} to {table[0]}  ")
            bar = progressbar.ProgressBar(max_value=len(range_ip), widgets=widgets).start()
            for Secloop, ip in enumerate(range_ip):
                try:
                    if self.verbose:
                        bar.update(Secloop)
                    self.executor.submit(do_it, ip)
                    time.sleep(self.delay_threads)
                except RuntimeError:
                    print("[#] your resource threds is over use limit threds or delay per thread")
                except KeyboardInterrupt:
                    quit("closed the scanner")
