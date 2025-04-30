import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import re

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

# Concatenar todas las entradas WAT2_
wat2 = ''
i = 1
while f'WAT2_{i:03}' in header:
    wat2 += header[f'WAT2_{i:03}']
    i += 1

# === GRAFICAR EL ORDEN SELECCIONADO ===
match = re.search(rf'spec{orden} = "(.*?)"', wat2)
if not match:
    raise ValueError(f"Orden {orden}: calibración no encontrada.")

spec_info = re.findall(r"[-+]?\d*\.\d+|\d+", match.group(1))
crval = float(spec_info[3])
cdelt = float(spec_info[4])
npix = data.shape[1]

print(f"Orden {orden}: crval = {crval}, cdelt = {cdelt}, npix = {npix}")

x = np.arange(npix)
wavelength = crval + x * cdelt
flux = data[orden - 1, :]

plt.figure(figsize=(10,6))
plt.plot(wavelength, flux, lw=1)
plt.xlabel('Longitud de onda (Å)')
plt.ylabel('Flujo (adu)')
plt.title(f'Orden {orden} de {filename}')
plt.grid()
plt.show()

# === GUARDAR TODOS LOS ÓRDENES EN UN SOLO ARCHIVO TXT ===

output_file = filename.replace('.fits', '_all_orders.txt')
with open(output_file, 'w') as f:
    f.write("# Orden  Lambda[Angstroms]  Flujo[adu]\n")
    for ord_idx in range(1, ny + 1):
        match = re.search(rf'spec{ord_idx} = "(.*?)"', wat2)
        if not match:
            print(f"Orden {ord_idx}: calibración no encontrada. Saltando.")
            continue
        spec_info = re.findall(r"[-+]?\d*\.\d+|\d+", match.group(1))
        crval = float(spec_info[3])
        cdelt = float(spec_info[4])
        wavelength = crval + np.arange(npix) * cdelt
        flux = data[ord_idx - 1, :]

        for wl, fl in zip(wavelength, flux):
            f.write(f"{ord_idx:03d}  {wl:.4f}  {fl:.4f}\n")
        f.write("\n")  # Separador entre órdenes

print(f"Archivo guardado como {output_file}")
