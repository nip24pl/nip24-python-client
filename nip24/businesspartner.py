#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2024 NETCAT (www.netcat.pl)
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
# @copyright 2015-2024 NETCAT (www.netcat.pl)
# @license http://www.apache.org/licenses/LICENSE-2.0
#


class BusinessPartner:
    """
    Business partner data
    """

    def __init__(self):
        self.regon = None
        self.firmName = None
        self.firstName = None
        self.secondName = None
        self.lastName = None

    def __str__(self):
        return 'BusinessPartner: [regon = ' + str(self.regon) \
            + ', firmName = ' + str(self.firmName) \
            + ', firstName = ' + str(self.firstName) \
            + ', secondName = ' + str(self.secondName) \
            + ', lastName = ' + str(self.lastName) \
            + ']'
