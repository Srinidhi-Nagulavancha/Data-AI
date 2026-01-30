import re

ip_address = []

ip_pattern = re.compile(r"\[([0-9]{1,3}(?:\.[0-9]{1,3}){3})\]")

with open("sample.csv", "r", encoding="utf-8") as f:
    for line in f:
        m = ip_pattern.search(line)
        if m:
            ip_address.append(m.group(1))

with open("ip_addr_out_csv.txt", "w", encoding="utf-8") as ip:
    for addr in ip_address:
        ip.write(addr + "\n")

print(f"Extracted {len(ip_address)} IP address(es) to ip_addr_out_csv.txt.")