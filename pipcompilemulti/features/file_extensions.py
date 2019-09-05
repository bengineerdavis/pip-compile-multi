"""
Requirements Files Extensions
=============================

By default ``pip-compile-multi`` compiles ``*.txt`` from ``*.in`` files.
While this is a common naming pattern, each project can use it's own:

.. code-block:: text

    -i, --in-ext TEXT      File extension of input files
    -o, --out-ext TEXT     File extension of output files
"""

from .base import BaseFeature, ClickOption
from ..options import OPTIONS


class InputExtension(BaseFeature):
    """Override input file extension."""

    OPTION_NAME = 'in_ext'
    CLICK_OPTION = ClickOption(
        long_option='--in-ext',
        short_option='-i',
        default="in",
        is_flag=False,
        help_text='File extension of input files.',
    )

    @property
    def value(self):
        """Extension string."""
        return OPTIONS[self.OPTION_NAME]

    def compose_input_file_name(self, env_name):
        """Compose file name given environment name.

        >>> InputExtension().compose_input_file_name('base')
        'base.in'
        """
        return '{0}.{1}'.format(env_name, self.value)
