from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('data.csv')
grouped_data = data.groupby(['Number', 'State'])

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    userInfo = int(request.form['area_code'])
    matching_group = None
    for key in grouped_data.indices.keys():
        if key[0] == userInfo:
            matching_group = key
            break

    if matching_group:
        area_code_data = grouped_data.get_group(matching_group)
        if len(area_code_data) > 1:
            results = []
            for _, row in area_code_data.iterrows():
                specific = f"City: {row['City']}, State: {row['State']}, Country: {row['Country']}"
                results.append(specific)
            return render_template('multiple_results.html', results=results)
        else:
            specific = f"City: {area_code_data['City'].iloc[0]}, State: {area_code_data['State'].iloc[0]}, Country: {area_code_data['Country'].iloc[0]}"
            return render_template('single_result.html', result=specific)
    else:
        return render_template('no_result.html')

if __name__ == '__main__':
    app.run(debug=True)
