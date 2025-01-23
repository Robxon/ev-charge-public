import dash
from dash import html, dcc, dash_table, Input, Output, State, _callback_context, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import plotly.graph_objects as go
from datetime import datetime, timedelta
import math


def serve_layout():
    app_layout = html.Div(
        [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        dbc.Card(
                            [
                                html.H3("Welcome to EV Charge Estimator"),
                                html.P(
                                    "This tool is here to help you estimate your electric vehicle's charging parameters and visualize the charging progress. By entering your vehicle's specifications, you can predict how long your car might take to charge, considering various factors. Let's get started with your vehicle's details!"
                                ),
                                html.Hr(),  # Adding a horizontal line for separation
                                html.H4("Quick Guide"),
                                html.P(
                                    "Here's a quick guide to get you started:"),
                                html.Ol([
                                    html.Li(
                                        "Choose the date and time for the charging estimate."),
                                    html.Li(
                                        "Input your car's charging power in kilowatts (kW)."),
                                    html.Li(
                                        "Enter your car's maximum range in kilometers (km)."),
                                    html.Li(
                                        "Set the initial state of charge as a percentage."),
                                    html.Li(
                                        "Type in the battery capacity in kilowatt-hours (kWh)."),
                                    html.Li(
                                        "Pick how you want to view the progress - 'Range (km)' or 'Charge State (%)'."),
                                ]),
                                html.P(
                                    "Get ready for a charging chart and a table with estimated stats."),
                                html.P(
                                    "Please remember, it's an estimate based on ideal conditions; actual charging times might vary!"),
                            ],
                            className="info-section result-card",
                        ),
                    ],
                        width=8),
                    dbc.Col([
                        dbc.Card([
                            html.H2("Set Up Your Ride"),
                            html.Div([
                                html.H6("Current time"),
                                html.Div([
                                    dmc.DatePicker(
                                        id="actual-date",
                                        label="Date",
                                        value=datetime.now().date(),
                                        style={"width": "48%"},
                                        clearable=False,
                                        icon=DashIconify(icon="wpf:calendar"),
                                    ),
                                    dmc.TimeInput(
                                        label="Time",
                                        icon=DashIconify(
                                            icon="teenyicons:clock-outline"),
                                        id="actual-time",
                                        value="2023-10-12T00:00:00",
                                        format=24,
                                        style={"width": "48%"}),
                                ],
                                    className='inputs-section'),

                            ],
                                className='inputs-wrapper mt-3 mb-3'
                            ),
                            html.Div([
                                html.H6("Vehicle specs 🚗"),
                                html.Div([
                                    html.Div([
                                        dbc.Label("Max Range"),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(
                                                    placeholder="Max Range",
                                                    id="max-range",
                                                    type='number',
                                                    value=250,
                                                    min=0,
                                                    step=0.01),
                                                dbc.InputGroupText("km"),
                                            ],
                                        ),
                                    ],
                                        style={"width": "48%"}),
                                    html.Div([
                                        dbc.Label("Battery Capacity"),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(
                                                    placeholder="Battery Capacity",
                                                    id="battery-capacity",
                                                    type='number',
                                                    value=50,
                                                    min=0,
                                                    step=0.01),
                                                dbc.InputGroupText("kWh"),
                                            ],
                                        ),
                                    ],
                                        style={"width": "48%"}),
                                ],
                                    className='inputs-section'),

                            ],
                                className='inputs-wrapper mt-3 mb-3'
                            ),

                            html.Div([
                                html.H6("Charging parameters 🔌"),
                                html.Div([
                                    html.Div([
                                        dbc.Label("Charging Power"),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(
                                                    placeholder="Charging Power",
                                                    id="charging-power",
                                                    type='number',
                                                    value=5,
                                                    min=0,
                                                    step=0.01),
                                                dbc.InputGroupText("kW"),
                                            ],
                                        ),
                                    ],
                                        style={"width": "48%"}
                                    ),
                                    html.Div([
                                        dbc.Label("Initial State of Charge"),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(
                                                    placeholder="Initial State of Charge",
                                                    id="initial-soc",
                                                    type='number',
                                                    value=0,
                                                    min=0,
                                                    step=0.01),
                                                dbc.InputGroupText("%"),
                                            ],
                                        ),
                                    ],
                                        style={"width": "48%"}),
                                ],
                                    className='inputs-section'),

                            ],
                                className='inputs-wrapper mt-3 mb-3'
                            ),
                        ],
                            className="result-card"),
                    ],
                        width=4),
                ]),
                html.Hr(),
                # Main Section
                html.Div(
                    dbc.Row([
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H3("Charging Visualization"),
                                    dmc.SegmentedControl(
                                        id="unit-selector",
                                        value="km",
                                        data=[
                                            {"value": "km",
                                             "label": "Range (km)"},
                                            {"value": "%",
                                             "label": "Charge State (%)"},
                                        ],
                                        style={"width": '30%'},
                                        radius="lg"
                                    ),
                                    dcc.Graph(id='charging-chart'),
                                ],
                                className="result-card",
                            ),
                            width=8
                        ),
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H3("Charging Progress"),
                                    dash_table.DataTable(id='data-table', columns=[
                                        {'name': 'Time', 'id': 'time'},
                                        {'name': 'SoC (%)',
                                         'id': 'state_of_charge'},
                                        {'name': 'Range (km)', 'id': 'range'}],
                                        style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                    },
                                        fill_width=False,
                                        tooltip_header={
                                        'state_of_charge': 'State of Charge'},
                                        page_current=0,
                                        page_size=12,
                                        page_action='native',
                                        style_cell={'textAlign': 'center'},
                                        # virtualization=True,
                                    )
                                ],
                                className="result-card",
                            ),
                            width=4,
                        )
                    ]
                    )
                )],
                className="app-container")
        ],
        className="main",
    )
    return app_layout


