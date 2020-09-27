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


class AccountStatus:
    """
    Account status
    """

    def __init__(self):
        self.uid = None

        self.type = None
        self.validTo = None
        self.billingPlanName = None

        self.subscriptionPrice = None
        self.itemPrice = None
        self.itemPriceStatus = None
        self.itemPriceInvoice = None
        self.itemPriceAll = None
        self.itemPriceIBAN = None
        self.itemPriceWhitelist = None
        self.itemPriceSearchVAT = None

        self.limit = None
        self.requestDelay = None
        self.domainLimit = None

        self.overPlanAllowed = None
        self.terytCodes = None
        self.excelAddIn = None
        self.JPKVAT = None
        self.CLI = None
        self.stats = None
        self.nipMonitor = None

        self.searchByNIP = None
        self.searchByREGON = None
        self.searchByKRS = None

        self.funcIsActive = None
        self.funcGetInvoiceData = None
        self.funcGetAllData = None
        self.funcGetVIESData = None
        self.funcGetVATStatus = None
        self.funcGetIBANStatus = None
        self.funcGetWhitelistStatus = None
        self.funcSearchVAT = None

        self.invoiceDataCount = None
        self.allDataCount = None
        self.firmStatusCount = None
        self.vatStatusCount = None
        self.viesStatusCount = None
        self.ibanStatusCount = None
        self.whitelistStatusCount = None
        self.searchVATCount = None
        self.totalCount = None

    def __str__(self):
        return 'AccountStatus: [uid = ' + str(self.uid) \
            + ', type = ' + str(self.type) \
            + ', validTo = ' + str(self.validTo) \
            + ', billingPlanName = ' + str(self.billingPlanName) \
            + ', subscriptionPrice = ' + str(self.subscriptionPrice) \
            + ', itemPrice = ' + str(self.itemPrice) \
            + ', itemPriceStatus = ' + str(self.itemPriceStatus) \
            + ', itemPriceInvoice = ' + str(self.itemPriceInvoice) \
            + ', itemPriceAll = ' + str(self.itemPriceAll) \
            + ', itemPriceIBAN = ' + str(self.itemPriceIBAN) \
            + ', itemPriceWhitelist = ' + str(self.itemPriceWhitelist) \
            + ', itemPriceSearchVAT = ' + str(self.itemPriceSearchVAT) \
            + ', limit = ' + str(self.limit) \
            + ', requestDelay = ' + str(self.requestDelay) \
            + ', domainLimit = ' + str(self.domainLimit) \
            + ', overPlanAllowed = ' + str(self.overPlanAllowed) \
            + ', terytCodes = ' + str(self.terytCodes) \
            + ', excelAddIn = ' + str(self.excelAddIn) \
            + ', jpkVat = ' + str(self.JPKVAT) \
            + ', cli = ' + str(self.CLI) \
            + ', stats = ' + str(self.stats) \
            + ', NIPMonitor = ' + str(self.nipMonitor) \
            + ', searchByNIP = ' + str(self.searchByNIP) \
            + ', searchByREGON = ' + str(self.searchByREGON) \
            + ', searchByKRS = ' + str(self.searchByKRS) \
            + ', funcIsActive = ' + str(self.funcIsActive) \
            + ', funcGetInvoiceData = ' + str(self.funcGetInvoiceData) \
            + ', funcGetAllData = ' + str(self.funcGetAllData) \
            + ', funcGetVIESData = ' + str(self.funcGetVIESData) \
            + ', funcGetVATStatus = ' + str(self.funcGetVATStatus) \
            + ', funcGetIBANStatus = ' + str(self.funcGetIBANStatus) \
            + ', funcGetWhitelistStatus = ' + str(self.funcGetWhitelistStatus) \
            + ', funcSearchVAT = ' + str(self.funcSearchVAT) \
            + ', invoiceDataCount = ' + str(self.invoiceDataCount) \
            + ', allDataCount = ' + str(self.allDataCount) \
            + ', firmStatusCount = ' + str(self.firmStatusCount) \
            + ', VATStatusCount = ' + str(self.vatStatusCount) \
            + ', VIESStatusCount = ' + str(self.viesStatusCount) \
            + ', IBANStatusCount = ' + str(self.ibanStatusCount) \
            + ', whitelistStatusCount = ' + str(self.whitelistStatusCount) \
            + ', searchVATCount = ' + str(self.searchVATCount) \
            + ', totalCount = ' + str(self.totalCount) \
            + ']'
