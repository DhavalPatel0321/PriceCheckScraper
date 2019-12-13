import requests
from bs4 import BeautifulSoup
import smtplib
#cant find the URL he wants, so im using a dummy one for now
URL = 'https://www.costco.com/lighting-by-pecaso-charlotte-chandelier-with-heirloom-grandcut-crystal.product.100481067.html'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'


def check_price():
    headers = {'user-agent':user_agent}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find("div", class_="product-h1-container visible-xs-block visible-sm-block visible-md-block visible-lg-block").get_text().strip()

    price = soup.find_all("div", class_="pull-right")
    #price = str(price)[54:57]
    #price = float(price)

    #if price < 1000:
   #     send_mail()

    print('Title: ' + str(title))
   # print('Price: ' + str(price))

check_price()

#bbzdecfwvlroqtew
"""
In order to use the smtp server to send emails, i set up a app password via google app passwords

"""
def send_mail():
    server = smtplib.SMTP('stmp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('dhavalp0321@gmail.com', 'bbzdecfwvlroqtew')

    subject = "Price Drop Reported"
    body = "Check the Costco Link "