import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class crawledArticle():
    def __init__(self, url, title, price,rating,):
        self.title = title
        self.price = price


class Bot:

    def article(self):
        count = 5
        page = 1
        pageinc = 20
        maxretrieves = 100
        a = []

        url = f"https://www.amazon.in/s?k=bags&page={str(page)}&crid=2M096C61O4MLT&qid=1679457615&sprefix=ba%2Caps%2C283&ref=sr_pg_2{str(page)}"

        options = Options()
        options.headless = True
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(15)

        while True:
            try:
                if page > 20:
                    break

                if count > 16:
                    count = 5
                    page += 1

                # get URL
                xpathtitle = f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{str(count)}]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a'
                URLtitle = browser.find_element_by_xpath(xpathtitle)
                titleURL = URLtitle.get_attribute('href')

                # get title
                xpathtitle = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(
                    count) + ']/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'
                title = browser.find_element_by_xpath(xpathtitle)
                titletext = title.get_attribute('innerHTML').splitlines()[0]
                print(titletext)
                print(titleURL)
                title.click()


                # get price
                xpathprice = 'a-price-whole'
                price = browser.find_element_by_class_name(xpathprice)
                pricetext = price.get_attribute('innerHTML')
                print(pricetext)

                # get rating
                ratingclass = 'a-icon-alt'
                rating = browser.find_element_by_class_name(ratingclass)
                ratingtext = rating.get_attribute('innerHTML')
                print(ratingtext)


                url = f"https://www.amazon.in/s?k=bags&page={str(page)}&crid=2M096C61O4MLT&qid=1679457615&sprefix=ba%2Caps%2C283&ref=sr_pg_2{str(page)}"
                browser.get(url)
                browser.set_page_load_timeout(10)

                info = crawledArticle(titletext, pricetext)
                a.append(info)

                count += 1

            except Exception as e:
                print("Exception", e)
                count += 1

                if page > 20:
                    break

                if count > 16:
                    count = 5
                    page += 1

                url = f"https://www.amazon.in/s?k=bags&page={str(page)}&crid=2M096C61O4MLT&qid=1679457615&sprefix=ba%2Caps%2C283&ref=sr_pg_2{str(page)}"
                browser.get(url)
                browser.set_page_load_timeout(10)

                print(page)
                print(a)

        browser.close()
        return a


fetcher = Bot()
with open('pro.csv', 'w', newline='', encoding='utf-8') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for article in fetcher.article():
        articlewriter.writerow([article.title, article.price])




# //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a
