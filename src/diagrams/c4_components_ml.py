from diagrams import Diagram
from diagrams.c4 import Container, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_ml_components', outformat='png', show=False, graph_attr=graph_attr):

    data_storage = Container(
        name="Data Storage",
        technology=None,
        type='HDFS',
        description="Stores a variety of trading-related data.",
    )

    trading_bot = Container(
        name="Trading Bot",
        technology='Python',
        type='Container',
        description="Executes trades using predictive data.",
    )

    application_api = Container(
        name="Application API",
        technology='Python, FastAPI',
        type='Container',
        description="Connects user interfaces with backend logic.",
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

    # ml system
    data_storage << Relationship('Get training data') << ml_training_component
    trading_bot >> Relationship('Get predictions') >> ml_system
    application_api >> Relationship('Get predictions') >> ml_system
