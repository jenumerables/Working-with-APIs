import requests
# API Key: 72fcdab56cfd4663844483bc2f6fc10f

r = requests.get(
  'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-1-01&to=2023-1-22&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'
)

content = r.json()

# Dictionary data type
#print(type(content))

# print first article title
#print(content['articles'][0]['title'])

# print article description
#print(content['articles'][0]['description'])

#print(content['articles'][0]['content'])

#articles = content['articles']
# list of dictionaries
#print(type(articles))

# print all titles and description
#for article in articles:
  #print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])


# create dynamic function
def get_news(topic,
             from_date,
             to_date,
             language='en',
             api_key='72fcdab56cfd4663844483bc2f6fc10f'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='stock',from_date='2023-1-01',to_date='2023-1-22'))