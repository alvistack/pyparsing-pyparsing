# module pyparsing.py
#
# Copyright (c) 2003-2021  Paul T. McGuire
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__doc__ = """
pyparsing module - Classes and methods to define and execute parsing grammars
=============================================================================

The pyparsing module is an alternative approach to creating and
executing simple grammars, vs. the traditional lex/yacc approach, or the
use of regular expressions.  With pyparsing, you don't need to learn
a new syntax for defining grammars or matching expressions - the parsing
module provides a library of classes that you use to construct the
grammar directly in Python.

Here is a program to parse "Hello, World!" (or any greeting of the form
``"<salutation>, <addressee>!"``), built up using :class:`Word`,
:class:`Literal`, and :class:`And` elements
(the :meth:`'+'<ParserElement.__add__>` operators create :class:`And` expressions,
and the strings are auto-converted to :class:`Literal` expressions)::

    from pyparsing import Word, alphas

    # define grammar of a greeting
    greet = Word(alphas) + "," + Word(alphas) + "!"

    hello = "Hello, World!"
    print(hello, "->", greet.parse_string(hello))

The program outputs the following::

    Hello, World! -> ['Hello', ',', 'World', '!']

The Python representation of the grammar is quite readable, owing to the
self-explanatory class names, and the use of :class:`'+'<And>`,
:class:`'|'<MatchFirst>`, :class:`'^'<Or>` and :class:`'&'<Each>` operators.

The :class:`ParseResults` object returned from
:class:`ParserElement.parseString` can be
accessed as a nested list, a dictionary, or an object with named
attributes.

The pyparsing module handles some of the problems that are typically
vexing when writing text parsers:

  - extra or missing whitespace (the above program will also handle
    "Hello,World!", "Hello  ,  World  !", etc.)
  - quoted strings
  - embedded comments


Getting Started -
-----------------
Visit the classes :class:`ParserElement` and :class:`ParseResults` to
see the base classes that most other pyparsing
classes inherit from. Use the docstrings for examples of how to:

 - construct literal match expressions from :class:`Literal` and
   :class:`CaselessLiteral` classes
 - construct character word-group expressions using the :class:`Word`
   class
 - see how to create repetitive expressions using :class:`ZeroOrMore`
   and :class:`OneOrMore` classes
 - use :class:`'+'<And>`, :class:`'|'<MatchFirst>`, :class:`'^'<Or>`,
   and :class:`'&'<Each>` operators to combine simple expressions into
   more complex ones
 - associate names with your parsed results using
   :class:`ParserElement.setResultsName`
 - access the parsed data, which is returned as a :class:`ParseResults`
   object
 - find some helpful expression short-cuts like :class:`delimitedList`
   and :class:`oneOf`
 - find more useful common expressions in the :class:`pyparsing_common`
   namespace class
"""
from collections import namedtuple

version_info = namedtuple("version_info", "major minor micro release_level serial")
__version_info__ = version_info(3, 0, 0, "candidate", 2)
__version__ = (
    "{}.{}.{}".format(*__version_info__[:3])
    + (
        "{}{}{}".format(
            "r" if __version_info__.release_level[0] == "c" else "",
            __version_info__.release_level[0],
            __version_info__.serial,
        ),
        "",
    )[__version_info__.release_level == "final"]
)
__version_time__ = "9 September 2021 19:06 UTC"
__versionTime__ = __version_time__
__author__ = "Paul McGuire <ptmcg@users.sourceforge.net>"

from .util import *
from .exceptions import *
from .actions import *
from .core import __diag__, __compat__
from .results import *
from .core import *
from .core import _builtin_exprs as core_builtin_exprs
from .helpers import *
from .helpers import _builtin_exprs as helper_builtin_exprs

from .unicode import unicode_set, pyparsing_unicode as unicode
from .testing import pyparsing_test as testing
from .common import (
    pyparsing_common as common,
    _builtin_exprs as common_builtin_exprs,
)

# define backward compat synonyms
if "pyparsing_unicode" not in globals():
    pyparsing_unicode = unicode
