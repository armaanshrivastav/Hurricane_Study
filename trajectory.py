import pandas as pd
import plotly.graph_objs as go
from plotly.io import write_html

# Function to convert hhmmss to milliseconds since midnight
def hhmmss_to_milliseconds(hhmmss):
    # Ensure hhmmss is an integer
    hhmmss = int(hhmmss)  # Convert string to integer
    hours = hhmmss // 10000
    minutes = (hhmmss % 10000) // 100
    seconds = hhmmss % 100
    return (hours * 3600 + minutes * 60 + seconds) * 1000

# Function to convert milliseconds back to hhmmss
def milliseconds_to_hhmmss(milliseconds):
    total_seconds = milliseconds // 1000
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours * 10000 + minutes * 100 + seconds

# Function to convert milliseconds back to hhmmss
def milliseconds_to_hhmmss_str(milliseconds):
    #print(milliseconds)
    # Calculate total seconds and fractional seconds
    total_seconds = milliseconds / 1000.0
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60

    # Format seconds to keep the fractional part
    formatted_seconds = f"{seconds:.3f}".split(".")[1]  # Keep up to 3 decimal places for seconds
    
    # Format the time as hhmmss where seconds include fraction
    return f"{hours:02}{minutes:02}{int(seconds):02}"

def plot_trajectories(dataframes, names,hurricanename, colors,custom_colorscale,start_time, end_time, output_file):
    """
    Generate a 3D scatter plot for the given DataFrames.

    Parameters:
    - dataframes: List of pandas DataFrames containing trajectory data.
    - names: List of names corresponding to each DataFrame (for legends).
    - output_file: File name to save the HTML plot.
    """

    # Generate tick values in milliseconds
    start_time = hhmmss_to_milliseconds(start_time)  # Convert start time to ms
    end_time = hhmmss_to_milliseconds(end_time)  # Convert end time to ms
    step = 20000  # 10 seconds in ms

    tickvals_ms = list(range(start_time, end_time + step, step))
    print(tickvals_ms)
    ticklabels = [milliseconds_to_hhmmss_str(ms) for ms in tickvals_ms]
    print(ticklabels)


    # Add the tickvals and ticklabels to the colorbar
    colorbar_ticks = dict(
        title='hhmmss',
        tickvals=tickvals_ms,
        ticktext=ticklabels,#[f"{label:06d}" for label in ticklabels],  # Format as hhmmss
        ticks="outside"
    )
    traces = []
    annotations = []

    for i, df in enumerate(dataframes):
        df['Actual Time'] = pd.to_numeric(df['Actual Time'], errors='coerce')
        df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')  
        df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')    
        df['Altitude'] = pd.to_numeric(df['Altitude'], errors='coerce')    
        df = df.dropna(subset=['Actual Time', 'Longitude', 'Latitude', 'Altitude'])
        # Create hover text that includes theta-e values and other data
        hover_text = (
            "Longitude: " + df['Longitude'].astype(str) +
            "<br>Latitude: " + df['Latitude'].astype(str) +
            "<br>Altitude: " + df['Altitude'].astype(str) +
            "<br>Actual Time: " + df['Actual Time'].astype(str)
        )
        trace = go.Scatter3d(
            x=df['Longitude'],
            y=df['Latitude'],
            z=df['Altitude'],
            showlegend=True,
            mode='markers',
            marker=dict(
                size=0,
                color=df['Actual Time'].apply(hhmmss_to_milliseconds),  # Color based on Time
                colorscale=custom_colorscale,  # Apply custom colorscale
                #cmin=df2['Actual Time'].min(),
                #cmax=df2['Actual Time'].max()
                colorbar=colorbar_ticks,
                cmin=start_time,
                cmax=end_time

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
        title=dict(text=f'{hurricanename} Time'),
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