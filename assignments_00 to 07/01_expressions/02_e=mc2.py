C = 299792458
def main():
   
   mass = float(input("Enter kilos of mass: "))

   energy = mass * C**2

   print(f"\n e = m * C^2...")
   print(f"\n m = \033[1;3m{mass}\033[0m kg")
   print(f"\n C = {C} m/s")
   print(f"\n {energy} joules of energy!")



if __name__ == '__main__':
    main()