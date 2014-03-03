from pylab import *

close('all')

NCdata = loadtxt("NC/erickson_conv_0.01.txt")
Cdata = loadtxt("C/erickson_conv_0.01.txt")

NCndofs = NCdata[:,0]
NCl2 =    NCdata[:,1]
NCen =    NCdata[:,2]
Cndofs = Cdata[:,0]
Cl2 =    Cdata[:,1]
Cen =    Cdata[:,2]

loglog(NCndofs, NCl2, marker=' ', linestyle='-',  linewidth=2, label='L2 - Nonconservative')
loglog(Cndofs, Cl2,   marker='o', linestyle=' ', linewidth=2, label='L2 - Conservative')
loglog(NCndofs, NCen, marker=' ', linestyle='-',  linewidth=2, label='Energy - Nonconservative')
loglog(Cndofs, Cen,   marker='o', linestyle=' ', linewidth=2, label='Energy - Conservative')
ylabel('Error')
xlabel('Degrees of Freedom')

legend(loc='best')

figure()
NCFlux1 = NCdata[:,3]
CFlux1 = Cdata[:,3]
NCFlux2 = NCdata[:,4]
CFlux2 = Cdata[:,4]
NCFlux3 = NCdata[:,5]
CFlux3 = Cdata[:,5]
loglog(NCndofs, NCFlux1,      linewidth=2, label='Max Local - Nonconservative')
loglog(NCndofs, abs(NCFlux2), linewidth=2, label='Net Global - Nonconservative')
loglog(Cndofs,   CFlux1,      linewidth=2, label='Max Local - Conservative')
loglog(Cndofs,   abs(CFlux2), linewidth=2, label='Net Global - Conservative')
xlabel('Degrees of Freedom')
ylabel('Flux Imbalance')

legend(loc='best')

show()
