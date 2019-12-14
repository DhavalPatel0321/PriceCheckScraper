import requests
from bs4 import BeautifulSoup
import smtplib
import time
#cant find the URL he wants, so im using a dummy one for now
URL = 'https://www.amazon.com/Sceptre-Edge-Less-FreeSync-DisplayPort-C275B-144RN/dp/B07N6ZBCVY/ref=sxin_2_ac_d_rm?ac_md=4-2-bW9uaXRvciAxNDRoeg%3D%3D-ac_d_rm&keywords=monitor&pd_rd_i=B07N6ZBCVY&pd_rd_r=b107eabc-45bf-4145-be75-3a0569302e52&pd_rd_w=h78kz&pd_rd_wg=vKUOL&pf_rd_p=e2f20af2-9651-42af-9a45-89425d5bae34&pf_rd_r=KNRQMKN589J0J7GK8F0Z&psc=1&qid=1576282884'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'


def check_price():
    headers = {'User-Agent':user_agent}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    #time.sleep(5)
    title = soup.find(id="productTitle")

    price = soup.find(id="priceblock_ourprice")

    #price = str(price)[54:57]
    #price = float(price)

    #if price < 1000:
   #     send_mail()

    print('Title: ' + (title))
    print('Price: ' + (price))

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
    body = "Check the Costco Link: https://www.costco.com/lighting-by-pecaso-charlotte-chandelier-with-heirloom-grandcut-crystal.product.100481067.html"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'dhavalp0321@gmail.com', #sender
        'dhavalp0321@gmail.com', #receipient
        msg                         # message
    )
    print("email successfully sent!")

    server.quit()