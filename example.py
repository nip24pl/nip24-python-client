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

from nip24 import *
from pprint import pprint

# Utworzenie obiektu klienta usługi serwisu produkcyjnego
# id – ciąg znaków reprezentujący identyfikator klucza
# key – ciąg znaków reprezentujący klucz
# nip24 = NIP24Client('id', 'key')

# Utworzenie obiektu klienta usługi serwisu testowego
nip24 = NIP24Client()

nip = '7171642051'
nip_eu = 'PL' + nip
account_number = '49154000046458439719826658'

# Sprawdzenie stanu konta
account = nip24.getAccountStatus()

if account:
    pprint(vars(account))
else:
    print u'Błąd: ' + nip24.getLastError()

# Sprawdzenie statusu fimy
active = nip24.isActiveExt(Number.NIP, nip)

if active:
    print u'Firma prowadzi aktywną działalność'
else:
    if not nip24.getLastError():
        print u'Firma zawiesiła lub zakończyła działalność'
    else:
        print u'Błąd: ' + nip24.getLastError()

# Sprawdzenie statusu firmy w rejestrze VAT
vat = nip24.getVATStatusExt(Number.NIP, nip, True)

if vat:
    print u'NIP: ' + vat.nip
    print u'REGON: ' + vat.regon
    print u'Nazwa firmy: ' + vat.name
    print u'Status: ' + str(vat.status)
    print u'Wynik: ' + vat.result
    print u'Data sprawdzenia: ' + vat.date.strftime('%Y-%m-%d')
    print u'Źródło: ' + vat.source
else:
    print u'Błąd: ' + nip24.getLastError()

# Wywołanie metody zwracającej dane do faktury
invoice = nip24.getInvoiceDataExt(Number.NIP, nip, False)

if invoice:
    print u'Nazwa: ' + invoice.name
    print u'Imię i nazwisko: ' + invoice.firstname + ' ' + invoice.lastname
    print u'Adres: ' + invoice.postCode + ' ' + invoice.postCity + ' ' + invoice.street \
        + ' ' + invoice.streetNumber
    print u'NIP: ' + invoice.nip
else:
    print u'Błąd: ' + nip24.getLastError()

# Wywołanie metody zwracającej szczegółowe dane firmy
all = nip24.getAllDataExt(Number.NIP, nip, False)

if all:
    pprint(vars(all))
else:
    print u'Błąd: ' + nip24.getLastError()

# Wywołanie metody zwracającej dane z systemu VIES
vies = nip24.getVIESData(nip_eu)

if vies:
    pprint(vars(vies))
else:
    print u'Błąd: ' + nip24.getLastError()

# Wywołanie metody zwracającej informacje o rachunku bankowym
iban = nip24.getIBANStatusExt(Number.NIP, nip, account_number)

if iban:
    pprint(vars(iban))
else:
    print u'Błąd: ' + nip24.getLastError()
