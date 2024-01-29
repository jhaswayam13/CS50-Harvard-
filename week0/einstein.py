def main():
    mass=int(input("Enter the value of mass:"))
    print("The energy E corresponding to this mass is:",energy(mass))
def energy(m):
    c=3*(10**8)
    E=m*(c**2)
    return E



main()
