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


class VIESData:
    """
    VIES data
    """

    def __init__(self):
        self.uid = None
        self.countryCode = None
        self.vatNumber = None
        self.valid = None
        self.traderName = None
        self.traderCompanyType = None
        self.traderAddress = None
        self.id = None
        self.date = None
        self.source = None

    def __str__(self):
        return 'VIESData: [uid = ' + str(self.uid) \
            + ', countryCode = ' + str(self.countryCode) \
            + ', vatNumber = ' + str(self.vatNumber) \
            + ', valid = ' + str(self.valid) \
            + ', traderName = ' + str(self.traderName) \
            + ', traderCompanyType = ' + str(self.traderCompanyType) \
            + ', traderAddress = ' + str(self.traderAddress) \
            + ', id = ' + str(self.id) \
            + ', date = ' + str(self.date) \
            + ', source = ' + str(self.source) \
            + ']'
