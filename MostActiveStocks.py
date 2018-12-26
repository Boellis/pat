from googlesearch import search
#import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create a list to hold the urls of our stocks
stock_list = []
# Looks for the most active stocks of the days and pulls their price from their NASDAQ page with StockPrice() function
def findMostActiveStocks():
    activeStocks = "https://www.nasdaq.com/markets/most-active.aspx"
    #Set the page that we will be scraping
    quote_page = activeStocks
    #Query the website and return the html to the variable 'html_page'
    html_page = urlopen(quote_page)
    #Parse the html using beautfil soup and store in the variable 'soup'
    soup = BeautifulSoup(html_page, 'html.parser')
    #Get the price
    stock_price_box = soup.find_all('a', attrs={'class':'mostactive'})
    for n in stock_price_box:
        stock_list.append(n.attrs['href'])

    # List them all
    #for i in range(len(stock_list)):
    # List top 10
    for i in range(10):
        print(stock_list[i])
        print(getStockPrice(stock_list[i]))
        print("---------------")

    # Prints an array of all the NASDAQ urls of the most active stocks
    #print(stock_list)


def getStockPrice(stockName):
    #Query the website and return the html to the variable 'html_page'
    html_page = urlopen(stockName)
    #Parse the html using beautfil soup and store in the variable 'soup'
    soup = BeautifulSoup(html_page, 'html.parser')
    #Get the price
    stock_price_box = soup.find('div', attrs={'class':'qwidget-dollar'})
    #Print the price
    return "Price: " + stock_price_box.text
    #return stock_price_box.text


if __name__ == '__main__':
    try:
        Stock()

    except KeyboardInterrupt:
        print("Program Interrupted")
