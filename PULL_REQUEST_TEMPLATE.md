\<insert pull request description here\>

-----

# Checklist

Please go through each entry in the below checklist and mark an 'X' if that condition has been met. Every entry should be marked with an 'X' to be get the Pull Request approved.


- [ ] All `import`s are in the first cell? 
    - [ ] First block of imports are standard libraries
    - [ ] Second block are 3rd party libraries
    - [ ] Third block are all `arcgis` imports? Note that in some cases, for samples, it is a good idea to keep the imports next to where they are used, particularly for uncommonly used features that we want to highlight.
- [ ] All `GIS` object instantiations are one of the following?
    - `gis = GIS()`
    - `gis = GIS('home')` or `gis = GIS('pro')`
    - `gis = GIS(profile="your_online_portal")`
    - `gis = GIS(profile="your_enterprise_portal")`
- [ ] If this notebook requires setup or teardown, did you add the appropriate code to `./misc/setup.py` and/or `./misc/teardown.py`?
- [ ] If this notebook references any portal items that need to be staged on AGOL/Python API playground, did you coordinate with a Python API team member to stage the item the correct way with the `api_data_owner` user?
- [ ] If the notebook requires working with local data (such as CSV, FGDB, SHP, Raster files), upload the files as items to the [Geosaurus Online Org](geosaurus.maps.arcgis.com/) using `api_data_owner` account and change the notebook to first download and unpack the files.
- [ ] Code simplified & split out across multiple cells, useful comments?
- [ ] Consistent voice/tense/narrative style? Thoroughly checked for typos?
- [ ] All images used like `<img src="base64str_here">` instead of `<img src="https://some.url">`? All map widgets contain a static image preview? (Call `mapview_inst.take_screenshot()` to do so)
- [ ] All file paths are constructed in an OS-agnostic fashion with `os.path.join()`? (Instead of `r"\foo\bar"`, `os.path.join(os.path.sep, "foo", "bar")`, etc.)
- [ ] Is your code formatted using [Jupyter Black](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)? You can use Jupyter Black to format your code in the  notebook.
- [ ] **IF YOU WANT THIS SAMPLE TO BE DISPLAYED ON THE DEVELOPERS.ARCGIS.COM WEBSITE**, ping @ mohi9282 so he can add it to the list for the next deploy 
