import pyvista as pv
import numpy as np

dataset=pv.read('D:/Geoenvironmental Services/CARXO/Blasillo 5/Planos/Isometrico/3Dpoints.vtk')
dataset

grid=pv.ImageData()
grid.origin=(387638.137,1996380,-1.2)
grid.spacing=(1, 1, 0.2)
grid.dimensions=(161,222, 2*5)

p = pv.Plotter()
p.set_scale(zscale=50)
p.add_mesh(grid.outline(), color='k')
p.add_mesh(dataset, render_points_as_spheres=True)
#p.show()

interp=grid.interpolate(dataset, radius=15000, sharpness=10000,strategy='null_value')
p.add_volume(interp,opacity=0.25)
p.add_mesh(interp.contour(2),opacity=0.25)
p.show()

#import numpy as np
#dataset=np.genfromtxt('Resultados concentracion.csv',delimiter=',',skip_header=1)

#mesh=pv.PolyData(dataset)
#mesh.plot()