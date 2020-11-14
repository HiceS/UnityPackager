# Unity Packager

This is a packager that has data structures that can condense and populate ` .unitypackage ` files that can be automatically parsed with unity and are already linked to the running exucutable.

- This is cross platform.
- This has no dependencies at all.
- This is an expensive conversion to the binary format.

Originally written for use in hellion since unity has no easy way to distribute compiled dependencies that use 3rd party libraries instead of runtime compiled scripts.

### Packaging

This package is developed this way so that making updates can be isolated to a specific version of the library.

### Documentation

TBD, however probably pydoc3 since it looks good.

I won't include pydoc3 as a development dependency however so it's up to the developer to read this if they want to update the docs.

### Packaging

1. Ensure you have the most up to date tools ` pip install -m --ser --upgrade setuptools wheel `

2. ` python setup.py sdist bdist_wheel `

In the ` dist\ ` directory there should be the built files to upload to pypi if needed for distribution