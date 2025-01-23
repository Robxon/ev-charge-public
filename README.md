# ChargeEV - Electric Vehicle Charging Estimator

ChargeEV is a user-friendly web application designed to help electric vehicle (EV) owners estimate charging times and visualize charging progress. By entering key vehicle specifications and charging parameters, users can predict charging durations and monitor progress through interactive charts and tables.

![alt text](https://github.com/Robxon/ev-charge-public/blob/main/assets/app_preview.png "App Preview")

## Features

- Estimate EV charging times based on vehicle specs and charging power.
- Visualize charging progress with interactive charts.
- View detailed charging stats in an easy-to-read table.
- Switch between units: Range (km) or Charge State (%).
- Intuitive interface built with Dash, Plotly, and Bootstrap for a seamless user experience.

## Technologies Used

- **Frontend**: Dash, Dash Mantine Components, Dash Bootstrap Components, Plotly
- **Backend**: Python
- **Data Visualization**: Plotly

## Installation

To run the ChargeEV web application locally, follow the steps below:

### 1. Clone the repository

git clone https://github.com/Robxon/ev-charge-public


### 2. Install the required dependencies

Navigate to the project directory and install the required Python libraries:

pip install -r requirements.txt


### 3. Run the app

After installing the dependencies, start the application by running:

py RunApp.py


The app should now be available in your browser at `http://127.0.0.1:8050`.

## Usage

Once the application is running, you can input the following parameters:

- **Vehicle specifications**: Battery capacity, charge rate, etc.
- **Charging power**: Input the charging power of the station.
- **Units**: Switch between units like range (km) or charge state (%).

The app will provide an estimated charging time, as well as an interactive chart and table showing the charging progress.


## Disclaimer

The app provides charging time estimates based on user input and is for informational purposes only. Actual results may vary due to factors like battery health and charger efficiency. The developers are not responsible for any inaccuracies, damages, or losses resulting from the use of the application. Use at your own risk.
