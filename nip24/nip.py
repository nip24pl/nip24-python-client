#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2019 NETCAT (www.netcat.pl)
#
# Licensed under the Apache License, Version 2.0 (the "License");
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


class NIP:
    """
    NIP number validator
    """

    @staticmethod
    def normalize(nip):
        """
        Normalizes form of the NIP number

        :param nip: input string
        :type nip: str
        :returns: normalized string or False
        :rtype: str or False
        """

        if not nip:
            return False

        nip = nip.strip().translate(None, '-')

        if not re.match('[0-9]{10}', nip):
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

        nip = NIP.normalize(nip)

        if not nip:
            return False

        w = [ 6, 5, 7, 2, 3, 4, 5, 6, 7 ]
        sum = 0

        for i in range(0, len(w)):
            sum += int(nip[i]) * w[i]

        sum %= 11

        if sum != int(nip[9]):
            return False

        return True