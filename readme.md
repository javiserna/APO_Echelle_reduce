# APO Echelle Spectra Reduction Workflow

This repository contains a workflow and scripts for reducing echelle spectra from APO (Apache Point Observatory).

## Requirements

To use this repository, you will need:

- PyRAF and IRAF installed
- Science observations of your targets
- Bias frames
- Flat fields with open/red filter
- Flat fields with blue filter
- Arc lamp exposures
- Dark exposures

## Instructions

1. **Download** this repository to your working directory. Unzip it if necessary.

2. **Activate** your Anaconda environment that has **PyRAF** installed.

3. **Initialize IRAF** within this directory by running:

   ```bash
   mkiraf
   ```

   This will create a folder named `uparm`.

4. **Move your observational data** (for example, the files from the `observations` folder) into:

   ```bash
   raw/DATE/
   ```

   where `DATE` corresponds to the date of the observations.

5. **Unpack** filter reference flat
   
   ```bash
   unzip filter_redflat.zip
   ```
7. **Compile or Enable** DCR for Cosmic Ray Removal
   
   Linux:
   
   Grant execution permissions to the precompiled DCR binary:
   ```bash
   chmod +x dcr
   ```
   
   MacOS:
   
   If you are using a Mac (especially Apple Silicon), compile DCR from source
   ```bash
   tar -xvf dcr.tar
   cd dcr
   make
   ```
   
   after successfully compilation:
   
   Replace the original dcr executable and dcr.par file in the repository directory with the new ones you just compiled.
      
9. **Return to the root** of your working directory and run the reduction script:

   ```bash
   python echelleReduction_py3.py DATE
   ```

10. **Wait a few minutes**. After completion, your reduced spectra will be available in:

   ```bash
   reduced/DATE/
   ```

   as files with the `.ec.fits` extension.

---

## Plotting Calibrated Orders

To visualize a specific spectral order from a reduced, wavelength-calibrated spectrum, you can use the script:

```bash
plot_spec.py
```

### How to use it

1. Open the script and **modify line 7** to indicate the FITS file you want to plot. For example:

   ```python
   filename = 'CVSO_315.0005.ec.fits'
   ```

2. On **line 8**, set the order you wish to plot:

   ```python
   orden = 40  # replace with any order between 1 and 115
   ```

3. Run the script from the terminal:

   ```bash
   python plot_spec.py
   ```

This script only works with `*.ec.fits` files that are **already wavelength calibrated**, as produced by this reduction workflow.

### Where to find the wavelength coverage per order

For a detailed table of the spectral orders and their wavelength ranges, refer to the ARCES instrument documentation:

👉 [https://www.apo.nmsu.edu/arc35m/Instruments/ARCES/](https://www.apo.nmsu.edu/arc35m/Instruments/ARCES/)

### Saving All Orders to a TXT File

When you run `plot_spec.py`, in addition to plotting a specific order, the script will also **save a plain-text file** with the flux and wavelength values for **all orders** in the same `.ec.fits` file. The output file will have the same name, but ending in `_all_orders.txt`, for example:

```
CVSO_315.0005.ec_all_orders.txt
```

Each line contains:

```
# Order  Wavelength[Angstroms]  Flux[adu]
```

This can be easily imported into any plotting software for further custom analysis.

---

**Notes on Continuum Flattening**

This workflow includes basic tools for continuum fitting, but they require user tuning on the polynomial order. A related script aesop_fitting.py can:

- Fit and remove the blaze function per order to normalize spectra
- Merge orders into a single 1D spectrum

⚠️ Note: This process currently rejects the first and last 100 pixels in each order to mitigate edge artifacts. While this is practical, it's not always optimal. Users are encouraged to carefully inspect the continuum and adjust parameters as needed for high-precision science.
