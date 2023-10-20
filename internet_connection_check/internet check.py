import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

def internet_connection_test(url='https://www.google.com/'):
    print(f'Attempting to connect to {url} to determine internet connection status.')

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        print(f'Connection to {url} was successful.')
        return True
    except ConnectionError:
        print(f'Failed to connect to {url}.')
    except Timeout:
        print(f'Timeout occurred while attempting to connect to {url}.')
    except RequestException as e:
        print(f'An error occurred: {e}')
    return False

if __name__ == "__main__":
    internet_connection_test()
