#!/usr/bin/python

from docutils import nodes
from docutils.parsers.rst import directives, roles

def math_jsmath_directive(name, arguments, options, content, lineno, 
                          content_offset, block_text, state, state_machine):
    """
    Provides a math directive for docutils which embeds the equation i \[\] 
    to be picked up by jsMath.
    """
    format = '\\[%s\\]'
    return [nodes.raw("", format % '\n'.join(content), format='html')]

def math_jsmath_role(name, rawtext, text, lineno, inliner, options={}, 
                     content=[]):
    """
    Provides a role for docutils to pick up and convert to jsMath syntax.
    """
    format = "\\(%s\\)"
    return [nodes.raw(
                      rawtext, 
                      format % rawtext.strip('`').replace(r'\\\\', r'\\'),
                      format='html'
            )], []
