import matplotlib.pyplot as plt
import numpy as np

def get_weights_and_bias(pt1, pt2):
    slope = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

    x = np.linspace(-6, 6, 100)
    y = - slope + (- pt1[1] + slope * pt1[0])

    ...

