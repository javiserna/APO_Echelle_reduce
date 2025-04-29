import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# === CONFIGURACIÓN ===
filename = 'CVSO_315.0005.ec.fits'
orden = 34   # Número de orden que quieres graficar (1 a 115)

# === ABRIR EL FITS ===
hdul = fits.open(filename)
data = hdul[0].data
header = hdul[0].header
hdul.close()

# Verifica el tamaño
ny, nx = data.shape
print(f"Tamaño de la imagen: {nx} x {ny} (pixeles)")
print(f"Número de órdenes disponibles: {ny}")

if orden < 1 or orden > ny:
    raise ValueError(f"Orden {orden} fuera de rango. Hay {ny} órdenes.")

# === EXTRAER LA INFORMACIÓN DE CALIBRACIÓN DEL HEADER ===

# Buscar la entrada correspondiente en WAT2_
wat2 = ''
i = 1
while f'WAT2_{i:03}' in header:
    wat2 += header[f'WAT2_{i:03}']
    i += 1

# Buscar el string que corresponde a nuestro orden
import re
match = re.search(rf'spec{orden} = "(.*?)"', wat2)
if not match:
    raise ValueError(f"No encontré la calibración para el orden {orden} en WAT2.")

spec_info = match.group(1).split()

# Ahora, del spec_info extraemos:
# [specnum, beam, dtype, crval, cdelt, npix, pix0, w0, w1, ...] 
# (los campos w0, w1, etc., son para no-linealidades si existieran)

crval = float(spec_info[3])  # primer valor de lambda
cdelt = float(spec_info[4])  # incremento de lambda
npix_from_data = data.shape[1] # número de pixeles
npix_from_header = int(float(spec_info[5])) # número de pixeles

if npix_from_data != npix_from_header:
    print(f"Advertencia: el header dice {npix_from_header} pixeles pero la imagen tiene {npix_from_data}")
    
npix = npix_from_data

print(f"Orden {orden}: crval = {crval}, cdelt = {cdelt}, npix = {npix}")

# === CONSTRUIR EL VECTOR DE LONGITUD DE ONDA ===
x = np.arange(npix)
wavelength = crval + (x) * cdelt

# === GRAFICAR EL ORDEN ===
flux = data[orden-1, :]

plt.figure(figsize=(10,6))
plt.plot(wavelength, flux, lw=1)
plt.xlabel('Longitud de onda (Å)')
plt.ylabel('Flujo (adu)')
plt.title(f'Orden {orden} de {filename}')
plt.grid()
plt.show()

