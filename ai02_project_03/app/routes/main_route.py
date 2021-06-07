from flask import Blueprint, render_template, request,url_for
from werkzeug.utils import redirect
from app.models import weather_model
from app.services import weather_api


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/weather_update/', methods=['Get'])
def weather_index():
    weather_list = weather_model.Weather.query.all()
    return render_template('weather.html',weather_list=weather_list)


@bp.route('/api/weather_update/<int:label>')
def add_label(label=None):

    weather_dict = weather_api.get_current_weather()
    weather_dict['label'] = label
    weather_model.add_weather_db(weather_dict)

    return redirect(url_for('main.weather_index'))

@bp.route('/api/weather_update/del/<int:weather_id>')
def delete_label(weather_id=None):
    weather_model.delete_weahter_db(weather_id)
    return redirect(url_for('main.weather_index'))