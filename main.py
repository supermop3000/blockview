# the main file for the program
#!/usr/bin/env python
import requests
import PyQt5



def main():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    print(data['bpi']['USD']['rate'])

if __name__ == "__main__":
    main()