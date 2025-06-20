import pandas as pd
import plotly.graph_objs as go
from plotly.io import write_html

from general import append_to_excel, strip_numeric_suffix

def plot_trajectories(dataframes, names,hurricanename, colors,custom_colorscale, output_file):
    """
    Generate a 3D scatter plot for the given DataFrames.

    Parameters:
    - dataframes: List of pandas DataFrames containing trajectory data.
    - names: List of names corresponding to each DataFrame (for legends).
    - output_file: File name to save the HTML plot.
    """

    traces = []
    annotations = []

    for i, df in enumerate(dataframes):
        #correlation = df['Altitude'].corr(df['RD (m/s)'])
        #print(f"Correlation between Altitude and Radial Velocity for {output_file}: {correlation}")
        # Example usage
        #append_to_excel("graphs/RDcorrelation_data.xlsx", strip_numeric_suffix(hurricanename), f"{hurricanename}-{names[i]}", correlation)
        df['RD (m/s)'] = pd.to_numeric(df['RD (m/s)'], errors='coerce')
        df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')  
        df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')    
        df['Altitude'] = pd.to_numeric(df['Altitude'], errors='coerce')    
        df = df.dropna(subset=['RD (m/s)', 'Longitude', 'Latitude', 'Altitude'])
        # Create hover text that includes theta-e values and other data
        hover_text = (
            "Longitude: " + df['Longitude'].astype(str) +
            "<br>Latitude: " + df['Latitude'].astype(str) +
            "<br>Altitude: " + df['Altitude'].astype(str) +
            "<br>RD (m/s): " + df['RD (m/s)'].astype(str)
        )
        trace = go.Scatter3d(
            x=df['Longitude'],
            y=df['Latitude'],
            z=df['Altitude'],
            showlegend=True,
            mode='markers',
            marker=dict(
                size=0,
                color=df['RD (m/s)'],  # Color based on Radial Velocity
                colorscale=custom_colorscale,  # Apply custom colorscale
                colorbar=dict(
                    title='m/s',
                    tickvals=list(range(-50, 51, 10)),  # Tick intervals for Radial Velocity
                    ticks="outside",
                ),
                cmin=-20,  # Minimum value for the colormap
                cmax=20    # Maximum value for the colormap
            ),
            text=hover_text,  # Set hover text
            hoverinfo='text',  # Show only hover text
            name=names[i]
        )

        # Add trace to the list
        traces.append(trace)

        dict1 = dict(
            x=df['Longitude'].iloc[-1],  # Close to trajectory 1
            y=df['Latitude'].iloc[-1],
            z=df['Altitude'].iloc[-1],
            text=f'<b>{i + 1}</b>',
            showarrow=False,
            font=dict(color=f'{colors[i]}', size=16, family="Arial")  # Increased font size
        )
        annotations.append(dict1)

    # Layout
    layout = go.Layout(
        title=dict(text=f'{hurricanename} Radial Velocity'),
        font=dict(size=9),
        margin=dict(l=0, r=0, t=20, b=0),  # Reduce margins to avoid cutting
        autosize=True,  # Allow dynamic resizing
        scene=dict(
            xaxis_title='Longitude',
            yaxis_title='Latitude',
            zaxis_title='Altitude (m)',
            yaxis=dict(
            range=[max(df['Latitude'].max() for df in dataframes),  # Maximum latitude
                   min(df['Latitude'].min() for df in dataframes)]  # Minimum latitude
            ),
            xaxis=dict(
            range=[max(df['Longitude'].max() for df in dataframes),  # Maximum latitude
                   min(df['Longitude'].min() for df in dataframes)]  # Minimum latitude
            ),
            camera=dict(
                eye=dict(x=2, y=1.5, z=1),  # Set camera position
                center=dict(x=0, y=0, z=0),  # Set focal point
                up=dict(x=0, y=0, z=1)      # Define up direction
            )
        ),
        legend=dict(
            font=dict(size=10),
            bgcolor='rgba(255, 255, 255, 0.8)',
            x=0.85,  # Adjusted position: left of the colorbar
            y=-0.5  # Centered vertically
        )
    )

    # Combine traces and layout into a figure
    fig = go.Figure(data=traces, layout=layout)

    # Add annotations
    fig.update_layout(scene_annotations=annotations)

    # Save the plot to an HTML file
    write_html(fig, file=output_file, include_plotlyjs='cdn', full_html=True, auto_open=False)


