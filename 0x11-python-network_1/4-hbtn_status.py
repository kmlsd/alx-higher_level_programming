
#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/statu""""

if __name__ == "__main__":
    content = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

