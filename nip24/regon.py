#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2020 NETCAT (www.netcat.pl)
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
# @copyright 2015-2020 NETCAT (www.netcat.pl)
# @license http://www.apache.org/licenses/LICENSE-2.0
#

import re

class REGON:
    """
    REGON number validator
    """

    @staticmethod
    def normalize(regon):
        """
        Normalizes form of the REGON number

        :param regon: input string
        :type regon: str
        :returns: normalized string or False
        :rtype: str or False
        """

        if not regon:
            return False

        regon = regon.strip()

        if not re.match('[0-9]{9,14}', regon):
            return False

        if len(regon) != 9 and len(regon) != 14:
            return False

        return regon

    @staticmethod
    def isValid(regon):
        """
        Checks if specified REGON is valid

        :param regon: input string
        :type regon: str
        :returns: True if NIP is valid
        :rtype: bool
        """

        regon = REGON.normalize(regon)

        if not regon:
            return False

        if len(regon) == 9:
            return REGON.__isValidR9(regon)
        else:
            if not REGON.__isValidR9(regon[0:9]):
                return False

            return REGON.__isValidR14(regon)

    @staticmethod
    def __isValidR9(regon):
        """
        Check 9-digit REGON number

        :param regon: input string
        :type regon: str
        :returns: True if NIP is valid
        :rtype: bool
        """

        w = [ 8, 9, 2, 3, 4, 5, 6, 7 ]
        sum = 0

        for i in range(0, len(w)):
            sum += int(regon[i]) * w[i]

        sum %= 11

        if (sum == 10):
            sum = 0

        if sum != int(regon[8]):
            return False

        return True

    @staticmethod
    def __isValidR14(regon):
        """
        Check 14-digit REGON number

        :param regon: input string
        :type regon: str
        :returns: True if NIP is valid
        :rtype: bool
        """

        w = [ 2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8 ]
        sum = 0

        for i in range(0, len(w)):
            sum += int(regon[i]) * w[i]

        sum %= 11

        if (sum == 10):
            sum = 0

        if sum != int(regon[13]):
            return False

        return True
