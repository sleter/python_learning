import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash example'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [3, 2, 9, 1, 8], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 6, 3, 6, 2], 'type': 'bar', 'name': 'Cars'},
                ],
            'layout': {
                'title': 'Basic Dash Example'
                }
            })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)

