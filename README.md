mkchroot
========

Create a basic chroot environment by copying binaries and their library
dependencies into a directory.

Usage
=====

Create a basic chroot in the directory `$HOME/chroot` with only the binaries
`/bin/bash` and `/bin/ls` provided.

    $ mkchroot $HOME/chroot /bin/bash /bin/ls

There is also a test mode (dry run mode) which can be invoked using the `-n`
option, which causes the program to take no action, and instead show you what
would happen.

Caveats
=======

This program does not attempt to identify anything other than library
dependencies of ELF binaries. For example, it will not try to detect the
dependencies of shell scripts, and it will not try to detect runtime
dependencies (other programs called with fork/exec).

This program will also not identify device nodes which may be needed by the
binaries running inside the chroot. You will need to create these yourself. You
may also need to mount the `/proc` filesystem inside your chroot.

Some distributions (such as CentOS 7) symlink `/bin` -> `/usr/bin`. If your
binaries depend on this, you will need to create these symlinks yourself.

Thanks
======

This program was inspired by this blog post:

<http://www.metashock.de/2012/11/export-binary-with-lib-dependencies/>