dash.register_page(__name__,
                   path='/',
                   title="ChargeEV",
                   update_title="ChargeEV | Loading...",
                   assets_folder="assets",
                   include_assets_files=True)
layout = serve_layout()


@callback(
    Output('charging-chart', 'figure'),
    Output('data-table', 'data'),
    Output('data-table', 'page_count'),
    Input('actual-time', 'value'),
    Input('actual-date', 'value'),
    Input('charging-power', 'value'),
    Input('initial-soc', 'value'),
    Input('battery-capacity', 'value'),
    Input('unit-selector', 'value'),
    Input('max-range', 'value')
)
def update_charging_chart(actual_time, actual_date, charging_power, initial_soc_percentage, battery_capacity, unit, max_range):

    if actual_time is None:
        return dash.no_update

    selected_time = datetime.strptime(actual_time, "%Y-%m-%dT%H:%M:%S").time()
    selected_date = datetime.strptime(actual_date, "%Y-%m-%d").date()
    actual_datetime = datetime.combine(selected_date, selected_time)

    initial_soc = initial_soc_percentage / 100.0

    time_intervals = [actual_datetime]
    state_of_charge = [initial_soc]
    data_table_data = [{'time': actual_datetime.strftime('%d %b. %H:%M'), 'state_of_charge': round(
        initial_soc * 100, 2), 'range': round(initial_soc * max_range, 2)}]

    while state_of_charge[-1] < 1.0:
        time_intervals.append(time_intervals[-1] + timedelta(hours=1))
        delta_soc = charging_power / battery_capacity
        next_soc = state_of_charge[-1] + delta_soc
        if next_soc > 1.0:
            time_intervals.pop()
            time_intervals.append(time_intervals[-1] + timedelta(minutes=30))
            delta_soc = charging_power / battery_capacity / 2
            next_soc = state_of_charge[-1] + delta_soc
            if next_soc > 1.0:
                time_intervals.pop()
                time_intervals.append(
                    time_intervals[-1] + timedelta(minutes=15))
                delta_soc = charging_power / battery_capacity / 4
                next_soc = state_of_charge[-1] + delta_soc
                if next_soc > 1.0:
                    time_intervals.pop()
                    time_intervals.append(
                        time_intervals[-1] + timedelta(minutes=5))
                    delta_soc = charging_power / battery_capacity / 12
                    next_soc = state_of_charge[-1] + delta_soc
                    if next_soc > 1.0001:
                        time_intervals.pop()
                        time_intervals.append(
                            time_intervals[-1] + timedelta(minutes=1))
                        delta_soc = charging_power / battery_capacity / 60
                        next_soc = state_of_charge[-1] + delta_soc
                        if next_soc > 1.0001:
                            break
        state_of_charge.append(next_soc)
        data_table_data.append({'time': time_intervals[-1].strftime('%d %b. %H:%M'), 'state_of_charge': round(
            state_of_charge[-1] * 100, 2), 'range': round(state_of_charge[-1] * max_range, 2)})

    if unit == 'km':
        values = [x * max_range for x in state_of_charge]
        y_title = 'Range (km)'
        y_color = 'blue'
        fill_color = 'rgba(134, 187, 210, 0.5)'
    else:
        values = [x * 100 for x in state_of_charge]
        y_title = 'State of Charge (%)'
        y_color = '#3d7b6b'
        fill_color = 'rgba(134, 187, 162, 0.5)'

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=time_intervals,
        y=values,
        mode='lines',
        name=y_title,
        line={'color': y_color},
        fill='tozeroy',
        fillcolor=fill_color
    ))

    fig.update_layout(
        title='EV Charging progress',
        xaxis_title='Time',
        yaxis_title=y_title,
        showlegend=False,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        yaxis=dict(showgrid=True, gridcolor='black'),
        xaxis=dict(showgrid=True),
        font={'family': 'Poppins'},
        modebar={'bgcolor': 'white'}
    )
    return fig, data_table_data, math.ceil(len(state_of_charge) / 10)
