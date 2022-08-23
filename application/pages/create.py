from dash import dcc, html, callback, Input, Output, State
from application import db
from application.models import User
from application.pages import login
import dash

layout= html.Div([ html.H1('Create User Account')
        , dcc.Location(id='create_user', refresh=True)
        , dcc.Input(id="username"
            , type="text"
            , placeholder="user name"
            , maxLength =15)
        , dcc.Input(id="password"
            , type="password"
            , placeholder="password")
        , dcc.Input(id="email"
            , type="email"
            , placeholder="email"
            , maxLength = 50)
        , html.Button('Create User', id='submit-val', n_clicks=0)
        , html.Div(
        [html.Div([html.H2('Already have a user account?'), 
        dcc.Link('Click here to Log In', href='/login')])])
    ])#end div

@callback(
   Output('create_user', 'pathname'),
    [Input('submit-val', 'n_clicks')],
    [State('username', 'value'), 
    State('password', 'value'), 
    State('email', 'value')]
    )
def insert_users(n_clicks, username, password, email):
    
    if username is not None and password is not None and email is not None:
        user = User(email=email, username=username,
                    password = password)
        db.session.add(user)
        db.session.commit()
        return '/login'
    
    return dash.no_update
    #else:
        #return [html.Div([html.H2('Already have a user account?'), 
        #dcc.Link('Click here to Log In', href='/login')])]

    