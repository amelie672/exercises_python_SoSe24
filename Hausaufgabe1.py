import matplotlib.pyplot as plt

def spar_funktion (AK, SR, i, lz):
   kapital = AK
   GK = []
   
   for k in range (1, lz+1):
    kapital = SR + kapital * (1+i)
    GK.append(kapital)
    
    return GK

print(spar_funktion(AK=10000,
              SR=1000,
              i= 0.01,
              lz=10))

plt.bar()