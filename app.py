from flask import Flask, render_template
import altair as alt
import pandas as pd

from models import db, migrate, Car


# create the Flask app
app = Flask(__name__)
app.config.from_object("config.Config")

# initialize plugins
db.init_app(app)
migrate.init_app(app, db)


# routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/data")
def data():
    cars_list = [
        dict(
            name=x.name,
            miles_per_gallon=x.miles_per_gallon,
            horsepower=x.horsepower,
            origin=x.origin,
        )
        for x in Car.query.all()
    ]
    cars = pd.DataFrame(cars_list)
    # make the chart
    # https://altair-viz.github.io/user_guide/interactions.html
    selection = alt.selection_point(fields=["origin"], bind="legend")
    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(
            x="horsepower:Q",
            y="miles_per_gallon:Q",
            color="origin:N",
            opacity=alt.condition(selection, alt.value(0.8), alt.value(0.2)),
            tooltip=["name", "origin", "horsepower", "miles_per_gallon"],
        )
        .add_params(selection)
    )
    return chart.to_json()
