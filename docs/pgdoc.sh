
packages="procgraph.components procgraph_pil procgraph_cv procgraph_hdf procgraph_pil procgraph_robotics procgraph_mpl procgraph_foo"

pgdoc --translate `pwd`/..=https://github.com/AndreaCensi/procgraph/blob/master --label 'pgdoc:procgraph.components' --output source/pgdoc.rst $packages
