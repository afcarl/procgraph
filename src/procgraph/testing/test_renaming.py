from procgraph.testing.utils import PGTestCase


class TestRenaming(PGTestCase):
    def test_renaming(self):
        ''' Sometimes instancing a block twice will give error because
            we overwrote the parsed spec. '''
        model_spec = """
--- model loaders

|input name=y|  --> |derivative| --> y_dot
y_dot  --> |derivative| --> y_ddot
 
         """
        self.check_semantic_ok(model_spec)
