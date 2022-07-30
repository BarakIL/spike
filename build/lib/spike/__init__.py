from itertools import product
import threading, time
from requests import get


class ScanIP(object):
    def __init__(self, tld, verbose=True, thredas=300, delay_threads=0.1) -> None:
        """
        from spike import ScanIP

        # TLD = Top Level To Domain/Alpha-2 code https://www.iban.com/country-codes
        # verbose = 

        scanner = ScanIP(tld="id")
        """
        self.delay_threads = delay_threads
        self.verbose = verbose
        self.thredas = thredas
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
        """
        response = get(f'https://cdn-lite.ip2location.com/datasets/{self.tld}.json')
        TableIP = [(d[1], d[0]) for d in response.json()["data"]]
        for table in TableIP:
            for ip in self.table_ips(table):
                try:
                    if self.verbose:
                        print(f'[*] scan ->> {ip}', end="\r")
                    if type(self.thredas) == int:
                        if threading.active_count() > self.thredas:
                            time.sleep(self.delay_threads)
                    t = threading.Thread(target=do_it, args=(ip, ))
                    self.Pthreds.append(t)
                    t.start()
                except RuntimeError:
                    print("[#] your resource threds is over use limit threds or delay per thread")
                except KeyboardInterrupt:
                    quit("closed the scanner")
            for t in self.Pthreds:
                t.join()
                



