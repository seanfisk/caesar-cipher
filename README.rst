===========================
 Interactive Caesar Cipher
===========================

+-------------+---------------------------------+
|Author       |Sean Fisk <fiskse@mail.gvsu.edu>,|
|             |Grand Valley State University    |
+-------------+---------------------------------+
|Developed For|Chuck Bates, Grand Valley State  |
|             |University                       |
+-------------+---------------------------------+

Requirements and Installation
=============================

This program is written in `Python`_ and utilizes `PySide`_, Python bindings for
the `Qt`_ libraries.

Install
-------

#. `Install Python`_.
#. `Install PySide`_.
#. Get the source code::

    git clone https://github.com/seanfisk/caesar-cipher
   
#. Install the Python module::

    python setup.py install

Run
---

#. Run the installed script::

    caesar_cipher

Documentation
-------------

#. To build the documentation you need to install `Sphinx`_. Here my recommended
   way to do that::

    easy_install pip
    pip install Sphinx

#. Build the documentation::

    cd docs
    make html # or `make.bat html' on Windows
    open build/html/index.html
    

.. _Python: http://python.org/
.. _PySide: http://www.pyside.org/
.. _Qt: http://qt.nokia.com/
.. _Install Python: http://www.python.org/download/
.. _Install PySide: http://qt-project.org/wiki/PySideDownloads
.. _Sphinx: http://sphinx.pocoo.org/
