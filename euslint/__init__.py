import pkg_resources

from euslint.lint import lint  # NOQA
from euslint.parse import parse  # NOQA
from euslint.test import test_line_length  # NOQA
from euslint.test import test_parenthesis  # NOQA
from euslint.test import test_tab  # NOQA
from euslint.test import test_whitespace  # NOQA


__version__ = pkg_resources.get_distribution('euslint').version
