#!/usr/bin/env bash

BASE=$(dirname $(readlink -f ${0}))

cd ${BASE}

git clean -f -d -x
