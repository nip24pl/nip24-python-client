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

class KRS:
    """
    KRS number validator
    """

    @staticmethod
    def normalize(krs):
        """
        Normalizes form of the KRS number

        :param krs: input string
        :type krs: str
        :returns: normalized string or False
        :rtype: str or False
        """

        if not krs:
            return False

        krs = krs.strip().zfill(10)

        if not re.match('[0-9]{10}', krs):
            return False

        return krs

    @staticmethod
    def isValid(krs):
        """
        Checks if specified KRS is valid

        :param nip: input string
        :type nip: str
        :returns: True if NIP is valid
        :rtype: bool
        """

        krs = KRS.normalize(krs)

        if not krs:
            return False

        return True
