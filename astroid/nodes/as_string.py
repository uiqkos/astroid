"""
as_string.py - Visitor to convert AST nodes to their string representation.

This visitor class implements visit methods for all node types.
"""

from astroid.nodes import NodeNG, Unknown

DOC_NEWLINE = "\n"

class AsStringVisitor:
    def __call__(self, node: NodeNG) -> str:
        return node.accept(self).replace(DOC_NEWLINE, "\n")

    def visit_unknown(self, node: Unknown) -> str:
        # Provide a string representation for Unknown nodes.
        # Since Unknown nodes represent unknown or unparsed code,
        # returning a placeholder string is appropriate.
        return "<unknown>"

    # Other visit_ methods for different node types would be here...