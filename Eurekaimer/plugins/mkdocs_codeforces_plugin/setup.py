# Copyright (c) 2024 Eurekaimer
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mkdocs-codeforces-plugin",
    version="0.1.0",
    description="MkDocs plugin to display Codeforces user statistics as beautiful cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eurekaimer/mkdocs-codeforces-plugin",
    author="Eurekaimer",
    author_email="2507983039@qq.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "mkdocs>=1.0.0",
        "requests>=2.0.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Documentation",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.7",
    entry_points={
        "mkdocs.plugins": [
            "codeforces = mkdocs_codeforces_plugin.plugin:CodeforcesPlugin",
        ],
    },
)