from diagrams import Diagram
from diagrams.c4 import Container, SystemBoundary, Relationship

from diagrams.programming.framework import Fastapi

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_api_components', outformat='png', show=False, graph_attr=graph_attr):

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

    ml_system = Container(
        name="ML System",
        technology='Python, Spark',
        type='Container',
        description="Train and inference of ML models.",
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

    # application api
    application_api >> Relationship('Get predictions') >> ml_system
    [web, tg_bot, mobile_app]  >> Relationship('') >> application_api
    application_api >> Relationship('') >> [auth_service, trading_service, user_profile_service, news_service, analytics_service]
    news_service >> Relationship('Get news') >> data_storage
    analytics_service >> Relationship('Get analytics') >> analytics_system
    trading_service >> Relationship('Control the bot') >> trading_bot
    user_profile_service >> Relationship('Get users data') >> data_storage