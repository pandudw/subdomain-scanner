import requests

# input the domain to scan subdomains
domain= "tokopedia.com"

# read all subdomains from wordlists
file= open("subdomains.txt")

# read all content 
content= file.read()

# split to create a new lines
subdomains= content.splitlines()

# a list of discovered subdomains
discovered_subdomains = []
for subdomain in subdomains:

# construct the url for subdomain
    url= f"http://{subdomain}.{domain}"
    
# test to get the HTTP response from server
    try: 
        request.get(url)
      
# if this raises an error, that means the subdomain does not exist and just pass the process
    except Exception:
        pass
    else:
        print("[+] Discovered subdomain", url)
# append the discovered subdomain
        discovered_subdomains.append()
