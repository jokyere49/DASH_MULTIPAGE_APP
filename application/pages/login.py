from dash import dcc, html, callback, Input, Output, State
from application import db
from application.models import User
from flask_login import login_user

layout =  html.Div([dcc.Location(id='url_login', refresh=True)
            , html.H2('''Please log in to continue:''', id='h1')
            , dcc.Input(placeholder='Enter your username',
                    type='text',
                    id='uname-box')
            , dcc.Input(placeholder='Enter your password',
                    type='password',
                    id='pwd-box')
            , html.Button(children='Login',
                    n_clicks=0,
                    type='submit',
                    id='login-button')
            , html.Div(children='', id='output-state')
        ]) #end div

@callback(
    Output('url_login', 'pathname')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def successful(n_clicks, username, password):
    user = User.query.filter_by(username=username).first()
    # you can throw an error is not found will work on that later
    if user is not None:
        if user.check_password(password):
            login_user(user)
            return '/success'
        else:
            pass
    else: 
        pass

@callback(
    Output('output-state', 'children')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def update_output(n_clicks, username, password):
    if n_clicks > 0:
        user = User.query.filter_by(username=username).first()
        if user is not None:
            if user.check_password(password):
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''