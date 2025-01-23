import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/privacy-policy')

policy_text = '''
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris a gravida ex, 
iaculis pulvinar sapien. Donec aliquam venenatis massa, sed rhoncus metus iaculis id. 
Aliquam iaculis eu eros et dignissim. Nunc tempus felis ut pulvinar venenatis. 
In molestie odio et orci placerat tincidunt. Etiam tempus viverra aliquam. Sed elementum 
est non nunc aliquet, non fermentum arcu consectetur.
Cras quis nisi dolor. Vestibulum vitae ligula nisl. Cras et turpis nec dolor dictum 
dictum sed eget diam. Suspendisse ac pharetra lectus, et mollis diam. Cras tristique mattis 
vehicula. Aliquam eget dictum eros, quis efficitur velit. Nunc ac ipsum sed metus condimentum 
sollicitudin. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante 
ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse 
vel elementum mi. Curabitur at convallis sem. Mauris eu porta sapien.
Integer malesuada eros eget egestas cursus. Donec fringilla turpis eu odio ornare, nec 
rhoncus sem dignissim. Vivamus euismod nulla sit amet efficitur tincidunt. In tempor lobortis 
elementum. Mauris sit amet enim arcu. Orci varius natoque penatibus et magnis dis parturient 
montes, nascetur ridiculus mus. Praesent tempus condimentum orci, nec elementum arcu tincidunt 
in. Pellentesque ligula odio, tincidunt at sapien suscipit, pharetra efficitur nisi. In tortor 
lectus, cursus id hendrerit quis, mollis at purus. Vivamus nec tortor congue, pellentesque risus 
sit amet, vulputate erat. Interdum et malesuada fames ac ante ipsum primis in faucibus.
Donec quis interdum lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
Phasellus laoreet bibendum diam sed ullamcorper. Cras at neque in turpis fermentum aliquam 
quis eget massa. In sed nisl posuere, elementum elit vel, pretium enim. Maecenas eget 
condimentum mi, sit amet placerat nisi. Etiam tempor congue turpis, ac condimentum tellus 
fringilla vitae. Pellentesque congue in dolor vel aliquet. Vivamus maximus est lectus, a 
tristique risus molestie non. Phasellus gravida sem nec enim tempus, facilisis sagittis erat 
fermentum. Cras sed purus a turpis consequat maximus. 
'''

layout = html.Div(
    html.Div(
        dbc.Card([
            dbc.CardBody([
                html.H3("PRIVACY POLICY", className="card-title"),
                html.Div([
                    html.P(3*policy_text),
                ]),
            ]),
        ]),
        className='privacy-policy-section'
    ),

    className="main")
