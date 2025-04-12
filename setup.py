from setuptools import setup, find_packages

setup(
    name="neuron7x_hub",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "pytest>=7.0.0"
    ],
    author="Neuro Labs Collective",
    description="Neuro-inspired cognitive engine with harmonic vector encoding and neurotransmitter modulation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/neuron7xforge/neuron7x-core",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9"
)
