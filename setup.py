from setuptools import setup, find_packages
import os 
setup(
    name="waifu-fetch",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "waifu-fetch = waifu_fetch.__main__:main"
        ]
    },
    package_data={
        "waifu_fetch": ["ascii_waifus/*.txt"]
    },
    install_requires=[
        "psutil"
    ],
    author="Anonymous",
    description="A waifu-powered neofetch-like terminal CLI",
    long_description=open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)
