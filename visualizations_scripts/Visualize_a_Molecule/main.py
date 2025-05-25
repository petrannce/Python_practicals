from ase import Atoms
from ase.visualize import view

water = Atoms('H2O', positions=[(0, 0, 0), (0, 0, 1), (1, 0, 0)])
view(water)