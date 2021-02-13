import urllib
import re

URL = "https://2ip.ru"

def getExternalIP():
    try:
        resp = urllib.urlopen(URL)
        if resp.code == 200:
            data = resp.read()
            reg_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
            s = reg_ip.search(data)
            return data[s.start():s.end()]
    except Exception as e:
        print(e)
        return None
    
def main():
    ipaddr = getExternalIP()
    if ipaddr != None :
        print("External IP: %s" % ipaddr)
        
if __name__ == "__main__":
    main()
