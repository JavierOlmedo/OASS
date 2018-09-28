from lib.output import *
import requests
import re
import os

def hunterio():
    default("Find emails in Hunter.io")
    emails = []
    url = "https://api.hunter.io/v2/domain-search?domain=" + dominio +"&api_key=" + API
    try:
        r = requests.get(url)
        rdata = r.json()
        resultados = rdata['meta']['results']
        if (resultados >= 1):
            success(str(resultados) + " emails found!! from domain " + domain)
            emails = rdata['data']['emails']
        else:
            error(str(resultados) + " emails found!!")
        for mail in emails:
            success(mail['value'])
    except:
        error("Error de API")

def theharvester():
    default("Launch command in TheHarvester")
    c = "theharvester -d " + domain +" -b all"
    os.system(c)


def info001():
    info("INFO-001 Conduct search engine discovery/reconnaissance for information leakage")
    hunterio()
    theharvester()
    print("\n")