from flask import Blueprint, render_template, request, flash

from .model import BodyPerformance
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        username = request.form.get('username')
        age = request.form.get('age')
        gender = request.form.getlist('gender')
        height_cm = request.form.get('height_cm')
        weight_kg = request.form.get('weight_kg')
        body_fat_pct = request.form.get('body_fat_pct')
        diastolic = request.form.get('diastolic')
        systolic = request.form.get('systolic')
        grip_force = request.form.get('gripForce')
        sit_and_bend_forward_cm = request.form.get('sit_and_bend_forward_cm')
        sit_ups_counts = request.form.get('sit_ups_counts')
        broad_jump_cm = request.form.get('broad_jump_cm')

        if len(username) < 2 or len(username) > 40:
            flash('Incorrect name length', category='error')
        elif float(age) < 0.0 or float(age) > 150:
            flash('Incorrect age', category='error')
        elif gender[0] not in ['F', 'M']:
            flash('Incorrect gender', category='error')
        elif float(height_cm) < 0.0 or float(height_cm) > 250:
            flash('Incorrect height', category='error')
        elif float(weight_kg) < 0.0 or float(weight_kg) > 500.0:
            flash('Incorrect weight', category='error')
        elif float(body_fat_pct) < 0.0 or float(body_fat_pct) > 100.0:
            flash('Incorrect body fat %', category='error')
        elif float(diastolic) < 0.0 or float(diastolic) > 300:
            flash('Incorrect diastolic', category='error')
        elif float(systolic) < 0.0 or float(systolic) > 400.0:
            flash('Incorrect systolic', category='error')
        elif float(grip_force) < 0 or float(grip_force) > 100.0:
            flash('Incorrect grip force', category='error')
        elif float(sit_and_bend_forward_cm) < -100.0 or float(sit_and_bend_forward_cm) > 500:
            flash('Incorrect sit and bend forward cm', category='error')
        elif float(sit_ups_counts) < 0 or float(sit_ups_counts) > 150:
            flash('Incorrect sit-ups counts', category='error')
        elif float(broad_jump_cm) < 0.0 or float(broad_jump_cm) > 400:
            flash('Incorrect broad jump cm', category='error')
        else:
            model_prediction = 'A'
            new_result = BodyPerformance(username=username,
                                         age=age, gender=gender[0], height_cm=height_cm,
                                         weight_kg=weight_kg, body_fat_pct=body_fat_pct,
                                         diastolic=diastolic, systolic=systolic, grip_force=grip_force,
                                         sit_and_bend_forward_cm=sit_and_bend_forward_cm,
                                         sit_ups_counts=sit_ups_counts, broad_jump_cm=broad_jump_cm,
                                         target_class=model_prediction)
            db.session.add(new_result)
            db.session.commit()
            db.session.refresh(new_result)
            print(f'new_result: {new_result}')
            return render_template('predicted_class.html')

    return render_template('home.html')
