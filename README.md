# Plane-Symmetry
This python program creates plane symmetries after the user selects an image to create a fundamental domain from.

Packages required -

pillow https://pillow.readthedocs.io/en/stable/installation.html

tkinter (installs with python) https://docs.python.org/3/library/tkinter.html

math (inside python's standard library)

numpy https://scipy.org/install.html

If you're using a version of Mac OS later than OS X, tkinter has serious bugs before python3.7.4. Install this version of python or later to successfully get tkinter working...

To run (after installing packages above), enter:
    'python3 symmetry.py'
from the command line.

Every plane symmetry group has been implemented except four - p3m1, p31m, p6 and p6m. https://en.wikipedia.org/wiki/Wallpaper_group

###### Bugs

Text on buttons may not be showing correctly - I think this an issue with MacOSX and might be fine on some versions or on Windows.
In any case I added labels next to each button so you can infer what they're meant to do.
