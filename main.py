import requests
# API Key: 72fcdab56cfd4663844483bc2f6fc10f

r = requests.get(
  'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-1-01&to=2023-1-22&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

content = r.json()

# create dynamic function
def get_news(country,
             api_key='72fcdab56cfd4663844483bc2f6fc10f'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(country='us'))