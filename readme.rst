=============================
 safepact - Contractor Escrow
=============================

:Version: 0.1.0dev
:Web: http://safepact.com/
:Source: http://github.com/winhamwr/safepact/

--

.. _dev-installation:

Development Setup
=================

Safepact uses `Vagrant`_ to ease developer machine installation.

To set up a development environment::

 * Clone the git repository::

    $ cd ~/workspace
    $ git clone git@github.com:winhamwr/safepact.git safepact

 * Install `Vagrant`_ ::

    $ gem install vagrant
    $ vagrant box add lucid32 http://files.vagrantup.com/lucid32.box

 * Grab the git submodules ::

    $ cd safepact
    $ git submodule init
    $ git submodule update

 * Delete the broken tomcat6 cookbook ::

    $ rm -r config/site-cookbooks/opscode/tomcat6

 * UBUNTU ONLY. Ensure that NFS is installed ::

    $ sudo apt-get install nfs-common nfs-kernel-server

.. _`Vagrant`: http://vagrantup.com

.. _development-examples:

Development Examples
====================

 * Build the Vagrant environment::

    $ cd ~/workspace/safepact
    $ vagrant up

 * Create the development database::

    $ cd ~/workspace/safepact
    $ vagrant ssh
    $ cd safepact
    $ ./manage.py syncdb

 * Run the development server::

    $ cd ~/workspace/safepact
    $ vagrant ssh
    $ cd safepact
    $ ./manage.py runserver 0.0.0.0:8000

 * View the application in a browser via http://localhost:8800/
