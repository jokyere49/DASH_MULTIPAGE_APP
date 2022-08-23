from dash import dcc, html, Input , Output , callback


layout = html.Div([dcc.Dropdown(
                    id='dropdown',
                    options=[{'label': i, 'value': i} for i in ['Day 1', 'Day 2']],
                    value='Day 1')
                , html.Br()
                , html.Div([dcc.Graph(id='graph')])
            ]) #end div

@callback(
    [Output('graph', 'figure')]
    , [Input('dropdown', 'value')])
def update_graph(dropdown_value):
    if dropdown_value == 'Day 1':
        return [{'layout': {'title': 'Graph of Day 1'}
                , 'data': [{'x': [1, 2, 3, 4]
                    , 'y': [4, 1, 2, 1]}]}]
    else:
        return [{'layout': {'title': 'Graph of Day 2'}
                ,'data': [{'x': [1, 2, 3, 4]
                    , 'y': [2, 3, 2, 4]}]}]