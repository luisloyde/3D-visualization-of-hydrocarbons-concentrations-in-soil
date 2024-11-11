# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from pathlib import Path
import os
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

# Obtiene el directorio del script (funciona en cualquier entorno)
files_directory = Path(__file__).parent

os.chdir(files_directory)

data = pd.read_excel('data49.xlsx') #data file directory
print(data.head())

x = data['X'].values #UTM X column
y = data['Y'].values #UTM Y column
z = data['PROF'].values*-1 #Depths

pollutant_concentration = data['HFP'].values #choose pollutant concentration column
MPL=3000 #Maximum permisible limit "LMP" in mexican regulation

grid_x, grid_y, grid_z = np.mgrid[
    min(x):max(x):1,
    min(y):max(y):1,
    min(z):0:1
    ]

grid_pollutant = griddata((x, y, z), pollutant_concentration, (grid_x, grid_y, grid_z), method='linear')

import plotly.graph_objs as go
import math
max_plot = math.ceil(pollutant_concentration.max()/MPL)*MPL

# Crear una figura 3D
fig = go.Figure(data=go.Volume(
    x=grid_x.flatten(),
    y=grid_y.flatten(),
    z=grid_z.flatten(),
    value=grid_pollutant.flatten(),
    isomin=0,  # Establecer un valor mínimo para la visualización
    isomax=max_plot,  # Establecer el valor máximo para la visualización
    opacity=0.5,  # Controlar la opacidad
    surface_count=int(max_plot/MPL),  # Número de superficies a mostrar
))

# Asignar factores de escala

x_range = max(x) - min(x)
y_range = max(y) - min (y)
ratio_y = y_range / x_range

# Configurar el diseño
fig.update_layout(
    scene=dict(
        xaxis_title=' UTM X (m)',
        yaxis_title='UTM Y (m)',
        zaxis_title='Depth (m)',
    ),
    scene_aspectmode='manual',
    scene_aspectratio=dict(x=1,y=ratio_y,z=0.25),
    title='Pollutant in soil'
)

fig.show()

import plotly.offline as pyo

# Genera un archivo HTML
pyo.plot(fig, filename='volumetric_visualization.html', auto_open=True)

# Cálculo de volumen

mask = grid_pollutant > MPL # Crear una máscara de las concentraciones que superan el umbral

# Determinar la resolución de la rejilla
delta_x = (max(x) - min(x)) / grid_x.shape[0]
delta_y = (max(y) - min(y)) / grid_y.shape[1]
delta_z = (max(z) - min(z)) / grid_z.shape[2]

# Calcular el volumen de cada celda
volume_ceils = delta_x * delta_y * delta_z

# Contar el número de celdas que superan el umbral
num_ceils_above = np.sum(mask)

# Calcular el volumen total que supera el umbral
volume_total_above = num_ceils_above * volume_ceils

print(f"The soil volume that presents pollutant concentrations above MPL is: {volume_total_above:.2f} m^3")

depths_above = grid_z[mask]

# Encontrar la profundidad máxima
maximum_depth = np.min(depths_above)

print(f"Maximum depth where pollutant concentration is above MPL: {maximum_depth:.2f} meters")

# Crear una máscara para seleccionar los puntos que superan el MPL
mask = grid_pollutant > MPL

# Filtrar los valores de las coordenadas y las concentraciones de contaminante utilizando la máscara
filtered_grid_x = grid_x[mask]
filtered_grid_y = grid_y[mask]
filtered_grid_z = grid_z[mask]
filtered_pollutant = grid_pollutant[mask]

# Crear una nueva figura 3D para el volumen contaminado
fig_contaminated = go.Figure(data=go.Volume(
    x=filtered_grid_x.flatten(),
    y=filtered_grid_y.flatten(),
    z=filtered_grid_z.flatten(),
    value=filtered_pollutant.flatten(),
    isomin=MPL,  # Mínimo será el Límite Máximo Permisible (MPL)
    isomax=max_plot,  # Máximo será el valor más alto de contaminación filtrado
    opacity=0.5,  # Controlar la opacidad
    surface_count=int((max_plot-MPL)/MPL),  # Número de superficies a mostrar
))

# Configurar el diseño de la figura 3D filtrada
fig_contaminated.update_layout(
    scene=dict(
        xaxis_title='UTM X (m)',
        yaxis_title='UTM Y (m)',
        zaxis_title='Depth (m)',
    ),
    scene_aspectmode='manual',
    scene_aspectratio=dict(x=1,y=ratio_y,z=0.25),
    title=f'Polluted volume (pollutant concentrations > {MPL})'
)

# Mostrar la figura
fig_contaminated.show()

pyo.plot(fig, filename='polluted_visualization.html', auto_open=True)