if "pyparsing_common" not in globals():
    pyparsing_common = common
if "pyparsing_test" not in globals():
    pyparsing_test = testing

core_builtin_exprs += common_builtin_exprs + helper_builtin_exprs


__all__ = [
    "__version__",
    "__version_time__",
    "__author__",
    "__compat__",
    "__diag__",
    "And",
    "CaselessKeyword",
    "CaselessLiteral",
    "CharsNotIn",
    "Combine",
    "Dict",
    "Each",
    "Empty",
    "FollowedBy",
    "Forward",
    "GoToColumn",
    "Group",
    "IndentedBlock",
    "Keyword",
    "LineEnd",
    "LineStart",
    "Literal",
    "Located",
    "PrecededBy",
    "MatchFirst",
    "NoMatch",
    "NotAny",
    "OneOrMore",
    "OnlyOnce",
    "OpAssoc",
    "Opt",
    "Optional",
    "Or",
    "ParseBaseException",
    "ParseElementEnhance",
    "ParseException",
    "ParseExpression",
    "ParseFatalException",
    "ParseResults",
    "ParseSyntaxException",
    "ParserElement",
    "QuotedString",
    "RecursiveGrammarException",
    "Regex",
    "SkipTo",
    "StringEnd",
    "StringStart",
    "Suppress",
    "Token",
    "TokenConverter",
    "White",
    "Word",
    "WordEnd",
    "WordStart",
    "ZeroOrMore",
    "Char",
    "alphanums",
    "alphas",
    "alphas8bit",
    "any_close_tag",
    "any_open_tag",
    "c_style_comment",
    "col",
    "common_html_entity",
    "counted_array",
    "cpp_style_comment",
    "dbl_quoted_string",
    "dbl_slash_comment",
    "delimited_list",
    "dict_of",
    "empty",
    "hexnums",
    "html_comment",
    "identchars",
    "identbodychars",
    "java_style_comment",
    "line",
    "line_end",
    "line_start",
    "lineno",
    "make_html_tags",
    "make_xml_tags",
    "match_only_at_col",
    "match_previous_expr",
    "match_previous_literal",
    "nested_expr",
    "null_debug_action",
    "nums",
    "one_of",
    "printables",
    "punc8bit",
    "python_style_comment",
    "quoted_string",
    "remove_quotes",
    "replace_with",
    "replace_html_entity",
    "rest_of_line",
    "sgl_quoted_string",
    "srange",
    "string_end",
    "string_start",
    "trace_parse_action",
    "unicode_string",
    "with_attribute",
    "indentedBlock",
    "original_text_for",
    "ungroup",
    "infix_notation",
    "locatedExpr",
    "with_class",
    "CloseMatch",
    "token_map",
    "pyparsing_common",
    "pyparsing_unicode",
    "unicode_set",
    "condition_as_parse_action",
    "pyparsing_test",
    # pre-PEP8 compatibility names
    "__versionTime__",
    "anyCloseTag",
    "anyOpenTag",
    "cStyleComment",
    "commonHTMLEntity",
    "countedArray",
    "cppStyleComment",
    "dblQuotedString",
    "dblSlashComment",
    "delimitedList",
    "dictOf",
    "htmlComment",
    "javaStyleComment",
    "lineEnd",
    "lineStart",
    "makeHTMLTags",
    "makeXMLTags",
    "matchOnlyAtCol",
    "matchPreviousExpr",
    "matchPreviousLiteral",
    "nestedExpr",
    "nullDebugAction",
    "oneOf",
    "opAssoc",
    "pythonStyleComment",
    "quotedString",
    "removeQuotes",
    "replaceHTMLEntity",
    "replaceWith",
    "restOfLine",
    "sglQuotedString",
    "stringEnd",
    "stringStart",
    "traceParseAction",
    "unicodeString",
    "withAttribute",
    "indentedBlock",
    "originalTextFor",
    "infixNotation",
    "locatedExpr",
    "withClass",
    "tokenMap",
    "conditionAsParseAction",
]
