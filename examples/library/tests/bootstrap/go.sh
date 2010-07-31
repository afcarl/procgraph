#!/bin/bash

logdir=${PBENV_DATA}/rawseeds/$1

pg laser_boot \
	hokuyo_front.file=${logdir}/HOKUYO_FRONT.csv.bz2 \
	hokuyo_rear.file=${logdir}/HOKUYO_REAR.csv.bz2 \
	sick_front.file=${logdir}/SICK_FRONT.csv.bz2 \
	sick_rear.file=${logdir}/SICK_REAR.csv.bz2 \
	odometry.file=${logdir}/ODOMETRY_XYT.csv.bz2 \
	out=${logdir}/rawseeds_laser_boot.avi\
	mencoder.vcodec=mjpeg
#	mencoder.vcodec=ljpeg
	# svs_t.dir=${logdir}/SVS_T \
	# svs_r.dir=${logdir}/SVS_R \
	# svs_l.dir=${logdir}/SVS_L \
	# omni.dir=${logdir}/OMNI \
	# frontal.dir=${logdir}/FRONTAL\
