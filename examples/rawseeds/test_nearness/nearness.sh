#!/bin/bash

logdir=${PBENV_DATA}/rawseeds/$1

pg nearness.pg \
	svs_r.dir=${logdir}/SVS_T \
	svs_l.dir=${logdir}/SVS_L \
	out=${logdir}/nearness.avi

