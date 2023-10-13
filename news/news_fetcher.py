from newsapi import NewsApiClient
import environ


env = environ.Env()

key = env("NEWS_API_KEY")
print(key)

# Init
newsapi = NewsApiClient(api_key=key)


def news_fetcher_function(**kwargs):
    for key,value in kwargs.items():
        if key=="query":
            query=value
        if key=="sources":
            sources=value
        if key=="category":
            category=value
        if key=="language":
            language=value
        if key=="from_date":
            from_date=value
        if key=="to_date":
            to_date=value
    
    print("9-----------", from_date)
    print("9-----------", to_date)

    all_articles = newsapi.get_everything(q=query if query else "",
                                          sources=sources if sources else "",
                                          # domains='bbc.co.uk,techcrunch.com',
                                          domains='',
                                          from_param=from_date if from_date else '2023-10-11',
                                          to=to_date if to_date else '2023-10-11',
                                          language=language if language else 'en',
                                          sort_by=category if category else 'relevancy',
                                          # page=2,
                                          )

    return all_articles