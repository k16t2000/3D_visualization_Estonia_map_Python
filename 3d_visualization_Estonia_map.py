import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [59,26,13.06,'N'], lat = [24,45,12.71,'E'],
    marker = { 'size': 10, 'color': "orange" }))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 24.75353, 'lat': 59.43696 },
        'zoom': 5},
    showlegend = False)

fig.show()
