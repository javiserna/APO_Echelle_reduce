import matplotlib.pyplot as plt
from aesop import EchelleSpectrum
from specutils import Spectrum1D

filename = 'CVSO_315.0005.ec.fits'
target_spectrum = EchelleSpectrum.from_fits(filename)

# Normalize blaze with polynomial (order 2)
target_spectrum.continuum_normalize_lstsq(polynomial_order=2)

# Optional: trim noisy edges on each order
for order in target_spectrum:
    N = 100  # remove 100 pixels at each edge
    order.flux = order.flux[N:-N]
    order.wavelength = order.wavelength[N:-N]

# Merge all orders into one 1D spectrum (simple averaging of overlaps)
spec1d = target_spectrum.to_Spectrum1D()

# Plot the stitched 1D spectrum
plt.figure()
spec1d.plot()
plt.xlabel("Wavelength")
plt.ylabel("Flux")
plt.title("Stitched 1D Spectrum of CVSO 315")
plt.tight_layout()
plt.show()

