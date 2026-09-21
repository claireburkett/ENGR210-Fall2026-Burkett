import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(r'C:\Users\SFU\OneDrive - Saint Francis University\Desktop\ENGR210-Fall\StrainTest.csv',
                  delimiter=",",
                  skiprows=1)
strain = data[:,0]
stress = data[:,1]
plt.plot(strain, stress)
plt.xlabel("Strain")
plt.ylabel("Stress (ksi)")
plt.show() # plots stress-strain curve

integral = 0
for i in range (5):
    x = strain[i]
    x1 = strain[i+1]
    h = x1-x
    trap = (stress[i]+stress[i+1])*h/2
    integral += trap
    
print("Modulus of Toughness = ", integral)