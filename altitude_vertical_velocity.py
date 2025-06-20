import plotly.graph_objs as go
from plotly.io import write_html

def plot_2d_altitude_vs_vertical_velocity(dataframes, names, hurricanename,colors, output_file_2d):
    """
    Generate a 2D scatter plot for altitude vs. vertical velocity.

    Parameters:
    - dataframes: List of pandas DataFrames containing trajectory data.
    - names: List of names corresponding to each DataFrame (for legends).
    - hurricanename: Name of the hurricane for the plot title.
    - output_file_2d: File name to save the HTML 2D plot.
    """
    traces = []

    for i, df in enumerate(dataframes):
        trace = go.Scatter(
            x=df['Altitude'],
            y=df['Vertical Velocity'],
            mode='markers',
            name=names[i],
            marker=dict(
                size=6,
                color=colors[i],  # Customize marker color
                opacity=0.7
            ),
            text=(
                "Altitude: " + df['Altitude'].astype(str) +
                "<br>Vertical Velocty: " + df['Vertical Velocity'].astype(str)
            ),
            hoverinfo='text'
        )
        traces.append(trace)

    # Layout
    layout = go.Layout(
        title=dict(text=f'{hurricanename} Altitude vs. Vertical Velocity'),
        xaxis=dict(
            title='Altitude (m)',
            showgrid=True
        ),
        yaxis=dict(
            title='Vertical Velocity',
            showgrid=True
        ),
        legend=dict(
            font=dict(size=10),
            bgcolor='rgba(255, 255, 255, 0.8)',
        ),
        autosize=True
    )

    # Combine traces and layout into a figure
    fig = go.Figure(data=traces, layout=layout)

    # Save the plot to an HTML file
    write_html(fig, file=output_file_2d, include_plotlyjs='cdn', full_html=True, auto_open=False)


