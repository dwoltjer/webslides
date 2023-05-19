from setuptools import setup, find_packages

setup(
    name="webslides",
    version="0.6.4",
    author="Derk-Jan Woltjer",
    author_email="derkjan.woltjer@gmail.com",
    description="Creates powerpoint like slides in HTML format. Including title page, index page and page navigation.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    licence="MIT License",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pandas", "plotly"]
)
