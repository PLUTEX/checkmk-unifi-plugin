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

from .agent_based_api.v1 import register, Service, Result, State


def discover_single(section):
    yield Service()


def check_unifi(section):
    state = section[0][0]
    if ['1'] not in section:
        yield Result(state=State.CRIT, summary=f'Device state is {state}')
    else:
        yield Result(state=State.OK, summary='Device is connected')


register.check_plugin(
    name="unifi",
    service_name="Unifi controller",
    discovery_function=discover_single,
    check_function=check_unifi,
)
