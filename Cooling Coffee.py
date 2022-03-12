from numpy import linspace,log,exp,sin,cos,sqrt,pi,e
from scipy.optimize import brentq
from scipy.integrate import odeint
from matplotlib.pyplot import plot, show

# set the temperatures in °C
HotCoffeeTemp = 100
CreamTemp = 20
CoolCoffee = 60 # Drinkable temperature
RoomTemp = 20

# set the volumes in oz
CoffeeVol = 8
CreamVol = 1

# newton cooling rate
r = 0.001

# Did my work from here

def rate_func(t,y):
    global RoomTemp, r
    rate = -r * (y - RoomTemp)
    return rate

# What's the cooling rate for 90°C Coffee?
print(rate_func(0,90))

# Get values at t=0 and t=90 (ie [0, 90])
print(odeint(rate_func, 90, [0,90], tfirst=True))

# Check over long time to check limiting behaviour
time = linspace(0,10000,1000)
Temp = odeint(rate_func, HotCoffeeTemp, time, tfirst=True)
# try plotting

plot(time,Temp)

show()

# To here, since rest was done collaboratively in class

def mix_func(V1,T1,V2,T2):
    # Calculates the final temperature of two liquids after they have been
    # mixed based upon the initial temperature and volume of each individual liquid.
    # Function is passed:
    # V1, initial Volume of liquid one
    # T1, initial temperature of liquid one
    # V2, initial Volume of liquid two
    # T2, initial temperature of liquid two
    # Tmix, the temperature of the mixture

    Tmix = ((V1*T1) + (V2*T2))/(V1 + V2)
    return Tmix

v1 = 10
v2 = 20
t1 = 100
t2 = 150
mix_func(v1,t1, v2,t2)


def CoffeeTemp(t):
    # This function returns the temperature of the coffee after cooling
    # for t seconds and mixing with cream. It models the physical
    # process in the problem, first cooling then mixing.

    # first let the coffee cool for t seconds
    TT = odeint(rate_func, HotCoffeeTemp, [0, t], tfirst=True)  # fill in arguments
    Temp = TT[-1]  # the final value in TT is the temperature after cooling for t seconds

    # second mix cream with coffee to get final temperature using mix_func
    Temp = mix_func(CoffeeVol, Temp, CreamVol, CreamTemp)

    return Temp

CoffeeTemp(1000)

def TempDiff(t):
  # difference between temperature of coffee and desired temperature
  diff = CoffeeTemp(t) - CoolCoffee
  return diff

TempDiff(1000)

CoolTime = brentq(TempDiff,10,20*60)
print(CoolTime)

print('If you start with ',round(CoffeeVol),'oz of coffee at ',round(HotCoffeeTemp,3),'deg-C')
print('mix in ',round(CreamVol),'oz of cream at ',
    round(CreamTemp),'deg-C ',
    'and wait ',round(CoolTime/60,2), 'minutes')
print('then your coffee will be at the ideal temperature of ',round(CoolCoffee,3),'deg-C')