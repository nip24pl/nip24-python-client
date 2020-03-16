#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2020 NETCAT (www.netcat.pl)
#
# Licensed under the Apache License, Version 2.0 (the "License"),
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author NETCAT <firma@netcat.pl>
# @copyright 2015-2020 NETCAT (www.netcat.pl)
# @license http://www.apache.org/licenses/LICENSE-2.0
#

import re

from nip24 import NIP


class EUVAT:
    """
    EU VAT number verificator
    """

    @staticmethod
    def normalize(nip):
        """
        Normalizes form of the VAT number

        :param nip: input string
        :type nip: str
        :returns: normalized string or False
        :rtype: str or False
        """

        if not nip:
            return False

        nip = re.sub('[ -]', '', nip).upper()

        if not re.match('[A-Z]{2}[A-Z0-9]{2,12}', nip):
            return False

        return nip

    @staticmethod
    def isValid(nip):
        """
        Checks if specified NIP is valid

        :param nip: input string
        :type nip: str
        :returns: True if NIP is valid
        :rtype: bool
        """

        nip = EUVAT.normalize(nip)

        if not nip:
            return False

        map = {
            'AT': 'ATU\\d{8}',
            'BE': 'BE0\\d{9}',
            'BG': 'BG\\d{9,10}',
            'CY': 'CY\\d{8}[A-Z]{1}',
            'CZ': 'CZ\\d{8,10}',
            'DE': 'DE\\d{9}',
            'DK': 'DK\\d{8}',
            'EE': 'EE\\d{9}',
            'EL': 'EL\\d{9}',
            'ES': 'ES[A-Z0-9]{9}',
            'FI': 'FI\\d{8}',
            'FR': 'FR[A-Z0-9]{2}\\d{9}',
            'GB': 'GB[A-Z0-9]{5,12}',
            'HR': 'HR\\d{11}',
            'HU': 'HU\\d{8}',
            'IE': 'IE[A-Z0-9]{8,9}',
            'IT': 'IT\\d{11}',
            'LT': 'LT\\d{9,12}',
            'LU': 'LU\\d{8}',
            'LV': 'LV\\d{11}',
            'MT': 'MT\\d{8}',
            'NL': 'NL\\d{9}B\\d{2}',
            'PL': 'PL\\d{10}',
            'PT': 'PT\\d{9}',
            'RO': 'RO\\d{2,10}',
            'SE': 'SE\\d{12}',
            'SI': 'SI\\d{8}',
            'SK': 'SK\\d{10}'
        }

        cc = nip[0:2].upper()
        num = nip[2:].upper()

        if cc not in map:
            return False

        if not re.match(map[cc], nip):
            return False

        if cc == 'PL':
            return NIP.isValid(num)

        return True
