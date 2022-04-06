import os
import sys
import urllib.parse
import requests
from BruteForceHelper import ThreadPool
import time

started = time.time()

print(f"Started at {started}")

pool_count = 100

urls = []
wordlist = ''
status_codes = []
arg_type = ''

# Collecting the input
for arg in sys.argv:
    if arg == '-u' or arg == '--url':
        arg_type = 'url'
    elif arg == '-w' or arg == '--wordlist':
        arg_type = 'wordlist'
    elif arg == '-s' or arg == '--statuscode':
        arg_type = 'statuscode'
    else:
        if arg_type == 'url':
            urls.append(arg.strip())
        elif arg_type == 'wordlist':
            wordlist = arg.strip()
        elif arg_type == 'statuscode':
            status_codes.append(int(arg.strip()))


def get(url):
    response = requests.get(url)
    print(url, response)
    if response.status_code in status_codes:
        result_file.write(f"{url}[Status Code {response.status_code}]\n")


wordlist_fp = open(wordlist, 'r')

# Checking whether result file already exist and renaming
result_file_name = 'result'
i = 0
while True:
    if not os.path.exists(result_file_name+".txt"):
        break
    else:
        i += 1

        result_file_name = "result" + str(i)

result_file_name += '.txt'
result_file = open(result_file_name, 'w')

pool = ThreadPool(pool_count)
req = requests.session()

curr_url_list = []
low_url_count = True

for url in urls:
    result_file.write(f'-----RESULTS FOR {url}-----\n')
    for word_count, word in enumerate(wordlist_fp):

        request_url = urllib.parse.urljoin(url, word.strip())
        curr_url_list.append(request_url)

        if word_count > pool_count:
            low_url_count = False

        if (word_count + 1) % pool_count == 0:
            pool.map(get, curr_url_list)
            pool.wait_completion()
            curr_url_list = []

if low_url_count:
    pool.map(get, curr_url_list)
    pool.wait_completion()

result_file.close()
wordlist_fp.close()
print(f"Total time: {time.time() - started}")