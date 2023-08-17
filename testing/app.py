# Import necessary libraries
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
statement = pd.read_csv(r"Categorized_Credit.csv")
df = pd.DataFrame(statement)

def convert_to_float(value):
    try:
        if '(' in value and ')' in value:
            return -float(value.replace('(', '').replace(')', '').replace('$', '').replace(',', ''))
        else:
            return float(value.replace('$', '').replace(',', ''))
    except ValueError:
        return value

# Convert the 'Amount' column to float
df['Amount'] = df['Amount'].apply(convert_to_float)

# Create a Plotly Express figure
fig = px.bar(df, x='Description', y='Amount', color='Category', title='Transaction Amounts by Description')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Interactive Transaction Data Dashboard"),
    dcc.Graph(id='graph', figure=fig),
    html.Label("Select Category:"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': category, 'value': category} for category in df['Category'].unique()],
        value=df['Category'].unique().tolist(),
        multi=True
    )
])

# Callback to update the graph based on user input
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('category-dropdown', 'value')]
)
def update_graph(selected_categories):
    filtered_df = df[df['Category'].isin(selected_categories)]
    fig = px.bar(filtered_df, x='Description', y='Amount', color='Category', title='Transaction Amounts by Description')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
