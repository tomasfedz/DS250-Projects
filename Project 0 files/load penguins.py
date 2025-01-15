import pandas as pd
import numpy as np
from lets_plot import *
from palmerpenguins import load_penguins


penguins = load_penguins()
penguinspecies = penguins['species']


# Create a basic plot 
(
    ggplot(data=penguins, mapping=aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point()
).show()
