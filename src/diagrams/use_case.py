from diagrams import Diagram
from diagrams.c4 import Person, Container

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/use_case', outformat='png', show=False, direction="TB"):

    user = Person("User", technology=None, type='')
    website = Container('Visit Website', technology=None, type='')

    cabinet = Container('Login', technology=None, type='')
    allow_functionalities = Container('Unlock Features', technology=None, type='')

    trading_system = Container('Open Trading System', technology=None, type='')
    trading_strategy = Container('Choose Trading Strategy', technology=None, type='')
    bot_start = Container('Start Trading Bot', technology=None, type='')
    bot_stop = Container('Stop Trading Bot', technology=None, type='')
    bot_monitoring = Container('Bot Monitoring', technology=None, type='')

    analytics = Container('View Analytics', technology=None, type='')
    analytics_history = Container('Trading Success History', technology=None, type='') 

    news = Container('Read News', technology=None, type='')
    stock_news = Container('Stock News Summary', technology=None, type='')

    prediction = Container('Predict Stock Price', technology=None, type='')


    user >> website >> [cabinet, trading_system, analytics, news, prediction]
    cabinet >> allow_functionalities
    trading_system >> trading_strategy >> bot_start
    bot_start >> [bot_stop, bot_monitoring]
    analytics >> analytics_history
    news >> stock_news
