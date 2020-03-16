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


class InvoiceData:
    """
    Invoice data
    """

    def __init__(self):
        self.uid = None
        self.nip = None
        self.name = None
        self.firstname = None
        self.lastname = None
        self.street = None
        self.streetNumber = None
        self.houseNumber = None
        self.city = None
        self.postCode = None
        self.postCity = None
        self.phone = None
        self.email = None
        self.www = None

    def __str__(self):
        return 'InvoiceData: [uid = ' + str(self.uid) \
            + ', nip = ' + str(self.nip) \
            + ', name = ' + str(self.name) \
            + ', firstName = ' + str(self.firstname) \
            + ', lastName = ' + str(self.lastname) \
            + ', street = ' + str(self.street) \
            + ', streetNumber = ' + str(self.streetNumber) \
            + ', houseNumber = ' + str(self.houseNumber) \
            + ', city = ' + str(self.city) \
            + ', postCode = ' + str(self.postCode) \
            + ', postCity = ' + str(self.postCity) \
            + ', phone = ' + str(self.phone) \
            + ', email = ' + str(self.email) \
            + ', www = ' + str(self.www) \
            + ']'
