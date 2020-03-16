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


class VATEntity:
    """
    VAT registry entity
    """

    def __init__(self):
        self.name = None
        self.nip = None
        self.regon = None
        self.krs = None

        self.residenceAddress = None
        self.workingAddress = None

        self.vatStatus = None
        self.vatResult = None

        self.representatives = []
        self.authorizedClerks = []
        self.partners = []

        self.ibans = []
        self.hasVirtualAccounts = None

        self.registrationLegalDate = None
        self.registrationDenialDate = None
        self.registrationDenialBasis = None
        self.restorationDate = None
        self.restorationBasis = None
        self.removalDate = None
        self.removalBasis = None

    def __str__(self):
        return 'VATEntity: [name = ' + str(self.name) \
            + ', nip = ' + str(self.nip) \
            + ', regon = ' + str(self.regon) \
            + ', krs = ' + str(self.krs) \
            + ', residenceAddress = ' + str(self.residenceAddress) \
            + ', workingAddress = ' + str(self.workingAddress) \
            + ', vatStatus = ' + str(self.vatStatus) \
            + ', vatResult = ' + str(self.vatResult) \
            + ', representatives = [' + ', '.join(str(e) for e in self.representatives) + ']' \
            + ', authorizedClerks = [' + ', '.join(str(e) for e in self.authorizedClerks) + ']' \
            + ', partners = [' + ', '.join(str(e) for e in self.partners) + ']' \
            + ', ibans = [' + ', '.join(str(e) for e in self.ibans) + ']' \
            + ', hasVirtualAccounts = ' + str(self.hasVirtualAccounts) \
            + ', registrationLegalDate = ' + str(self.registrationLegalDate) \
            + ', registrationDenialDate = ' + str(self.registrationDenialDate) \
            + ', registrationDenialBasis = ' + str(self.registrationDenialBasis) \
            + ', restorationDate = ' + str(self.restorationDate) \
            + ', restorationBasis = ' + str(self.restorationBasis) \
            + ', removalDate = ' + str(self.removalDate) \
            + ', removalBasis = ' + str(self.removalBasis) \
            + ']'
