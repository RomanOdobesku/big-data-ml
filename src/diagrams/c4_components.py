from diagrams import Diagram
from diagrams.c4 import Person, Container, System, SystemBoundary, Relationship

from diagrams.programming.framework import Fastapi

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_components', outformat='png', show=False, graph_attr=graph_attr):
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

        data_storage = Container(
            name="Data Storage",
            technology=None,
            type='HDFS',
            description="Stores a variety of trading-related data.",
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

        market_data_adapter = Container(
            name="Market Data Adapter",
            technology='Python',
            type='Container',
            description="Facilitates access to external market data.",
        )

        with SystemBoundary("Application API"):
            application_api = Fastapi('Application API')

            auth_service = Container(
                name="Authentication Service",
                technology=None,
                type='Component',
                description="Manages user authentication and authorization.",
            )

            trading_service = Container(
                name="Trading Service",
                technology=None,
                type='Component',
                description="Handles trading operations and transactions.",
            )

            user_profile_service = Container(
                name="User Profile Service",
                technology=None,
                type='Component',
                description="Manages user profile data.",
            )

            news_service = Container(
                name="News Service",
                technology=None,
                type='Component',
                description="Manages news data.",
            )

            analytics_service = Container(
                name="Analytics Service",
                technology=None,
                type='Component',
                description="Manages analytics data.",
            )

        with SystemBoundary("ML System"):
            ml_system = Container(
                name="ML Inference Component",
                technology=None,
                type='Component',
                description="Performs the inference of the model.",
            )

            ml_training_component = Container(
                name="ML Training Component",
                technology='Python, Spark',
                type='Component',
                description="Fit models using Spark ML.",
            )

        with SystemBoundary("Analytics System"):
            analytics_system = Container(
                name="Analytics Component",
                technology=None,
                type='Component',
                description="Provides in-depth market analysis.",
            )

            report_service = Container(
                name="Report Service",
                technology=None,
                type='Component',
                description="Generates trading reports and analytics.",
            )

            data_analysis_service = Container(
                name="Data Analysis Service",
                technology=None,
                type='Component',
                description="Performs data analysis for market insights.",
            )

        with SystemBoundary("Trading Bot"):
            trading_bot = Container(
                name="Trading Bot",
                technology=None,
                type='Component',
                description="Executes trades using predictive data.",
            )

            risk_management_component = Container(
                name="Risk Management Component",
                technology=None,
                type='Component',
                description="Manages risk associated with automated trading.",
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

    news << Relationship('News parsing') << news_parser
    news_parser << Relationship('Get news data') << kafka
    market_data << Relationship('Get market data') << market_data_adapter
    market_data_adapter << Relationship('Get market data') << kafka
    kafka >> Relationship('Write the data') >> data_storage
    kafka >> Relationship('Write the data') >> analytical_data_storage

    data_exchange << Relationship('Data exchange') >> analytical_data_storage
    data_storage << Relationship('Data exchange') >> data_exchange

    # application api
    application_api >> Relationship('Get predictions') >> ml_system
    [web, tg_bot, mobile_app]  >> Relationship('') >> application_api
    application_api >> Relationship('') >> [auth_service, trading_service, user_profile_service, news_service, analytics_service]
    news_service >> Relationship('Get news') >> data_storage
    analytics_service >> Relationship('Get analytics') >> analytics_system
    trading_service >> Relationship('Control the bot') >> trading_bot
    user_profile_service >> Relationship('Get users data') >> data_storage

    # ml system
    data_storage << Relationship('Get training data') << ml_training_component

    # analytics system
    data_analysis_service << Relationship('Get insights') <<  report_service
    analytical_data_storage << Relationship('Get analytics data') << data_analysis_service
    [report_service, data_analysis_service] >> Relationship('') >> analytics_system

    # trading bot
    risk_management_component >> Relationship('') >> trading_bot
    kafka << Relationship('Get data for risk management') << risk_management_component
    kafka << Relationship('Get data for trading') << trading_bot
    trading_bot >> Relationship('Get statistics') >> analytics_system
    trading_bot >> Relationship('Get predictions') >> ml_system
    trading_bot >> Relationship('Trading') >> stock_exchange
