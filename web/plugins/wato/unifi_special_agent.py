#!/usr/bin/env python3
# Copyright (C) 2021, Jan-Philipp Litza <jpl@plutex.de>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    TextAscii,
    Password,
    Integer,
    FixedValue,
)

from cmk.gui.plugins.wato import (
    HostRulespec,
    rulespec_registry,
)
from cmk.gui.plugins.wato.datasource_programs import (
    RulespecGroupDatasourceProgramsApps,
)


def _valuespec_special_agents_unifi():
    return Dictionary(elements=[
        ("username", TextAscii(
            title=_("Username"),
            allow_empty=False,
        )),
        ("password", Password(
            title=_("Password"),
            allow_empty=False,
        )),
        ("port", Integer(
            title=_("Port"),
            default_value=443,
        )),
        ("no-cert-check", FixedValue(
            True,
            title=_("Disable SSL certificate validation"),
            totext=_("SSL certificate validation is disabled"),
        )),
    ])


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsApps,
        name="special_agents:unifi",
        title=lambda: _("Ubiquiti Unifi"),
        valuespec=_valuespec_special_agents_unifi,
    ))
