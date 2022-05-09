## dns-resolver
Using dnspython, a toolkit for Python to resolve DNS queries.

1. To run, clone this repository and go into that directory.
2. With a terminal of your choice, input: `python mydig.py` followed by any website, like www.google.com
3. Example output:

```console
$ python mydig.py
Enter site: cnn.com
QUESTION SECTION:
cnn.com. IN A
ANSWER SECTION:
cnn.com. 60 IN A 151.101.1.67
cnn.com. 60 IN A 151.101.129.67
cnn.com. 60 IN A 151.101.193.67
cnn.com. 60 IN A 151.101.65.67
Query time: 23.23436737060547 msec
WHEN: 2021-03-04 19:11:28.770866
```
