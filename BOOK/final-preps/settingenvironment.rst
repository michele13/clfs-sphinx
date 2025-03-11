3.3. Setting Up the Environment
===============================

Set up a good working environment by creating two new startup files for the **bash** shell. 
While logged in as user *clfs*, issue the following command to create a new ``.bash_profile``: 

.. code-block:: shell

    cat > ~/.bash_profile << "EOF"
    exec env -i HOME=${HOME} TERM=${TERM} PS1='\u:\w\$ ' /bin/bash
    EOF

When logged on as user *clfs*, the initial shell is usually a login shell which reads the ``/etc/profile``  of the host (probably containing 
some settings and environment variables) and then ``.bash_profile``. The exec **env -i.../bin/bash** command in the ``.bash_profile`` file replaces 
the running shell with a new one with a completely empty environment, except for the ``HOME``, ``TERM``, and ``PS1`` variables. 
This ensures that no unwanted and potentially hazardous environment variables from the host system leak into the build environment. 
The technique used here achieves the goal of ensuring a clean environment. 

The new instance of the shell is a non-login shell, which does not read the ``/etc/profile`` or ``.bash_profile`` files, but rather reads 
the ``.bashrc`` file instead. Create the ``.bashrc`` file now: 

.. code-block:: shell

    cat > ~/.bashrc << "EOF"
    set +h
    umask 022
    CLFS=/mnt/clfs
    LC_ALL=POSIX
    PATH=${CLFS}/cross-tools/bin:/bin:/usr/bin
    export CLFS LC_ALL PATH
    EOF

The **set +h** command turns off **bash**'s hash function. Hashing is ordinarily a useful feature —**bash** uses a hash table
to remember the full path of executable files to avoid searching the ``PATH`` time and again to find the same executable.
However, the new tools should be used as soon as they are installed. By switching off the hash function, the shell will always search 
the ``PATH`` when a program is to be run. As such, the shell will find the newly compiled tools in ``${CLFS}/cross-tools``
as soon as they are available without remembering a previous version of the same program in a different location.

Setting the user file-creation mask (umask) to 022 ensures that newly created files and directories are only writable by their owner, 
but are readable and executable by anyone (assuming default modes are used by the open(2) system call, new files will end up 
with permission mode 644 and directories with mode 755). 

The ``CLFS`` variable should be set to the chosen mount point.

The ``LC_ALL`` variable controls the localization of certain programs, making their messages follow the conventions of a specified country.
If the host system uses a version of Glibc older than 2.2.4, having ``LC_ALL`` set to something other than “POSIX” or “C” 
(during this chapter) may cause issues. 

By putting ``${CLFS}/cross-tools`` at the beginning of the ``PATH``, the cross-compiler built in 
:doc:`Constructing Cross-Compile Tools<../part3>` will be picked up by the build process for the temp-system packages before 
anything that may be installed on the host. This, combined with turning off hashing, helps to ensure that you will be using the 
cross-compile tools to build the temp-system in ``/tools``. 

Finally, to have the environment fully prepared for building the temporary tools, source the just-created user profile: 

.. code-block:: shell

    source ~/.bash_profile

