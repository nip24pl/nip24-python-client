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


class AccountStatus:
    """
    Account status
    """

    def __init__(self):
        self.uid = None
        self.billingPlanName = None
        self.subscriptionPrice = None
        self.itemPrice = None
        self.itemPriceStatus = None
        self.itemPriceInvoice = None
        self.itemPriceAll = None
        self.itemPriceIBAN = None
        self.limit = None
        self.requestDelay = None
        self.domainLimit = None
        self.overPlanAllowed = None
        self.terytCodes = None
        self.excelAddIn = None
        self.JPKVAT = None
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
        self.invoiceDataCount = None
        self.allDataCount = None
        self.firmStatusCount = None
        self.vatStatusCount = None
        self.viesStatusCount = None
        self.ibanStatusCount = None
        self.totalCount = None
