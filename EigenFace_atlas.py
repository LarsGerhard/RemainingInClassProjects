# Face recognition by Santiago Serrano
# http://www.pages.drexel.edu/~sis26/Eigencode.htm
# Modified by Eric Salathe Dec 2015
from numpy import (
    linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e, 
    ones, arange, zeros, real, imag, sign, shape, dot, size,
    mean
    )

from numpy.random import rand

from matplotlib.pyplot import (
    plot,xlabel,ylabel,legend,show, figure, subplot, title, tight_layout, stem, pcolormesh,
    get_cmap
    )   
from scipy.io import loadmat

'''
Read in the image database
This fills an 96x64x40  array called  pics where each 96x64 layer is a
picture and there are 40 pictures (layers). 
The first pictur is pics[:,:,0]
To make  picture number i into a single column vector, use
X=pics[:,:,i].reshape((row*col,))
'''
# read in images

infile=loadmat('Faces.mat')
pics = infile['pics']

row, col, mpictot = shape(pics) # image size
npixel = row*col # total pixels in each image

'''
Read in the EigenFaces, which form a basis for our
  vector space of faces. Only the top few eigenfaces are necesary
  to represent the dataset, and we can flatten the vector space. 
'''
infile=loadmat('EigenFaces.mat')
u=infile['u']
nn, meig = shape(u) # meig is the number of eigen vectors in our basis



# plot all the faces, 5 to a row

figure(1)
cmap=get_cmap('gray')
figcol=5
figrow=int(mpictot/figcol)
for i in range(mpictot):
    subplot(figrow, figcol, i+1)
    pcolormesh(pics[:,:,i],cmap=cmap)


figure(2)
for i in range(meig):
    subplot(figrow, figcol, i+1)
    pcolormesh(u[:,i].reshape((row,col),order='F'),cmap=cmap)


