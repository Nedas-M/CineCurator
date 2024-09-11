from scraperFunctions import fetchData, extractData, printData
from dotenv import load_dotenv
import os

load_dotenv()

bestMoviesUrl = os.getenv('BEST_MOVIES_URL')
inTheatresUrl = os.getenv('IN_THEATRES_URL')

bestMoviesSoup = fetchData(bestMoviesUrl)


if bestMoviesSoup:
    bestMovieData = bestMoviesSoup.findAll('div', attrs={'class': 'c-finderProductCard'})
    bestMovies = extractData(bestMovieData)
    printData(bestMovies, "BEST THIS YEAR")
inTheatresSoup = fetchData(inTheatresUrl)
if inTheatresSoup:
    theatreMovieData = inTheatresSoup.findAll('div', attrs={'class': 'c-finderProductCard'})
    theatreMovies = extractData(theatreMovieData)
    printData(theatreMovies, "BEST IN THEATRES")
