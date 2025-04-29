# APO Echelle Spectra Reduction Workflow

This repository contains a workflow and scripts for reducing echelle spectra from APO (Apache Point Observatory).

## Requirements

To use this repository, you will need:
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

5. **Return to the root** of your working directory and run the reduction script:
   ```bash
   python echelleReduction_py3.py DATE
   ```

6. **Wait a few minutes**. After completion, your reduced spectra will be available in:
   ```bash
   reduced/DATE/
   ```
   as files with the `.ec.fits` extension.

## Plotting

To visualize a particular order of the reduced spectrum, a plotting script will be shared soon.  
For now, this basic reduction process should allow you to obtain your extracted spectra.

## Caveats

- **Dark correction** is not yet implemented — this feature is currently in development.
- **Continuum flattening** across different orders is not fully automated. Some basic tools are included, but they require user tuning through trial and error.
- **Spectral order visualization tools** are under active development.
