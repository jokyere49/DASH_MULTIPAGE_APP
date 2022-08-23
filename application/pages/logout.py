from dash import dcc, html, Input, Output, callback
from application.pages import login

layout = html.Div([dcc.Location(id='logout', refresh=True)
        , html.Br()
        , html.Div(html.H2('You have been logged out - Please login'))
        , html.Br()
        , html.Div([login.layout])
        , html.Button(id='back-button', children='Go back', n_clicks=0)
    ])#end div

@callback(
    Output('logout', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'