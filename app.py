from flask import Flask, render_template, request, send_from_directory
import create_data
import os

app = Flask(__name__)

# Remove existing plot.png if it exists
if os.path.exists("static/plot.png"):
    os.remove("static/plot.png")


@app.route('/', methods=['GET', 'POST'])
def index():
    image_path = None

    if request.method == 'POST':
        disease = request.form['disease']
        pop_size = int(request.form['pop_size'])
        init_infected = int(request.form['init_infected'])
        sim_days = int(request.form['sim_days'])

        if disease == "Custom...":
            min_recovery_time = int(request.form['min_recovery_time'])
            max_recovery_time = int(request.form['max_recovery_time'])
            create_data.create_data(disease, pop_size, init_infected, sim_days, min_recovery_time, max_recovery_time)
        else:
            create_data.create_data(disease, pop_size, init_infected, sim_days, 0, 0)

        image_path = '/static/plot.png'

    return render_template('index.html', image_path=image_path)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)
