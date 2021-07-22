import imdb
ia = imdb.IMDb()
search = ia.search_movie('joker')
year = search[1]['year']
print(search[0]['title']+":"+str(year))