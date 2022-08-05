#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2022 NETCAT (www.netcat.pl)
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
# @copyright 2015-2022 NETCAT (www.netcat.pl)
# @license http://www.apache.org/licenses/LICENSE-2.0
#


class AllData:
    """
    All firm data
    """

    def __init__(self):
        self.uid = None
        self.type = None
        self.nip = None
        self.regon = None
        self.name = None
        self.shortname = None
        self.firstname = None
        self.secondname = None
        self.lastname = None
        self.street = None
        self.streetCode = None
        self.streetNumber = None
        self.houseNumber = None
        self.city = None
        self.cityCode = None
        self.community = None
        self.communityCode = None
        self.county = None
        self.countyCode = None
        self.state = None
        self.stateCode = None
        self.postCode = None
        self.postCity = None
        self.phone = None
        self.email = None
        self.www = None
        self.creationDate = None
        self.startDate = None
        self.registrationDate = None
        self.holdDate = None
        self.renevalDate = None
        self.lastUpdateDate = None
        self.endDate = None
        self.registryEntityCode = None
        self.registryEntityName = None
        self.registryCode = None
        self.registryName = None
        self.recordCreationDate = None
        self.recordNumber = None
        self.basicLegalFormCode = None
        self.basicLegalFormName = None
        self.specificLegalFormCode = None
        self.specificLegalFormName = None
        self.ownershipFormCode = None
        self.ownershipFormName = None
        self.pkd = []

    def __str__(self):
        return 'AllData: [uid = ' + str(self.uid) \
            + ', nip = ' + str(self.nip) \
            + ', regon = ' + str(self.regon) \
            + ', type = ' + str(self.type) \
            + ', name = ' + str(self.name) \
            + ', shortName = ' + str(self.shortname) \
            + ', firstName = ' + str(self.firstname) \
            + ', secondName = ' + str(self.secondname) \
            + ', lastName = ' + str(self.lastname) \
            + ', street = ' + str(self.street) \
            + ', streetCode = ' + str(self.streetCode) \
            + ', streetNumber = ' + str(self.streetNumber) \
            + ', houseNumber = ' + str(self.houseNumber) \
            + ', city = ' + str(self.city) \
            + ', cityCode = ' + str(self.cityCode) \
            + ', community = ' + str(self.community) \
            + ', communityCode = ' + str(self.communityCode) \
            + ', county = ' + str(self.county) \
            + ', countyCode = ' + str(self.countyCode) \
            + ', state = ' + str(self.state) \
            + ', stateCode = ' + str(self.stateCode) \
            + ', postCode = ' + str(self.postCode) \
            + ', postCity = ' + str(self.postCity) \
            + ', phone = ' + str(self.phone) \
            + ', email = ' + str(self.email) \
            + ', www = ' + str(self.www) \
            + ', creationDate = ' + str(self.creationDate) \
            + ', startDate = ' + str(self.startDate) \
            + ', registrationDate = ' + str(self.registrationDate) \
            + ', holdDate = ' + str(self.holdDate) \
            + ', renevalDate = ' + str(self.renevalDate) \
            + ', lastUpdateDate = ' + str(self.lastUpdateDate) \
            + ', endDate = ' + str(self.endDate) \
            + ', registryEntityCode = ' + str(self.registryEntityCode) \
            + ', registryEntityName = ' + str(self.registryEntityName) \
            + ', registryCode = ' + str(self.registryCode) \
            + ', registryName = ' + str(self.registryName) \
            + ', recordCreationDate = ' + str(self.recordCreationDate) \
            + ', recordNumber = ' + str(self.recordNumber) \
            + ', basicLegalFormCode = ' + str(self.basicLegalFormCode) \
            + ', basicLegalFormName = ' + str(self.basicLegalFormName) \
            + ', specificLegalFormCode = ' + str(self.specificLegalFormCode) \
            + ', specificLegalFormName = ' + str(self.specificLegalFormName) \
            + ', ownershipFormCode = ' + str(self.ownershipFormCode) \
            + ', ownershipFormName = ' + str(self.ownershipFormName) \
            + ', pkd = [' + ', '.join(str(e) for e in self.pkd) + ']' \
            + ']'
