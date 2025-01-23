from dash import html, dcc, State, Input, Output, ctx
import dash_bootstrap_components as dbc
import dash
import flask

app = dash.Dash(__name__,
                use_pages=True,
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                ],
                title="ChargeEV",
                update_title="ChargeEV | Loading...",
                assets_folder="assets",
                include_assets_files=True)

app.title = "EV Charge Stats"
app.css.config.serve_locally = True
server = app.server

app.layout = html.Div([
    dbc.Alert(
        [
            html.P(
                [
                    "Cookies help us deliver the best experience on our website. By using the website you agree to the use of the cookies. ",
                    html.A("Find out how we use cookies.", href="/privacy-policy",
                           target="_blank", style={"display": "inline"})
                ]
            ),
            dbc.Button("Got it!", color="success",
                       className="ms-auto me-auto d-block w-75", id="got-it-btn"),
        ],
        color="warning",
        className="alert-container ",
        dismissable=False,
        is_open=False,
        id='cookies-alert'
    ),
    # Top section
    html.Div(
        [
            html.Div("Logo", className="search-bar"),
            html.Div("Username", className="user-profile"),
        ],
        className="top-section",
        style={"position": "relative", "z-index": 1},
    ),
    html.Div(
        children=dash.page_container,
        style={"position": "relative", "z-index": 1},
    ),
    html.Footer(
        [
            html.Div([
                html.Div("Contact us at: example@mail.com"),
                html.Div("Made by Robert Kowalski"),
                html.Div("© EVXXXXXX. All rights reserved."),
            ], style={"width": "90%", "display": "flex", "justify-content": "space-between"})
        ],
        className="",
        style={"position": "relative", "z-index": 1},
    ),
])


@app.callback(
    Output('cookies-alert', 'is_open'),
    Input('got-it-btn', 'n_clicks'),
)
def manage_cookies_consent(n_clicks):
    trigger = ctx.triggered_id
    all_cookies = dict(flask.request.cookies)
    if all_cookies:
        if all_cookies['cookies_consent_given'] == 'true':
            return False
    elif n_clicks is not None and trigger == 'got-it-btn':
        if n_clicks > 0:
            dash.callback_context.response.set_cookie(
                'cookies_consent_given', 'true', max_age=604800)
            return False
    return True


if __name__ == "__main__":
    app.run_server(debug=True)
