from flask import Blueprint, render_template, request,redirect,url_for
from app.models import weather_model
from app.utils import main_func

bp = Blueprint('predict', __name__)

@bp.route('/predict/', methods=['Get','Post'])
def predict():
    
    return render_template('predict.html')

@bp.route('/predict/result')
def predict_label():
    pred = main_func.predict_condition()
    prediction_n = pred[0]
    if prediction_n == 0:
        prediction = 'walk'
    if prediction_n == 1:
        prediction = 'run'
    a =1
    return render_template('predict.html',prediction = prediction)