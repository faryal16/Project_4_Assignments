# Write a program that continually reads in mass from the user and then outputs 
# the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy,
# m stands for mass, and C is the speed of light:

# E = m * c**2

C: int = 299792458  # The speed of light in m/s

def main():
    
    mass_in_kg:float = float(input("\n\033[1;3m Enter kilos of mass: \033[0m"))
    
    energy_in_joules: float = str(mass_in_kg * (C ** 2))
    
    # display the work
    print("\n\033[1m e = m * C^2.. \033[0m ")
    print(f"\n m = {mass_in_kg}kg")
    print(f"\nC = {C}m/s")
    
    print(f"\n{energy_in_joules} joules of energy! ")
    
    
if __name__ == '__main__':
    main()