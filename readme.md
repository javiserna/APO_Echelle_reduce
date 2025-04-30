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

5. **Uncompress** filter_redflat

   ```bash
   unzip filter_redflat.zip
   ```
6. **Give permissions** to dcr file (Linux): 

   ```bash
   chmod +x dcr
   ```
   **For Mac OS X** you will need to uncompress dcr.tar and inside that folder execute make command
   ```bash
   untar dcr.tar
   cd dcr
   make
   ```
   Once dcr is recompiled, please replace the dcr executable and dcr.par with the new ones into the repo folder
   
8. **Return to the root** of your working directory and run the reduction script:

   ```bash
   python echelleReduction_py3.py DATE
   ```

9. **Wait a few minutes**. After completion, your reduced spectra will be available in:

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

## Caveats

- **Dark correction** is not yet implemented — this feature is currently in development.
- **Continuum flattening** across different orders is not fully automated. Some basic tools are included, but they require user tuning through trial and error.
