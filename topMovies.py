# Scraping top 10 movies

from scraperFunctions import fetchData, extractData, printData
from dotenv import load_dotenv
import os

load_dotenv()

bestMoviesUrl = os.getenv('BEST_MOVIES_URL')
inTheatresUrl = os.getenv('IN_THEATRES_URL')

bestMoviesSoup = fetchData(bestMoviesUrl)

# If the data was successfully fetched, process it
if bestMoviesSoup:
    bestMovieData = bestMoviesSoup.findAll('div', attrs={'class': 'c-finderProductCard'})
    bestMovies = extractData(bestMovieData)
    printData(bestMovies, "BEST THIS YEAR")

inTheatresSoup = fetchData(inTheatresUrl)

# If the data was successfully fetched, process it
if inTheatresSoup:
    theatreMovieData = inTheatresSoup.findAll('div', attrs={'class': 'c-finderProductCard'})
    theatreMovies = extractData(theatreMovieData)
    printData(theatreMovies, "BEST IN THEATRES")
