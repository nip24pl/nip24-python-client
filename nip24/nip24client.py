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

import base64
import datetime
import hashlib
import hmac
import os
import sys
import time
import urllib2
import urlparse

from nip24 import Number, NIP, REGON, KRS, EUVAT, PKD, IBAN, AllData, InvoiceData, VIESData, VATStatus, IBANStatus, AccountStatus
from io import BytesIO
from lxml import etree
from dateutil.parser import parse

class NIP24Client:
    """
    NIP24 service client
    """

    VERSION = '1.3.3'

    PRODUCTION_URL = 'https://www.nip24.pl/api'
    TEST_URL = 'https://www.nip24.pl/api-test'

    TEST_ID = 'test_id'
    TEST_KEY = 'test_key'

    HMAC_ALG = hashlib.sha256

    def __init__(self, id = None, key = None):
        """
        Construct new service client object

        :param id: NIP24 key identifier
        :type id: str
        :param key: NIP24 key
        :type key: str
        """
        self.__url__ = self.TEST_URL
        self.__id__ = self.TEST_ID
        self.__key__ = self.TEST_KEY

        if id is not None and key is not None:
            self.__url__ = self.PRODUCTION_URL
            self.__id__ = id
            self.__key__ = key

        self.__err__ = u''

    def setURL(self, url):
        """
        Set non default service URL

        :param url: service URL
        :type url: str
        """

        self.__url__ = url

    def isActive(self, nip_):
        """
        Check firm activity

        :param nip_: NIP number
        :type nip_: str
        :returns: True is firm is active
        :rtype: bool
        """

        return self.isActiveExt(Number.NIP, nip_)

    def isActiveExt(self, type, number):
        """
        Check firm activity

        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :returns: True is firm is active
        :rtype: bool
        """

        # clear error
        self.__err__ = u''

        # validate number and construct path
        suffix = self.__getPathSuffix(type, number)

        if not suffix:
            return False

        # prepare url
        url = self.__url__ + '/check/firm/' + suffix

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            if int(err) == 9:
                # not active
                self.__err__ = u''
                return False
            else:
                self.__err__ = self.__get_text(doc, '/result/error/description/text()')
                return False

        # ok
        return True

    def getInvoiceData(self, nip, force=True):
        """
        Get invoice data for specified NIP number

        :param nip: NIP number
        :type nip: str
        :param force: ignored, left for backward compatibility
        :type force: bool
        :return: InvoiceData object or False
        :rtype: InvoiceData or False
        """

        return self.getInvoiceDataExt(Number.NIP, nip)

    def getInvoiceDataExt(self, type, number, force=True):
        """
        Get invoice data for specified number type

        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :param force: ignored, left for backward compatibility
        :type force: bool
        :return: InvoiceData object or False
        :rtype: InvoiceData or False
        """

        # clear error
        self.__err__ = u''

        # validate number and construct path
        suffix = self.__getPathSuffix(type, number)

        if not suffix:
            return False

        # prepare url
        url = self.__url__ + '/get/invoice/' + suffix

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            self.__err__ = self.__get_text(doc, '/result/error/description/text()')
            return False

        invoice = InvoiceData()

        invoice.uid = self.__get_text(doc, '/result/firm/uid/text()')

        invoice.nip = self.__get_text(doc, '/result/firm/nip/text()')

        invoice.name = self.__get_text(doc, '/result/firm/name/text()')
        invoice.firstname = self.__get_text(doc, '/result/firm/firstname/text()')
        invoice.lastname = self.__get_text(doc, '/result/firm/lastname/text()')

        invoice.street = self.__get_text(doc, '/result/firm/street/text()')
        invoice.streetNumber = self.__get_text(doc, '/result/firm/streetNumber/text()')
        invoice.houseNumber = self.__get_text(doc, '/result/firm/houseNumber/text()')
        invoice.city = self.__get_text(doc, '/result/firm/city/text()')
        invoice.postCode = self.__get_text(doc, '/result/firm/postCode/text()')
        invoice.postCity = self.__get_text(doc, '/result/firm/postCity/text()')

        invoice.phone = self.__get_text(doc, '/result/firm/phone/text()')
        invoice.email = self.__get_text(doc, '/result/firm/email/text()')
        invoice.www = self.__get_text(doc, '/result/firm/www/text()')

        return invoice

    def getAllData(self, nip, force=True):
        """
        Get all firm data for specified NIP number

        :param nip: NIP number
        :type nip: str
        :param force: ignored, left for backward compatibility
        :type force: bool
        :return: AllData object or False
        :rtype: AllData or False
        """

        return self.getAllDataExt(Number.NIP, nip)

    def getAllDataExt(self, type, number, force=True):
        """
        Get all data for specified number type

        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :param force: ignored, left for backward compatibility
        :type force: bool
        :return: AllData object or False
        :rtype: AllData or False
        """

        # clear error
        self.__err__ = u''

        # validate number and construct path
        suffix = self.__getPathSuffix(type, number)

        if not suffix:
            return False

        # prepare url
        url = self.__url__ + '/get/all/' + suffix

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            self.__err__ = self.__get_text(doc, '/result/error/description/text()')
            return False

        all = AllData()

        all.uid = self.__get_text(doc, '/result/firm/uid/text()')

        all.type = self.__get_text(doc, '/result/firm/type/text()')
        all.nip = self.__get_text(doc, '/result/firm/nip/text()')
        all.regon = self.__get_text(doc, '/result/firm/regon/text()')

        all.name = self.__get_text(doc, '/result/firm/name/text()')
        all.shortname = self.__get_text(doc, '/result/firm/shortname/text()')
        all.firstname = self.__get_text(doc, '/result/firm/firstname/text()')
        all.secondname = self.__get_text(doc, '/result/firm/secondname/text()')
        all.lastname = self.__get_text(doc, '/result/firm/lastname/text()')

        all.street = self.__get_text(doc, '/result/firm/street/text()')
        all.streetCode = self.__get_text(doc, '/result/firm/streetCode/text()')
        all.streetNumber = self.__get_text(doc, '/result/firm/streetNumber/text()')
        all.houseNumber = self.__get_text(doc, '/result/firm/houseNumber/text()')
        all.city = self.__get_text(doc, '/result/firm/city/text()')
        all.cityCode = self.__get_text(doc, '/result/firm/cityCode/text()')
        all.community = self.__get_text(doc, '/result/firm/community/text()')
        all.communityCode = self.__get_text(doc, '/result/firm/communityCode/text()')
        all.county = self.__get_text(doc, '/result/firm/county/text()')
        all.countyCode = self.__get_text(doc, '/result/firm/countyCode/text()')
        all.state = self.__get_text(doc, '/result/firm/state/text()')
        all.stateCode = self.__get_text(doc, '/result/firm/stateCode/text()')
        all.postCode = self.__get_text(doc, '/result/firm/postCode/text()')
        all.postCity = self.__get_text(doc, '/result/firm/postCity/text()')

        all.phone = self.__get_text(doc, '/result/firm/phone/text()')
        all.email = self.__get_text(doc, '/result/firm/email/text()')
        all.www = self.__get_text(doc, '/result/firm/www/text()')

        all.creationDate = self.__get_date_time(doc, '/result/firm/creationDate/text()')
        all.startDate = self.__get_date_time(doc, '/result/firm/startDate/text()')
        all.registrationDate = self.__get_date_time(doc, '/result/firm/registrationDate/text()')
        all.holdDate = self.__get_date_time(doc, '/result/firm/holdDate/text()')
        all.renevalDate = self.__get_date_time(doc, '/result/firm/renevalDate/text()')
        all.lastUpdateDate = self.__get_date_time(doc, '/result/firm/lastUpdateDate/text()')
        all.endDate = self.__get_date_time(doc, '/result/firm/endDate/text()')

        all.registryEntityCode = self.__get_text(doc, '/result/firm/registryEntity/code/text()')
        all.registryEntityName = self.__get_text(doc, '/result/firm/registryEntity/name/text()')

        all.registryCode = self.__get_text(doc, '/result/firm/registry/code/text()')
        all.registryName = self.__get_text(doc, '/result/firm/registry/name/text()')

        all.recordCreationDate = self.__get_date_time(doc, '/result/firm/record/created/text()')
        all.recordNumber = self.__get_text(doc, '/result/firm/record/number/text()')

        all.basicLegalFormCode = self.__get_text(doc, '/result/firm/basicLegalForm/code/text()')
        all.basicLegalFormName = self.__get_text(doc, '/result/firm/basicLegalForm/name/text()')

        all.specificLegalFormCode = self.__get_text(doc, '/result/firm/specificLegalForm/code/text()')
        all.specificLegalFormName = self.__get_text(doc, '/result/firm/specificLegalForm/name/text()')

        all.ownershipFormCode = self.__get_text(doc, '/result/firm/ownershipForm/code/text()')
        all.ownershipFormName = self.__get_text(doc, '/result/firm/ownershipForm/name/text()')

        all.pkd = []

        i = 1
        while True:
            code = self.__get_text(doc, '/result/firm/PKDs/PKD[' + str(i) + ']/code/text()')

            if len(code) == 0:
                break

            descr = self.__get_text(doc, '/result/firm/PKDs/PKD[' + str(i) + ']/description/text()')
            pri = self.__get_text(doc, '/result/firm/PKDs/PKD[' + str(i) + ']/primary/text()')

            pkd = PKD()

            pkd.code = code
            pkd.description = descr
            pkd.primary = True if pri == "true" else False

            all.pkd.append(pkd)
            i += 1

        return all

    def getVIESData(self, euvat):
        """
        Get VIES data for specified number

        :param euvat: EU VAT number with 2-letter country prefix
        :type euvat: str
        :return: VIESData object or False
        :rtype: VIESData or False
        """

        # clear error
        self.__err__ = u''

        # validate number and construct path
        suffix = self.__getPathSuffix(Number.EUVAT, euvat)

        if not suffix:
            return False

        # prepare url
        url = self.__url__ + '/get/vies/' + suffix

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            self.__err__ = self.__get_text(doc, '/result/error/description/text()')
            return False

        vies = VIESData()

        vies.uid = self.__get_text(doc, '/result/vies/uid/text()')

        vies.countryCode = self.__get_text(doc, '/result/vies/countryCode/text()')
        vies.vatNumber = self.__get_text(doc, '/result/vies/vatNumber/text()')

        vies.valid = True if self.__get_text(doc, '/result/vies/valid/text()') == 'true' else False

        vies.traderName = self.__get_text(doc, '/result/vies/traderName/text()')
        vies.traderCompanyType = self.__get_text(doc, '/result/vies/traderCompanyType/text()')
        vies.traderAddress = self.__get_text(doc, '/result/vies/traderAddress/text()')

        vies.id = self.__get_text(doc, '/result/vies/id/text()')
        vies.date = self.__get_date(doc, '/result/vies/date/text()')
        vies.source = self.__get_text(doc, '/result/vies/source/text()')

        return vies

    def getVATStatus(self, nip, direct=True):
        """
        Check if frim is an active VAT payer

        :param nip: NIP number
        :type nip: str
        :param direct: ignored, left for backward compatibility
        :type direct: bool
        :return: VATStatus object or False
        :rtype: VATStatus or False
        """

        return self.getVATStatusExt(Number.NIP, nip)

    def getVATStatusExt(self, type, number, direct=True):
        """
        Check if firm is an active VAT payer

        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :param direct: ignored, left for backward compatibility
        :type direct: bool
        :return: VATStatus object or False
        :rtype: VATStatus or False
        """

        # clear error
        self.__err__ = u''

        # validate number and construct path
        suffix = self.__getPathSuffix(type, number)

        if not suffix:
            return False

        # prepare url
        url = self.__url__ + '/check/vat/direct/' + suffix

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            self.__err__ = self.__get_text(doc, '/result/error/description/text()')
            return False

        vat = VATStatus()

        vat.uid = self.__get_text(doc, '/result/vat/uid/text()')

        vat.nip = self.__get_text(doc, '/result/vat/nip/text()')
        vat.regon = self.__get_text(doc, '/result/vat/regon/text()')
        vat.name = self.__get_text(doc, '/result/vat/name/text()')

        vat.status = int(self.__get_text(doc, '/result/vat/status/text()'))
        vat.result = self.__get_text(doc, '/result/vat/result/text()')

        vat.date = self.__get_date(doc, '/result/vat/date/text()')
        vat.source = self.__get_text(doc, '/result/vat/source/text()')

        return vat

    def getIBANStatus(self, nip, iban, date=None):
        """
        Check if firm owns bank account number

        :param nip: NIP number
        :type nip: str
        :param iban: bank account IBAN (for polish numbers PL prefix may be omitted)
        :type iban: str
        :param date: date in format 'yyyy-mm-dd' (null - current day)
        :type date: str
        :return: IBANStatus object or False
        :rtype: IBANStatus or False
        """

        return self.getIBANStatusExt(Number.NIP, nip, iban, date)

    def getIBANStatusExt(self, type, number, iban, date=None):
        """
        Check if firm owns bank account number

        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :param iban: bank account IBAN (for polish numbers PL prefix may be omitted)
        :type iban: str
        :param date: date in format 'yyyy-mm-dd' (None - current day)
        :type date: str
        :return: IBANStatus object or False
        :rtype: IBANStatus or False
        """

        # clear error
        self.__err__ = u''

        # validate number and construct path
        suffix = self.__getPathSuffix(type, number)

        if not suffix:
            return False

        if not IBAN.isValid(iban):
            iban = 'PL' + iban

            if not IBAN.isValid(iban):
                self.__err__ = u'Numer IBAN jest nieprawidłowy'
                return False

        if not date:
            date = datetime.date.today().strftime('%Y-%m-%d')

        # prepare url
        url = self.__url__ + '/check/iban/' + suffix + '/' + IBAN.normalize(iban) + '/' + parse(date).strftime('%Y-%m-%d')

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            self.__err__ = self.__get_text(doc, '/result/error/description/text()')
            return False

        ibs = IBANStatus()

        ibs.uid = self.__get_text(doc, '/result/iban/uid/text()')

        ibs.nip = self.__get_text(doc, '/result/iban/nip/text()')
        ibs.regon = self.__get_text(doc, '/result/iban/regon/text()')
        ibs.iban = self.__get_text(doc, '/result/iban/iban/text()')

        ibs.valid = True if self.__get_text(doc, '/result/iban/valid/text()') == 'true' else False

        ibs.id = self.__get_text(doc, '/result/iban/id/text()')
        ibs.date = self.__get_date(doc, '/result/iban/date/text()')
        ibs.source = self.__get_text(doc, '/result/iban/source/text()')

        return ibs

    def getAccountStatus(self):
        """
        Get user account's status

        :return: AccountStatus object or False
        :rtype: AccountStatus or False
        """

        # clear error
        self.__err__ = u''

        # prepare url
        url = self.__url__ + '/check/account/status'

        # send request
        res = self.__get(url)

        if not res:
            self.__err__ = u'Nie udało się nawiązać połączenia z serwisem NIP24'
            return False

        # parse response
        doc = etree.parse(BytesIO(res))

        if not doc:
            self.__err__ = u'Odpowiedź serwisu NIP24 ma nieprawidłowy format'
            return False

        err = self.__get_text(doc, '/result/error/code/text()')

        if len(err) > 0:
            self.__err__ = self.__get_text(doc, '/result/error/description/text()')
            return False

        status = AccountStatus()

        status.uid = self.__get_text(doc, '/result/vat/uid/text()')
        status.billingPlanName = self.__get_text(doc, '/result/account/billingPlan/name/text()')
        
        status.subscriptionPrice = float('0' + self.__get_text(doc, '/result/account/billingPlan/subscriptionPrice/text()'))
        status.itemPrice = float('0' + self.__get_text(doc, '/result/account/billingPlan/itemPrice/text()'))
        status.itemPriceStatus = float('0' + self.__get_text(doc, '/result/account/billingPlan/itemPriceCheckStatus/text()'))
        status.itemPriceInvoice = float('0' + self.__get_text(doc, '/result/account/billingPlan/itemPriceInvoiceData/text()'))
        status.itemPriceAll = float('0' + self.__get_text(doc, '/result/account/billingPlan/itemPriceAllData/text()'))
        status.itemPriceIBAN = float('0' + self.__get_text(doc, '/result/account/billingPlan/itemPriceIBANStatus/text()'))
        
        status.limit = int(self.__get_text(doc, '/result/account/billingPlan/limit/text()'))
        status.requestDelay = int(self.__get_text(doc, '/result/account/billingPlan/requestDelay/text()'))
        status.domainLimit = int(self.__get_text(doc, '/result/account/billingPlan/domainLimit/text()'))

        status.overPlanAllowed = True if self.__get_text(doc, '/result/account/billingPlan/overplanAllowed/text()') == 'true' else False
        status.terytCodes = True if self.__get_text(doc, '/result/account/billingPlan/terytCodes/text()') == 'true' else False
        status.excelAddIn = True if self.__get_text(doc, '/result/account/billingPlan/excelAddin/text()') == 'true' else False
        status.JPKVAT = True if self.__get_text(doc, '/result/account/billingPlan/jpkVat/text()') == 'true' else False
        status.stats = True if self.__get_text(doc, '/result/account/billingPlan/stats/text()') == 'true' else False
        status.nipMonitor = True if self.__get_text(doc, '/result/account/billingPlan/nipMonitor/text()') == 'true' else False
        
        status.searchByNIP = True if self.__get_text(doc, '/result/account/billingPlan/searchByNip/text()') == 'true' else False
        status.searchByREGON = True if self.__get_text(doc, '/result/account/billingPlan/searchByRegon/text()') == 'true' else False
        status.searchByKRS = True if self.__get_text(doc, '/result/account/billingPlan/searchByKrs/text()') == 'true' else False
        
        status.funcIsActive = True if self.__get_text(doc, '/result/account/billingPlan/funcIsActive/text()') == 'true' else False
        status.funcGetInvoiceData = True if self.__get_text(doc, '/result/account/billingPlan/funcGetInvoiceData/text()') == 'true' else False
        status.funcGetAllData = True if self.__get_text(doc, '/result/account/billingPlan/funcGetAllData/text()') == 'true' else False
        status.funcGetVIESData = True if self.__get_text(doc, '/result/account/billingPlan/funcGetVIESData/text()') == 'true' else False
        status.funcGetVATStatus = True if self.__get_text(doc, '/result/account/billingPlan/funcGetVATStatus/text()') == 'true' else False
        status.funcGetIBANStatus = True if self.__get_text(doc, '/result/account/billingPlan/funcGetIBANStatus/text()') == 'true' else False
        
        status.invoiceDataCount = int(self.__get_text(doc, '/result/account/requests/invoiceData/text()'))
        status.allDataCount = int(self.__get_text(doc, '/result/account/requests/allData/text()'))
        status.firmStatusCount = int(self.__get_text(doc, '/result/account/requests/firmStatus/text()'))
        status.vatStatusCount = int(self.__get_text(doc, '/result/account/requests/vatStatus/text()'))
        status.viesStatusCount = int(self.__get_text(doc, '/result/account/requests/viesStatus/text()'))
        status.ibanStatusCount = int(self.__get_text(doc, '/result/account/requests/ibanStatus/text()'))
        status.totalCount = int(self.__get_text(doc, '/result/account/requests/total/text()'))

        return status

    def getLastError(self):
        """
        Get last error message

        :return: unicode string
        :rtype: str
        """

        return self.__err__

    def __auth(self, method, url):
        """
        Prepare authorization header content

        :param method: HTTP method
        :type method: str
        :param url: target URL
        :type url: str
        :returns: authorization header content or False
        :rtype: str or False
        """

        # parse url
        u = urlparse.urlparse(url)
        ls = u.netloc.split(':')

        host = ls[0]
        port = 443 if u.scheme == 'https' else 80

        if len(ls) > 1:
            port = ls[1]

        # prepare auth header value
        nonce = os.urandom(4).encode('hex')
        ts = int(time.time())

        s = '' + str(ts) + '\n' \
            + nonce + '\n' \
            + method + '\n' \
            + u.path + '\n' \
            + host + '\n' \
            + str(port) + '\n' \
            + '\n'

        mac = base64.b64encode(hmac.new(self.__key__, s, self.HMAC_ALG).digest())

        return 'MAC id="' + self.__id__ + '", ts="' + str(ts) + '", nonce="' +  nonce + '", mac="' + mac + '"'

    def __user_agent(self):
        """
        Prepare user agent information header content

        :return: user agent header content
        :rtype: str
        """

        return 'NIP24Client/' + self.VERSION + ' Python/' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) \
            + '.' + str(sys.version_info[2])

    def __get(self, url):
        """
        Get result of HTTP GET request

        :param url: target URL
        :type url: str
        :returns: result content or False
        :rtype: str or False
        """

        # auth
        auth = self.__auth('GET', url)

        if not auth:
            return False

        # send request
        try :
            req = urllib2.Request(url)
            req.add_header('User-Agent', self.__user_agent())
            req.add_header('Authorization', auth)

            res = urllib2.urlopen(req)
            content = res.read()
        except urllib2.URLError, ue:
            #print ue.code
            return False

        return content

    def __get_text(self, doc, xpath_):
        """
        Get XML element as text

        :param doc: etree document
        :type doc: tree
        :param xpath_: xpath string
        :type xpath_: string
        :return: string
        :rtype: str
        """

        s = doc.xpath(xpath_)

        if not s:
            return u''

        if len(s) != 1:
            return u''

        return unicode(s[0].strip())

    def __get_date_time(self, doc, xpath_):
        """
        Get XML element as date time object

        :param doc: etree document
        :type doc: tree
        :param xpath_: xpath string
        :type xpath_: string
        :return: datetime
        :rtype: datetime or None
        """

        s = self.__get_text(doc, xpath_)

        if len(s) == 0:
            return None

        return parse(s)

    def __get_date(self, doc, xpath_):
        """
        Get XML element as date object

        :param doc: etree document
        :type doc: tree
        :param xpath_: xpath string
        :type xpath_: string
        :return: datetime
        :rtype: datetime or None
        """

        s = self.__get_text(doc, xpath_)

        sl = len(s)

        if sl == 0:
            return None
        elif sl == 11:
            # dateutil does not support xsd:date type in form YYYY-MM-DDZ
            s = s[0:10] + 'T00:00:00Z'
        elif sl == 16:
            # dateutil does not support xsd:date type in form YYYY-MM-DD+00:00
            s = s[0:10] + 'T00:00:00' + s[10:]

        return parse(s)

    def __getPathSuffix(self, type, number):
        """
        Get path suffix

        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :return: path suffix
        :rtype: string or False
        """

        if type == Number.NIP:
            if not NIP.isValid(number):
                self.__err__ = u'Numer NIP jest nieprawidłowy'
                return False

            path = 'nip/' + NIP.normalize(number)
        elif type == Number.REGON:
            if not REGON.isValid(number):
                self.__err__ = u'Numer REGON jest nieprawidłowy'
                return False

            path = 'regon/' + REGON.normalize(number)
        elif type == Number.KRS:
            if not KRS.isValid(number):
                self.__err__ = u'Numer KRS jest nieprawidłowy'
                return False

            path = 'krs/' + KRS.normalize(number)
        elif type == Number.EUVAT:
            if not EUVAT.isValid(number):
                self.__err__ = u'Numer EU VAT ID jest nieprawidłowy'
                return False

            path = 'euvat/' + EUVAT.normalize(number)
        else:
            self.__err__ = u'Nieprawidłowy typ numeru'
            return False

        return path