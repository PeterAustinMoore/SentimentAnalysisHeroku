from aiohttp import web
import nltk
import operator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

bounds = {0.7: "positive", 0.2:"slight positive", 0:"nuetral", -0.2:"slight negative", -0.7:"negative"}

async def handle(request):
    sentence = request.rel_url.query["data"]
    print(sentence)
    ss = sid.polarity_scores(sentence)
    sen = ss["compound"]
    data = {"sentiment":bounds[min(bounds, key=lambda x:abs(x - sen))], "value":sen}
    print(data)
    return web.json_response(data)

async def indx(request):
    return web.Response(text="head over to /sentiment?data=[your sentence]")


async def sentiment_app():
    app = web.Application()
    app.add_routes([web.get('/', indx),
                    web.get('/sentiment', handle)])
    return app
