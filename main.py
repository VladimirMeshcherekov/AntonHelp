
from typing import Final
import math

_k1: Final = 0;
_k2: Final = 0;
chislitel = 0;
znamenatel = 0;
koren = 1;
for z in range(-2, 13):
    z = (z/2);
    try:
        chislitel = math.sin(z*2) * math.sin(z*2) * math.sin(z*2) - _k1;
        koren = math.sqrt(1/math.fabs(z));
        znamenatel = koren + (math.e ** (z + _k2));
        print("z =", z, "; y =", chislitel / znamenatel);
    except:
        print("при z =", z, " возникло исключение");







# t.me/snappy
