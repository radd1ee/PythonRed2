from flask import Flask, render_template, request
from funcs import check_bad_weather, validate_coordinates, validate_city_name, get_weather_by_coordinates, get_weather_by_city
from API import api_key

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('selection_form.html')

@app.route('/weather_choice', methods=['POST'])
def weather_choice():
    choice = request.form['choice']
    if choice == 'coordinates':
        return render_template('coordinates_form.html')
    elif choice == 'cities':
        return render_template('city_form.html')

@app.route('/weather_by_coordinates', methods=['POST'])
def weather_by_coordinates():
    lat1 = request.form['lat1']
    lon1 = request.form['lon1']

    is_valid1, error_message1 = validate_coordinates(lat1, lon1)

    if not is_valid1:
        return render_template('error.html', message=f"Ошибка для точки 1: {error_message1}")

    weather_point1 = get_weather_by_coordinates(lat1, lon1)

    bad_weather_point1 = check_bad_weather(weather_point1)

    return render_template('weather_result_two_points.html',
                            point1=weather_point1, result1=bad_weather_point1,)

@app.route('/weather_by_cities', methods=['POST'])
def weather_by_cities():
    city1 = request.form['city1']

    is_valid1, error_message1 = validate_city_name(city1)

    if not is_valid1:
        return render_template('error.html', message=f"Ошибка для города 1: {error_message1}")

    weather_city1 = get_weather_by_city(city1)

    bad_weather_city1 = check_bad_weather(weather_city1)

    return render_template('weather_result_two_points.html',
                            point1=weather_city1, result1=bad_weather_city1,)


if __name__ == '__main__':
    app.run(debug=True)