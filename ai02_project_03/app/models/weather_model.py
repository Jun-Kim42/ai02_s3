from app import db

class Weather(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    pressure = db.Column(db.Float)
    humidity = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    speed = db.Column(db.Float)
    deg = db.Column(db.Float)
    label = db.Column(db.Integer)
    #user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

def add_weather_db(weather_dict):
    new_weather = Weather(
        id = weather_dict['id'],
        temp = weather_dict['temp'],
        pressure = weather_dict['pressure'],
        humidity = weather_dict['humidity'],
        feels_like = weather_dict['feels_like'],
        speed = weather_dict['speed'],
        deg = weather_dict['deg'],
        label = weather_dict['label'],
    )

    db.session.add(new_weather)
    db.session.commit()

    return

def delete_weahter_db(weather_id):
    data = Weather.query.filter(Weather.id == weather_id).first()
    db.session.delete(data)
    db.session.commit()

    return