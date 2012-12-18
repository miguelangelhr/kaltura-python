from distutils.core import setup
 
 
setup(
    name = "kaltura-python",
    version = __import__("KalturaCoreClient").API_VERSION,
    description = "The Kaltura python API client",
#    packages = [
#        "urls_sugar",
#    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
