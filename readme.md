# Just bruteforce
This is a simple web URL bruteforce script developed for my assignment from [**Cloudsek**](https://cloudsek.com/)

## Installation
1. Install the dependencies using the following code
```pip3 install -r requirements.txt```
2. Source the virtual environment by running the following code in the project root directory ```source venv/bin/activate```

## Usage
Run the tool using: 

**GENERAL USAGE**

``python3 main.py -u <url> [optional <url>] -w <wordlist_file_name> -s <status_code> [optional <status_code>]``

### Mandatory Params
1. ```-u``` or ```--url```: After specifying this parameter, tool will expect list of url seperated by spaces
2. ```-w``` or ```--wordlist```: After this parameter, tool expects the name of wordlist file with extension located in the project root.
3. ```-s``` or ```--statuscode```: After this parameter, tool expects one or more status codes seperated by spaces which should be considered as success. PS: All should be integers.

### Results
- Results will be written in a ```result.txt``` file generated in the project root itself. If the file already exist, no worries on losing data, it will change the name of output file as ```result<int>.txt```.
- Results related to each URL will be under a heading ``-----RESULTS FOR <URL>-----``

## How it works
After receiving the user inputs and output file name, tool iterates over URLS and collect each word from the file and this request will be pooled for threads. This threads will work asynchronously.
### Advantages
1. RAM Usage is never a challenge as we are just reading single lines from wordlist.
2. Request are being pooled into ThreadPools, and they're run asynchronously so that parallel request are made to avoid the summation of waiting time.
### Miscellaneous Notes
1. ``pool_count`` variable: 
   - This variable can be used as a count for requests to be pooled for concurrent/parallel requests. I recommend, to keep this to be an optimum number depending on the size of wordlist.
   - If this is enough high and wordlist is also enough big, it will give good results in terms of performance, but if the word list is small given this is high, it will give ordinary results as advantage of pooling is not taken here.
   - If this is small and wordlist is big, here also it will give ordinary results as advantage of pooling is not taken here. 
   - Another point to be noted is if this is too high, it affects adversely as pooling takes more time than making requests.

## Credits
Used blogs:
1. [Writing fast async HTTP requests in Python - JonLuca&#39;s Blog](https://blog.jonlu.ca/posts/async-python-http) 

## Developer Info
Ajwad Juman PC  
3rd Year Student  
IIT Kharagpur

[ajwadjumanpc@gmail.com](mailto:ajwadjumanpc@gmail.com)  
[armedjuror@gmail.com](mailto:armedjuror@gmail.com)  

[GITHUB](https://github.com/armedjuror) | [WEB](https://armedjuror.github.io/)