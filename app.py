from application import app, engine, db
from dash import html, dcc, Input , Output, callback 
from application.pages import create, data, failed, login, logout, success
from flask_login import current_user, logout_user
from application.models import User
from flask import redirect

# create the initial database
User.metadata.create_all(engine)
#user1 = User(email='test1@test.com', username='joky',
#                    password = 'password')

#db.session.add(user1)
#db.session.commit()

app.layout= html.Div([
            html.Div(id='page-content', className='content')
            ,  dcc.Location(id='url', refresh=False)
        ])

@callback(
    Output('url', 'pathname'),
    Output('page-content', 'children')
    , [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return '/', create.layout
    elif pathname == '/login':
        return '/login', login.layout
    elif pathname == '/success':
        if current_user.is_authenticated:
            return '/success', success.layout
        else:
            return '/failed', failed.layout
    elif pathname =='/data':
        if current_user.is_authenticated:
            return '/data', data.layout
        else:
            return '/login', login.layout
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return '/logout', logout.layout
        else:
            return '/logout', logout.layout
    else:
        return '404'




if __name__ == '__main__':
    app.run_server(debug=True)