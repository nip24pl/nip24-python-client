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


class WLStatus:
    """
    Whitelist status info
    """

    def __init__(self):
        self.uid = None
        self.nip = None
        self.iban = None
        self.valid = None
        self.virtual = None
        self.status = None
        self.result = None
        self.hashIndex = None
        self.maskIndex = None
        self.date = None
        self.source = None

    def __str__(self):
        return 'WLStatus: [uid = ' + str(self.uid) \
            + ', nip = ' + str(self.nip) \
            + ', iban = ' + str(self.iban) \
            + ', valid = ' + str(self.valid) \
            + ', virtual = ' + str(self.virtual) \
            + ', status = ' + str(self.status) \
            + ', result = ' + str(self.result) \
            + ', hashIndex = ' + str(self.hashIndex) \
            + ', maskIndex = ' + str(self.maskIndex) \
            + ', date = ' + str(self.date) \
            + ', source = ' + str(self.source) \
            + ']'
