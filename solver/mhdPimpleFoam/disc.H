(
     fvm::ddt(rho,phi)
   + fvm::div(rho*U,phi)
   - fvm::laplacian(gammaPhi,phi)
  ==
     fvc::(Qphi)
);
