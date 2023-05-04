from flask import Flask, request

from service import weather_service

app = Flask(__name__)

@app.route("/hello-world")
def get_hello_flask():
    return {"msg": "Hello Flask"}


@app.route("/weather-info", methods=["GET"])
def get_weather_info():
    lat= float(request.args.get("lat", default=0.00))
    lng = float(request.args.get("lng", default=0.00))

    content = weather_service.get_temperature(lat=lat, lng=lng)

    print(content is None)

    if content is None:
        return {"msg": "erro ao fazer a requisição"}

    return content


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')