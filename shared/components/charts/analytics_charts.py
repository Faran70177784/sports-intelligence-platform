"""
Reusable analytics charts.
"""

import plotly.express as px
import streamlit as st


class AnalyticsCharts:
    """Reusable dashboard charts."""

    @staticmethod
    def pie_chart(
        data,
        title: str,
    ) -> None:

        if not data:
            st.info("No data available.")
            return

        labels = [x[0] for x in data]
        values = [x[1] for x in data]

        fig = px.pie(
            names=labels,
            values=values,
            title=title,
        )

        fig.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20,
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    @staticmethod
    def bar_chart(
        data,
        title: str,
        x_title: str,
        y_title: str,
    ) -> None:

        if not data:
            st.info("No data available.")
            return

        labels = [x[0] for x in data]
        values = [x[1] for x in data]

        fig = px.bar(
            x=labels,
            y=values,
            title=title,
            labels={
                "x": x_title,
                "y": y_title,
            },
        )

        fig.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20,
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )