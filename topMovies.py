from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

yearPageScrape = requests.get('https://www.metacritic.com/browse/movie/all/all/current-year/', headers=headers)
print('STATUS CODE : ' + str(yearPageScrape.status_code), '\n')
soup = BeautifulSoup(yearPageScrape.content, 'html.parser')

movieData = soup.findAll('div', attrs={'class':'c-finderProductCard'})

for movie in movieData:
    
    titleElement = movie.find('h3', attrs={'class':'c-finderProductCard_titleHeading'})
    title = titleElement.get_text(strip=True) if titleElement else 'NO TITLE'

    descElement = movie.find('div', attrs={'class':'c-finderProductCard_description'})
    desc = descElement.get_text(strip=True) if descElement else 'NO DESCRIPTION'

    scoreElement = movie.find('div', attrs={'class':'c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green g-color-gray90 c-siteReviewScore_xsmall'})
    score = scoreElement.get_text(strip=True) if scoreElement else 'NO SCORE'

    print(title, '\n', desc, score, '\n')