from arrays.ula import ula
from arrays.uca import uca
from arrays.uha import uha
from arrays.ura import ura

from constants.params import D, UCA_DEFAULT_RADIUS


def get_coords(arr_type, params):
    if arr_type == "ula":
        N = int(params[0])
        return ula(N, D)
    elif arr_type == "uca":
        N = int(params[0])
        return uca(N, UCA_DEFAULT_RADIUS)
    elif arr_type == "ura":
        Nx = int(params[0])
        Ny = int(params[1])
        return ura(Nx, Ny, D, D)
    elif arr_type == "uha":
        N_side = int(params[0])
        return uha(N_side, D)
