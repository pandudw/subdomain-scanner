import requests

# input the domain to scan subdomains
domain= "tokopedia.com"

# read all subdomains from file (subdomains.txt)
file= open("subdomains.txt")

# read all content 
content= file.read()

# split to create a new lines
subdomains= content.splitlines()
