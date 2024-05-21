from vega_datasets import data

from models import db, migrate, Car
from app import app

cars = data.cars()

rows = cars.to_dict(orient="records")

with app.app_context():
    for row in rows:
        car = Car(
            name=row["Name"],
            miles_per_gallon=row["Miles_per_Gallon"],
            cylinders=row["Cylinders"],
            displacement=row["Displacement"],
            horsepower=row["Horsepower"],
            weight=row["Weight_in_lbs"],
            acceleration=row["Acceleration"],
            year=row["Year"].to_pydatetime().year,
            origin=row["Origin"],
        )
        db.session.add(car)
        db.session.commit()
