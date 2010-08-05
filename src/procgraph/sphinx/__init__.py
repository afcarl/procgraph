# Import Docutils document tree nodes module.
from docutils import nodes
# Import ``directives`` module (contains conversion functions).
from docutils.parsers.rst import directives
# Import Directive base class.
from docutils.parsers.rst import Directive


from sphinx.util.compat import (Directive,
                                make_admonition)




def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))

class Image(Directive):

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'alt': directives.unchanged,
                   'height': directives.nonnegative_int,
                   'width': directives.nonnegative_int,
                   'scale': directives.nonnegative_int,
                   'align': align,
                   }
    has_content = False

    def run(self):
        reference = directives.uri(self.arguments[0])
        self.options['uri'] = reference
        image_node = nodes.image(rawsource=self.block_text,
                                 **self.options)
        return [image_node]



class mongodoc(nodes.Admonition, nodes.Element):
    pass



class Block(Directive):

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True 
    has_content = True

    def run(self):
        block_type = self.arguments[0]
        
        self.assert_has_content()
        text = '\n'.join(self.content)
        text = 'Block %s\n-----------\n\n' % block_type + text
        classes = ['block-content']
        node = nodes.container(text)
        node['classes'].extend(classes)
        
        self.state.nested_parse(self.content, self.content_offset, node)
        

#        header = nodes.header('Block %s' % block_type)
        
        return [node]
 
 


def setup(app):
    app.add_directive('block', Block)
    return
