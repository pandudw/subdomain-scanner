import requests

api_key = ' '
api_secret = ' '
domain = ' '

def get_subdomains(api_key, api_secret, domain):
    url = f'https://api.godaddy.com/v1/domains/{domain}/records'
    headers = {'Authorization': f'sso-key {api_key}:{api_secret}'}
    response = requests.get(url, headers=headers)

    print(f"API Response Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        subdomains = [record['name'] for record in data if record['type'] == 'A']
        return subdomains
    else:
        print(f"Error: {response.status_code}")
        try:
            error_message = response.json().get('message')
            print(f"Error Message: {error_message}")
        except:
            pass
        return []

subdomains = get_subdomains(api_key, api_secret, domain)
print(f"Subdomains for {domain}: {subdomains}")
