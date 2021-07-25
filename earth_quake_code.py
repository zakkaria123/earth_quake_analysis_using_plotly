def map_plot():
	import json
	nakato=open('d:\\inspire\\pyfiles\\nakato.json')
	loaded_to=json.load(nakato)
	index=loaded_to['features']
	lats,longs=[],[]
	for values in index:
		lati=values['geometry']['coordinates'][1]
		longi=values['geometry']['coordinates'][0]
		lats.append(float(lati))
		longs.append(float(longi))
	import plotly.graph_objects as go
	fig=go.Figure(go.Scattermapbox(
		mode='markers',
		marker={'size':10},
		lat=[-19,20,0],
		lon=[20,32,100]))
	fig.add_trace(go.Scattermapbox(
		mode='markers',
		lat=lats,
		lon=longs,
		marker={'size':10}))
	fig.update_layout(
		margin={'l':0,'r':0,'b':0,'t':0},
		mapbox={
			'center':{'lat':20,'lon':20},
			'zoom':1,
			'style':'stamen-terrain',
			'center':{'lat':-20,'lon':-20}})
	fig.show()
  
map_plot()
