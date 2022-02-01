""" Test concurrency """
import concurrent.futures
import threading
import time
import requests

thread_local = threading.local()

def get_session():
    """ get thread info """
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    """ download url """
    session = get_session()
    with session.get(url) as _:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='', flush=True)

def download_all_sites(target_sites):
    """ spin up download threads """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, target_sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        ] * 10

    print("Starting downloads")
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")
