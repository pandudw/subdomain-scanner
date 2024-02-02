# Subdomain Scanner

Subdomain Scanner is a simple tool to retrieve a list of subdomains for a given domain along with their status codes.

## Prerequisites
- `api_key`: Your domain registrar API key.
- `api_secret`: Your domain registrar API secret.
- `domain`: The domain to be enumerated.

## How to Use
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/subdomain-enumerator.git
    cd subdomain-enumerator
    ```
2. **Run the Script:**
    ```bash
    python3 subdomain_enumerator.py
    ```
3. **Review Results:**
    The script will print a list of subdomains along with their status codes.

## Notes

- Replace the values of `YOUR_API_KEY`, `YOUR_API_SECRET`, and `example.com` with your corresponding information.
    
## Dependencies
- `requests`: Python library for making HTTP requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
