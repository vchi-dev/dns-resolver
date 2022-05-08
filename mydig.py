import dns.query
import dns.message
import dns.name
import dns.rdatatype

import time
import datetime

domain = input("Enter site: ")
hostname = dns.name.from_text(domain)
nameserver = '205.251.192.47' # Amazon Server

if not hostname.is_absolute():
    hostname = hostname.concatenate(dns.name.root)

start = time.time()

request = dns.message.make_query(hostname, dns.rdatatype.A)
UDPrequest = dns.query.udp(request, nameserver)

while UDPrequest.answer == [] and UDPrequest.additional != []:
    ipAddresses = []

    for ipAddress in UDPrequest.additional:
        for someText in ipAddress:
            text = someText.to_text()
            if "." in text:
                ipAddresses.append(text)
                
    for ipAddress in ipAddresses:
        nameserver = ip
        request = dns.message.make_query(hostname, dns.rdatatype.A)
        UDPrequest = dns.query.udp(request, nameserver)

end = time.time()

print("QUESTION SECTION:")
print(hostname, "   IN A")
print()
print("ANSWER SECTION:")
for ipAddress in UDPrequest.answer:
    print(ipAddress)
print()
print("Query time: ", (end - start)*1000, "msec")
print("WHEN: ", datetime.datetime.now())