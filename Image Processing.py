from numpy import dot, sqrt, array
u = [2.225, -0.7644, -2.7317]

# The coordinates are just 2.225i -0.7644j - 2.7317k, since if we dot our vectors that's what we'll get

x = [1, 0, 0]
y = [0, 1, 0]
z = [0, 0, 1]

xp = array((0.65, 0.65, -0.38))

yp = array((0.31, -0.69, -0.65))

zp = array((-0.69, 0.31, -0.65))

# Question 1

print(dot(xp, yp))

print(dot(yp, zp))

# These are both approximately 0, so the given vectors are orthogonal to each other

print(sqrt(dot(xp, xp)))

print(sqrt(dot(yp, yp)))

print(sqrt(dot(zp, zp)))

# These all also have a length of approximately 1, so they're all orthonormal

# Question 2

# We can do the following calculations to find our coordinates

c1 = dot(u, xp)

c2 = dot(u, yp)

c3 = dot(u, zp)

print("Transformed Coordinates: ", c1, c2, c3)

# Question 3

# Reconstruct the vector

uTF = c1 * xp + c2 * yp + c3 * zp

print(uTF)
