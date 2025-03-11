4.8. musl-1.2.5 
===============

The musl package contains the main C library. This library provides the basic routines for allocating memory, searching directories, 
opening and closing files, reading and writing files, string handling, pattern matching, arithmetic, and so on.

4.8.1. Installation of musl
---------------------------

Configure the package:

.. code-block:: shell

  ./configure \
    CROSS_COMPILE=${CLFS_TARGET}- \
    --prefix=/ \
    --target=${CLFS_TARGET}

Compile the package:

.. code-block:: shell

    make

Install the package:

.. code-block:: shell

    DESTDIR=${CLFS}/cross-tools/${CLFS_TARGET} make install

.. _contents-musl:

4.8.2. Contents of musl
-----------------------


| **Installed Programs:**   ld-musl.so.0
| **Installed Libraries:**  libc.so.0, libcrypt.so.0, libdl.so.0, libm.so.0, libpthread.so.0, librt.so.0
| **Installed Headers:**    To be written...

Short Descriptions
~~~~~~~~~~~~~~~~~~

.. _ld-musl:

**ld-musl**
    The musl dynamic linker / loader

``libc``
	The C library

``libcrypt``	
    The cryptographic library

``libdl``
	The musl dynamic linker / loader library

``libm``
	The math library

``libpthread``
	The POSIX thread library

``librt``
	The clock and timer library 