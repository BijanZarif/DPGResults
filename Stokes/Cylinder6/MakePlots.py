from pylab import *

close('all')

NCdata = loadtxt("NC/stokeshemker_err.txt")
Cdata = loadtxt("C/stokeshemker_err.txt")
NCFdata = loadtxt("NC/stokeshemker_flux.txt")
CFdata = loadtxt("C/stokeshemker_flux.txt")

NCndofs = NCdata[:,0]
Cndofs = Cdata[:,0]
NCEnErr = NCdata[:,1]
CEnErr = Cdata[:,1]
NCFlux1 = NCdata[:,2]
CFlux1 = Cdata[:,2]
NCFlux2 = NCdata[:,3]
CFlux2 = Cdata[:,3]
NCFlux3 = NCdata[:,4]
CFlux3 = Cdata[:,4]
# loglog(NCndofs, NCEnErr,      linewidth=2, label='Energy Error - Nonconservative')
# loglog(Cndofs, CEnErr,        linewidth=2, label='Energy Error - Conservative')
# loglog(NCndofs, NCFlux1,      linewidth=2, label='Max Local - Nonconservative')
# loglog(NCndofs, abs(NCFlux2), linewidth=2, label='Net Global - Nonconservative')
# loglog(Cndofs,   CFlux1,      linewidth=2, label='Max Local - Conservative')
# loglog(Cndofs,   abs(CFlux2), linewidth=2, label='Net Global - Conservative')
# xlabel('Degrees of Freedom')
# ylabel('Flux Imbalance')
# legend(loc='best')

figure()
nrefsNC = NCFdata.shape[0]
nrefsC = CFdata.shape[0]
xpts = array([-1, -0.95, 0, 0.95, 3])
for i in range(0, nrefsNC):
   massFlux = NCFdata[i,:]
   massLoss = (massFlux[0]-massFlux)/massFlux[0]*100
   plot(xpts, massLoss, '-o', label='%d' % NCndofs[i]+' DOFs')
xlabel('x location')
ylabel('percent mass loss')
legend(loc='best')

figure()
for i in range(0, nrefsC):
   massFlux = CFdata[i,:]
   massLoss = (massFlux[0]-massFlux)/massFlux[0]*100
   plot(xpts, massLoss, '-o', label='%d' % Cndofs[i]+' DOFs')
xlabel('x location')
ylabel('percent mass loss')
legend(loc='best')

show()
