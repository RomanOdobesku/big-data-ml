from diagrams import Diagram
from diagrams.c4 import Container, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram(filename='./docs/.png/c4_analytics_components', outformat='png', show=False, graph_attr=graph_attr):

    analytical_data_storage = Container(
        name="Analytical Data Storage",
        technology='Clickhouse',
        type='Analytical DB',
        description="Handles analytical data for quick access.",
    )

    application_api = Container(
        name="Application API",
        technology='Python, FastAPI',
        type='Container',
        description="Connects user interfaces with backend logic.",
    )

    trading_bot = Container(
        name="Trading Bot",
        technology='Python',
        type='Container',
        description="Executes trades using predictive data.",
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


    # analytics system
    data_analysis_service << Relationship('Get insights') <<  report_service
    analytical_data_storage << Relationship('Get analytics data') << data_analysis_service
    [report_service, data_analysis_service] >> Relationship('') >> analytics_system
    trading_bot >> Relationship('Get statistics') >> analytics_system
    application_api >> Relationship('Get analytics') >> analytics_system
