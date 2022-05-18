<%!
    import pydmt.helpers.misc
    import config.project
    import config.python
    import user.personal
    import config.version
    line = '=' * (len(config.project.name)+2)
%>${line}
*${config.project.name}*
${line}

.. image:: https://img.shields.io/pypi/v/${config.python.package_name}

.. image:: https://img.shields.io/github/license/veltzer/${config.project.name}

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg

project website: ${config.project.website}

author: ${user.personal.personal_fullname}

version: ${pydmt.helpers.misc.get_version_str()}

<%include file="../snipplets/main.rst.mako" />
