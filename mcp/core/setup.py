from setuptools import setup, find_packages

setup(
    name="mcp-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.25.0",
        "redis>=5.0.0",
        "tenacity>=8.0.0",
        "structlog>=23.0.0",
    ],
)
