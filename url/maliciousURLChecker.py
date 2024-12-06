from urllib.parse import urlparse
import coverage
import os

def urlChecker(url):
    #parse URL into parts:
    url_ = urlparse(url)
    scheme = url_.scheme
    hostname = url_.hostname
    body = ''
    tld = ''

    domain = hostname.split(".")

    subdomain = domain[0]
    tld = domain[-1]
    if len(domain) > 3:
        body = ''
        for x in domain[1:-1]:
            body = body + "." + x
        body = body[1:]
    else:
        body = domain[1]
    path = url_.path

    #now check url for malicious patterns:
    if tld in ['ru', 'tk', 'icu', 'xyz', 'cn']:
        if any(e in path for e in [".exe", ".bat", ".sh", ".app"]):

            return "This site may be malicious. Please consider visiting a different site."
        elif len(domain) > 5:
            return "This site may be malicious. Please consider visiting a different site."

        elif any(e in body for e in ["<", ">", "%"]) or any(e in path for e in ["<", ">", "%"]):
            return "This site may be malicious. Please consider visiting a different site."

    if scheme != "https":
        if any(e in path for e in [".exe", ".bat", ".sh", ".app"]):
            if len(domain) > 5:
                return "This site may be malicious. Please consider visiting a different site."

        elif any(e in body for e in ["<", ">", "%"]) or any(e in path for e in ["<", ">", "%"]):
            return "This site may be malicious. Please consider visiting a different site."

    


    
