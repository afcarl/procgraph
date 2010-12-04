
from procgraph import register_simple_block
from procgraph.components.images.copied_from_reprep import skim_top_and_bottom

register_simple_block(
  skim_top_and_bottom, 'skim',
  params={'percent': 5},
  doc='Skims the top and bottom percentile from the data.')
