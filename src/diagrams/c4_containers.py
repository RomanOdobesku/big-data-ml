from diagrams import Diagram
from diagrams.c4 import Person, Container, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_containers', outformat='png', show=False, graph_attr=graph_attr):
    user = Person(
        name="User",
        description="Engages with the trading system via various interfaces."
    )

    with SystemBoundary("Trading System"):

        web = Container(
            name="Web Application",
            technology='Python, Streamlit',
            type='Container',
            description="Provides user interface for trading operations.",
        )

        tg_bot = Container(
            name="Telegram Bot",
            technology='Python',
            type='Container',
            description="Offers trading functionalities through Telegram.",
        )

        mobile_app = Container(
            name="Mobile App",
            technology='Android, iOS',
            type='Container',
            description="Enables trading access on mobile devices.",
        )

        application_api = Container(
            name="Application API",
            technology='Python, FastAPI',
            type='Container',
            description="Connects user interfaces with backend logic.",
        )

        data_storage = Container(
            name="Data Storage",
            technology=None,
            type='HDFS',
            description="Stores a variety of trading-related data.",
        )

        ml_system = Container(
            name="ML System",
            technology='Python, Spark',
            type='Container',
            description="Train and inference of ML models.",
        )

        news_parser = Container(
            name="News Parser",
            technology='Python',
            type='Container',
            description="Processes external news for insights.",
        )

        kafka = Container(
            name="Topics Storage",
            technology=None,
            type='Kafka Topics',
            description="Manages news and market data flow"
        )

        data_exchange = Container(
            name="Data Exchange",
            technology='Spark Application',
            type='Container',
            description="Transfers data between HDFS and analytical data storage.",
        )

        analytical_data_storage = Container(
            name="Analytical Data Storage",
            technology='Clickhouse',
            type='Analytical DB',
            description="Handles analytical data for quick access.",
        )

        analytics_system = Container(
            name="Analytics System",
            technology='Python',
            type='Container',
            description="Provides in-depth market analysis.",
        )

        trading_bot = Container(
            name="Trading Bot",
            technology='Python',
            type='Container',
            description="Executes trades using predictive data.",
        )

        market_data_adapter = Container(
            name="Market Data Adapter",
            technology='Python',
            type='Container',
            description="Facilitates access to external market data.",
        )

    news = System(
        name="External News Sources",
        technology=None,
        type='External Sources',
        description="Provides current financial news.",
        external=True
    )

    market_data = System(
        name="Market Data Sources",
        technology=None,
        type='External Sources',
        description="Supplies up-to-date market data.",
        external=True
    )

    stock_exchange = System(
        name="Stock Exchange Broker",
        technology=None,
        type='External Software System',
        description="Platform for executing financial trades.",
        external=True
    )

    user >> Relationship('') >> [web, tg_bot, mobile_app]
    [web, tg_bot, mobile_app] >> Relationship('') >> application_api

    news << Relationship('News parsing') << news_parser
    news_parser << Relationship('Get news data') << kafka
    market_data << Relationship('Get market data') << market_data_adapter
    market_data_adapter << Relationship('Get market data') << kafka
    kafka >> Relationship('Write the data') >> data_storage
    kafka >> Relationship('Write the data') >> analytical_data_storage
    kafka << Relationship('Get data for trading') << trading_bot

    data_storage << Relationship('Get training data') << ml_system
    data_exchange << Relationship('Data exchange') >> analytical_data_storage
    data_storage << Relationship('Data exchange') >> data_exchange

    trading_bot >> Relationship('Get statistics') >> analytics_system
    trading_bot >> Relationship('Get predictions') >> ml_system
    trading_bot >> Relationship('Trading') >> stock_exchange

    analytics_system >> Relationship('Get analytics data') >> analytical_data_storage
    application_api >> Relationship('Get analytics') >> analytics_system
    application_api >> Relationship('Get predictions') >> ml_system
    application_api >> Relationship('Get news') >> data_storage
    application_api >> Relationship('Control the bot') >> trading_bot
