from ase.cluster import Icosahedron
from ase.visualize import view

nanoparticle = Icosahedron('Au', noshells=2)

view(nanoparticle)