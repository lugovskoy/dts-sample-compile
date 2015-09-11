#!/bin/bash

WORKDIR=$1

cd $WORKDIR || exit 1
git clone git://repo.or.cz/tinycc.git tinycc || exit 1
