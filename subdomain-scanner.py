import requests

def get_subdomains(api_key, api_secret, domain):
    url = 
    headers = {'Authorization': f'sso-key {api_key}:{api_secret}'}

    response = requests.get(url, headers=headers)

    print(f"API Response Status Code: {response.status_code}")