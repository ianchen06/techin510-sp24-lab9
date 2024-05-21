import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Car(db.Model):
    __tablename__ = "cars"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128))
    miles_per_gallon = sa.Column(sa.Float)
    cylinders = sa.Column(sa.Integer)
    displacement = sa.Column(sa.Float)
    horsepower = sa.Column(sa.Float)
    weight = sa.Column(sa.Float)
    acceleration = sa.Column(sa.Float)
    year = sa.Column(sa.Integer)
    origin = sa.Column(sa.String(128))
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(
        sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now()
    )

    def __repr__(self):
        return f"<Car {self.name}>"
