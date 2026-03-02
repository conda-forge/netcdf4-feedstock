#!/bin/bash

if [[ $(uname) == Darwin ]]; then
    export LDFLAGS="-headerpad_max_install_names $LDFLAGS"
fi

export NETCDF4_LIMITED_API=1
export netCDF4_DIR=$PREFIX
export HDF5_DIR=$PREFIX

${PYTHON} -m pip install --no-deps --ignore-installed .
