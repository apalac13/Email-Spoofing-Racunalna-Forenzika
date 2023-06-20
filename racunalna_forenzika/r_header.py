import re


def matchre(data, *args):
    for regstr in args:
        matchObj = re.search(regstr+'.*', data, re.M | re.I)
        if matchObj:
            print(matchObj.group(0).lstrip().rstrip())
            if regstr == "Authentication-Results":
                ip_match = re.search(
                    r'sender IP is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', matchObj.group(0))
                if ip_match:
                    ip = ip_match.group(1)
                    name_match = re.search(
                        r'header.from=(\S+)', matchObj.group(0))
                    if name_match:
                        name = name_match.group(1)
                        print(f"Sender IP: {ip}")
                        print(f"Sender Name: {name}")
                    else:
                        print("Sender name not found")

                else:
                    print("Sender IP not found")
        else:
            print("No ", regstr, "found")


if __name__ == "__main__":
    print("Email Header Program analizer: ")
    filename = "header_file.txt"
    fo = open(filename, "r")  # fo=filehandle
    data = fo.read()
    matchre(data, "MIME-version", "Date:", "Subject:",
            "delivered-to:", "From:", "^to:", "reply-to")
    matchre(data, "Authentication-Results")
    matchre(data, "Received-SPF")
    fo.close()
