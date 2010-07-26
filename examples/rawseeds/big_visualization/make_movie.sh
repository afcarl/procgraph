#!/bin/bash

logdir=${PBENV_DATA}/rawseeds/$1

pg all.pg \
	hokuyo_front.file=${logdir}/HOKUYO_FRONT.csv.bz2 \
	hokuyo_rear.file=${logdir}/HOKUYO_REAR.csv.bz2 \
	sick_front.file=${logdir}/SICK_FRONT.csv.bz2 \
	sick_rear.file=${logdir}/SICK_REAR.csv.bz2 \
	svs_t.dir=${logdir}/SVS_T \
	svs_r.dir=${logdir}/SVS_R \
	svs_l.dir=${logdir}/SVS_L \
	omni.dir=${logdir}/OMNI \
	frontal.dir=${logdir}/FRONTAL\
	out=${logdir}/display-all.avi

