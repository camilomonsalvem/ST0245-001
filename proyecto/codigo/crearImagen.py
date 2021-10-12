import urllib.request
import numpy as np
from numpy import genfromtxt
from matplotlib import pyplot as plt

# tqdm is not strictly necessary, but it gives us a pretty progress bar
# to visualize progress.
from tqdm import trange

def linkArchivo(url):
    urllib.request.urlretrieve(url,"archivo.csv")

def crearMatriz():
    f = "archivo.csv"
    f = genfromtxt(f,delimiter=",") 
    imgplot = plt.imshow(f, cmap = "gray") 
    plt.imsave("imagenCreada.jpg",f,cmap = "gray")

def __main__():
    a = input()
    linkArchivo(a)
    crearMatriz()

__main__()