#!/usr/bin/env python3
import math
def example_str():
    print (len("sdfsdfsfsdfsdfsdfsdfsfs"))
    print ("New" + "Found" + "Land")
    s = "New"
    s += "Found"
    s += "Land"
    print(s)
    colors = ';'.join(['#000000', '#000100'])
    print (colors.split(';'))
    print (''.join(['high', 'way', 'man']))
    print ("unforgetable".partition("forget"))

    departure, separator, arrival = "London:Edinburg".partition(':')
    print (departure)
    print (arrival)

    origin, _, destination = "Sealte:Boston".partition(':')
    print (origin)
    print (destination)

    print ("The age of {0} is {1}".format('Jim', 32))
    print ("Current possition {latitude} {longitude}".format(latitude="60N",
                                                             longitude="5E"))
    coordinate = (65.2, 23.3, 82.2)
    print ("Galactic position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=coordinate))

    print ("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))


if __name__ == '__main__':
    example_str()
