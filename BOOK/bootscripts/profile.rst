7.4. Creating /etc/profile
==========================

Is the file that specifices how your environment will function.

Now we will create the profile file for use with our system:

.. code-block:: shell

    cat > ${CLFS}/targetfs/etc/profile << "EOF"
    # /etc/profile

    # Set the initial path
    export PATH=/bin:/usr/bin

    if [ `id -u` -eq 0 ] ; then
            PATH=/bin:/sbin:/usr/bin:/usr/sbin
            unset HISTFILE
    fi

    # Setup some environment variables.
    export USER=`id -un`
    export LOGNAME=$USER
    export HOSTNAME=`/bin/hostname`
    export HISTSIZE=1000
    export HISTFILESIZE=1000
    export PAGER='/bin/more '
    export EDITOR='/bin/vi'

    # End /etc/profile
    EOF