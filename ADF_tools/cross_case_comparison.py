from pathlib import Path
import logging
import xarray as xr
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


# figure out which cases we can get

sloc = Path("/glade/scratch/hannay/ADF")  # search location
cases = [x for x in sloc.iterdir() if x.is_dir()]  # each subdirectory is probably a case name
for c in cases:
    if (c/"plots").exists() and (c/"plots").is_dir():
        for cc in (c/"plots").iterdir():
            print(f"{cc.name} Last Modified: {cc.stat().st_mtime}")




