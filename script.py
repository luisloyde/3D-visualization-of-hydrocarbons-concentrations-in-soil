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
    min(z):0+1:0.1
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
        xaxis_title='Coordenada UTM E',
        yaxis_title='Coordenada UTM N',
        zaxis_title='Profundidad',
    ),
    scene_aspectmode='manual',
    scene_aspectratio=dict(x=1,y=ratio_y,z=0.25),
    title='HFP en suelo'
)

fig.show()

import plotly.offline as pyo

# Genera un archivo HTML
pyo.plot(fig, filename='volumetric_visualization.html', auto_open=True)


