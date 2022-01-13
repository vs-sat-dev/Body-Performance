from sqlalchemy.sql import func
import enum

from . import db


class Gender(enum.Enum):
    M = 'M'
    F = 'F'


class Class(enum.Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'


class BodyPerformance(db.Model):
    __tablename__ = 'body_performance'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender))
    height_cm = db.Column(db.Float, nullable=False)
    weight_kg = db.Column(db.Float, nullable=False)
    body_fat_pct = db.Column(db.Float, nullable=False)
    diastolic = db.Column(db.Float, nullable=False)
    systolic = db.Column(db.Float, nullable=False)
    grip_force = db.Column(db.Float, nullable=False)
    sit_and_bend_forward_cm = db.Column(db.Float, nullable=False)
    sit_ups_counts = db.Column(db.Float, nullable=False)
    broad_jump_cm = db.Column(db.Float, nullable=False)
    target_class = db.Column(db.Enum(Class))
