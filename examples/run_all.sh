#!/bin/bash
set -e
set -x

pg tutorial0_basics

pg tutorial1_signals

pg tutorial3_config in=coastguard.mp4 out=coastguard3.avi

# pg tutorial4_models in=coastguard.mp4 out=coastguard4.avi
 
# pg tutorial5_config_advanced  in=coastguard.mp4 out=coastguard5.avi

pg tutorial6_signals_advanced 

pg tutorial7_simple_blocks

pg tutorial8_simple_blocks_conf

pg tutorial9_best_practices

pg tutorial10_stateful_blocks







