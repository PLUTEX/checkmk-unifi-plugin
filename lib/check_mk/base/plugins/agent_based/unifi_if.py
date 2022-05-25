#!/usr/bin/env python3
# Copyright (C) 2022, Jan-Philipp Litza <jpl@plutex.de>.
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

import json
from .agent_based_api.v1 import register, type_defs
from .utils import interfaces


def parse_unifi_if(string_table: type_defs.StringTable) -> interfaces.Section:
    return [
        interfaces.Interface(
            index=str(port['port_idx']),
            descr=str(port['port_idx']),
            alias=port['name'],
            type='6',  # Ethernet
            speed=port.get('speed', 0) * 1000000,
            oper_status=('1' if port.get('up', True) else '2'),
            in_octets=float(port.get('rx_bytes', 0)),
            in_ucast=float(
                port.get('rx_packets', 0)
                - port.get('rx_multicast', 0)
                - port.get('rx_broadcast', 0)
            ),
            in_mcast=float(port.get('rx_multicast', 0)),
            in_bcast=float(port.get('rx_broadcast', 0)),
            in_discards=float(port.get('rx_dropped', 0)),
            in_errors=float(port.get('rx_errors', 0)),
            out_octets=float(port.get('tx_bytes', 0)),
            out_ucast=float(
                port.get('tx_packets', 0)
                - port.get('tx_multicast', 0)
                - port.get('tx_broadcast', 0)
            ),
            out_mcast=float(port.get('tx_multicast', 0)),
            out_bcast=float(port.get('tx_broadcast', 0)),
            out_discards=float(port.get('tx_dropped', 0)),
            out_errors=float(port.get('tx_errors', 0)),
            admin_status=('1' if port['enable'] else '2'),
        )
        for port in json.loads(string_table[0][0])
    ]


register.agent_section(
    name="unifi_if",
    parse_function=parse_unifi_if,
    parsed_section_name="interfaces",
    supersedes=["if", "if64", "if64adm"],
)
