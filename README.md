# Area Code Lookup

Area Code Lookup is a local application that allows users to find information about cities, states, and countries associated with specific area codes.

## Features

- Enter an area code to retrieve information about the corresponding city, state, and country.
- Handle cases where multiple cities have the same area code within a state.
- Provide a user-friendly interface to input and display the results.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/area-code-lookup.git`
2. Navigate to the project directory: `cd area-code-lookup`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Make sure you have the necessary data file (`data.csv`) in the project directory.
2. Run the application: `python app.py`
3. Open your web browser and go to `http://localhost:5000` to access the application.
4. Enter an area code in the input field and click the "Submit" button.
5. View the results displayed on the screen.

## Technologies Used

- Python
- Flask (Python web framework)
- pandas (Python library for data manipulation)
- HTML
- CSS

## File Structure

- `app.py`: The main Python file that handles the Flask application and routes.
- `data.csv`: The data file containing area code information.
- `templates/`: Directory containing HTML templates for different pages.
    - `index.html`: Home page template with the area code input form.
    - `result.html`: Template for displaying the result of a single area code search.
    - `no_result.html`: Template for displaying a message when no result is found.
    - `multiple_results.html`: Template for displaying multiple results for an area code.
- `static/`: Directory containing static files (CSS, images, etc.).
    - `style.css`: CSS file for styling the web pages.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

