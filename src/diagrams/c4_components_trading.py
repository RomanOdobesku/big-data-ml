from diagrams import Diagram
from diagrams.c4 import Container, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_trading_components', outformat='png', show=False, graph_attr=graph_attr):

    kafka = Container(
        name="Topics Storage",
        technology=None,
        type='Kafka Topics',
        description="Manages news and market data flow"
    )

    analytics_system = Container(
        name="Analytics System",
        technology='Python',
        type='Container',
        description="Provides in-depth market analysis.",
    )

    ml_system = Container(
        name="ML System",
        technology='Python, Spark',
        type='Container',
        description="Train and inference of ML models.",
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

    stock_exchange = System(
        name="Stock Exchange Broker",
        technology=None,
        type='External Software System',
        description="Platform for executing financial trades.",
        external=True
    )

    # trading bot
    risk_management_component >> Relationship('') >> trading_bot
    kafka << Relationship('Get data for risk management') << risk_management_component
    kafka << Relationship('Get data for trading') << trading_bot
    trading_bot >> Relationship('Get statistics') >> analytics_system
    trading_bot >> Relationship('Get predictions') >> ml_system
    trading_bot >> Relationship('Trading') >> stock_exchange
