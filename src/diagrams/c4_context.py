from diagrams import Diagram
from diagrams.c4 import Person, Container, System, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_context', outformat='png', direction="TB", show=False, graph_attr=graph_attr):
    customer = Person(
        name="User", description=""
    )

    trading_system = Container(
        name="Trading System",
        technology=None,
        type='Software system',
        description="",
    )

    news = System(
        name="External News Sources",
        technology=None,
        type='External Sources',
        description="",
        external=True
    )

    stock_exchange = System(
        name="Stock Exchange",
        technology=None,
        type='External Software System',
        description="",
        external=True
    )


    customer >> Relationship('Visits website using [HTTPS]') >> trading_system
    trading_system >> Relationship('News parsing') >> news
    trading_system << Relationship('Getting stock quotes and trading by API') >> stock_exchange

