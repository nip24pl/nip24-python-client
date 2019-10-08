#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2019 NETCAT (www.netcat.pl)
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
# @copyright 2015-2019 NETCAT (www.netcat.pl)
# @license http://www.apache.org/licenses/LICENSE-2.0
#

import re
import string


class IBAN:
    """
    IBAN verificator
    """

    @staticmethod
    def normalize(iban):
        """
        Normalizes form of the IBAN number

        :param iban: input string
        :type iban: str
        :returns: normalized string or False
        :rtype: str or False
        """

        if not iban:
            return False

        iban = re.sub('[ -]', '', iban).upper()

        if not re.match('[A-Z]{2}[0-9A-Z]{13,30}', iban):
            return False

        return iban

    @staticmethod
    def isValid(iban):
        """
        Checks if specified IBAN is valid

        :param iban: input string
        :type iban: str
        :returns: True if IBAN is valid
        :rtype: bool
        """

        iban = IBAN.normalize(iban)

        if not iban:
            return False

        map = {
            'AD': 'AD\\d{10}[A-Z0-9]{12}',
            'AE': 'AE\\d{21}',
            'AL': 'AL\\d{10}[A-Z0-9]{16}',
            'AT': 'AT\\d{18}',
            'AZ': 'AZ\\d{2}[A-Z]{4}[A-Z0-9]{20}',
            'BA': 'BA\\d{18}',
            'BE': 'BE\\d{14}',
            'BG': 'BG\\d{2}[A-Z]{4}\\d{6}[A-Z0-9]{8}',
            'BH': 'BH\\d{2}[A-Z]{4}[A-Z0-9]{14}',
            'BR': 'BR\\d{25}[A-Z]{1}[A-Z0-9]{1}',
            'BY': 'BY\\d{2}[A-Z0-9]{4}\\d{4}[A-Z0-9]{16}',
            'CH': 'CH\\d{7}[A-Z0-9]{12}',
            'CR': 'CR\\d{20}',
            'CY': 'CY\\d{10}[A-Z0-9]{16}',
            'CZ': 'CZ\\d{22}',
            'DE': 'DE\\d{20}',
            'DK': 'DK\\d{16}',
            'DO': 'DO\\d{2}[A-Z0-9]{4}\\d{20}',
            'EE': 'EE\\d{18}',
            'ES': 'ES\\d{22}',
            'FI': 'FI\\d{16}',
            'FO': 'FO\\d{16}',
            'FR': 'FR\\d{12}[A-Z0-9]{11}\\d{2}',
            'GB': 'GB\\d{2}[A-Z]{4}\\d{14}',
            'GE': 'GE\\d{2}[A-Z]{2}\\d{16}',
            'GI': 'GI\\d{2}[A-Z]{4}[A-Z0-9]{15}',
            'GL': 'GL\\d{16}',
            'GR': 'GR\\d{9}[A-Z0-9]{16}',
            'GT': 'GT\\d{2}[A-Z0-9]{24}',
            'HR': 'HR\\d{19}',
            'HU': 'HU\\d{26}',
            'IE': 'IE\\d{2}[A-Z]{4}\\d{14}',
            'IL': 'IL\\d{21}',
            'IQ': 'IQ\\d{2}[A-Z]{4}\\d{15}',
            'IS': 'IS\\d{24}',
            'IT': 'IT\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}',
            'JO': 'JO\\d{2}[A-Z]{4}\\d{4}[A-Z0-9]{18}',
            'KW': 'KW\\d{2}[A-Z]{4}[A-Z0-9]{22}',
            'KZ': 'KZ\\d{5}[A-Z0-9]{13}',
            'LB': 'LB\\d{6}[A-Z0-9]{20}',
            'LC': 'LC\\d{2}[A-Z]{4}[A-Z0-9]{24}',
            'LI': 'LI\\d{7}[A-Z0-9]{12}',
            'LT': 'LT\\d{18}',
            'LU': 'LU\\d{5}[A-Z0-9]{13}',
            'LV': 'LV\\d{2}[A-Z]{4}[A-Z0-9]{13}',
            'MC': 'MC\\d{12}[A-Z0-9]{11}\\d{2}',
            'MD': 'MD\\d{2}[A-Z0-9]{20}',
            'ME': 'ME\\d{20}',
            'MK': 'MK\\d{5}[A-Z0-9]{10}\\d{2}',
            'MR': 'MR\\d{25}',
            'MT': 'MT\\d{2}[A-Z]{4}\\d{5}[A-Z0-9]{18}',
            'MU': 'MU\\d{2}[A-Z]{4}\\d{19}[A-Z]{3}',
            'NL': 'NL\\d{2}[A-Z]{4}\\d{10}',
            'NO': 'NO\\d{13}',
            'PK': 'PK\\d{2}[A-Z]{4}[A-Z0-9]{16}',
            'PL': 'PL\\d{26}',
            'PS': 'PS\\d{2}[A-Z]{4}[A-Z0-9]{21}',
            'PT': 'PT\\d{23}',
            'QA': 'QA\\d{2}[A-Z]{4}[A-Z0-9]{21}',
            'RO': 'RO\\d{2}[A-Z]{4}[A-Z0-9]{16}',
            'RS': 'RS\\d{20}',
            'SA': 'SA\\d{4}[A-Z0-9]{18}',
            'SC': 'SC\\d{2}[A-Z]{4}\\d{20}[A-Z]{3}',
            'SE': 'SE\\d{22}',
            'SI': 'SI\\d{17}',
            'SK': 'SK\\d{22}',
            'SM': 'SM\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}',
            'ST': 'ST\\d{23}',
            'SV': 'SV\\d{2}[A-Z]{4}\\d{20}',
            'TL': 'TL\\d{21}',
            'TN': 'TN\\d{22}',
            'TR': 'TR\\d{8}[A-Z0-9]{16}',
            'UA': 'UA\\d{8}[A-Z0-9]{19}',
            'VG': 'VG\\d{2}[A-Z]{4}\\d{16}',
            'XK': 'XK\\d{18}'
        }

        cc = iban[0:2].upper()

        if cc not in map:
            return False

        if not re.match(map[cc], iban):
            return False

        chars = string.digits + string.ascii_uppercase
        iban = iban[4:] + iban[:4]
        num = int(''.join(str(chars.index(c)) for c in iban))

        return num % 97 == 1
