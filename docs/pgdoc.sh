
packages="procgraph.components procgraph_cv procgraph_foo procgraph_hdf procgraph_images procgraph_io_misc procgraph_mpl procgraph_mplayer procgraph_numpy_ops procgraph_pil procgraph_robotics procgraph_signals procgraph_statistics"


pgdoc --translate `pwd`/..=https://github.com/AndreaCensi/procgraph/blob/master  --output source/pgdoc.inc $packages
