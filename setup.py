import setuptools

# with open("./readme.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="dimscommon",
    version="0.0.1",
    author="Mateusz Kojro",
    author_email="mateuszkojro@outlook.com",
    description="Package containing common python scripts for DIMS project",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'matplotlib',
        'cython',
        'requests',
        'pandas',
        'numpy',
        'opencv-python',
        'psycopg2',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)