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

from nip24 import *

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
    print(account)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Sprawdzenie statusu fimy
active = nip24.isActiveExt(Number.NIP, nip)

if active:
    print('Firma prowadzi aktywną działalność')
else:
    if not nip24.getLastError():
        print('Firma zawiesiła lub zakończyła działalność')
    else:
        print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Sprawdzenie statusu firmy w rejestrze VAT
vat = nip24.getVATStatusExt(Number.NIP, nip)

if vat:
    print(vat)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Wywołanie metody zwracającej dane do faktury
invoice = nip24.getInvoiceDataExt(Number.NIP, nip)

if invoice:
    print(invoice)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Wywołanie metody zwracającej szczegółowe dane firmy
all = nip24.getAllDataExt(Number.NIP, nip)

if all:
    print(all)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Wywołanie metody zwracającej dane z systemu VIES
vies = nip24.getVIESData(nip_eu)

if vies:
    print(vies)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Wywołanie metody zwracającej informacje o rachunku bankowym
iban = nip24.getIBANStatusExt(Number.NIP, nip, account_number)

if iban:
    print(iban)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Wywołanie metody sprawdzającej status podmiotu na białej liście podatników VAT
whitelist = nip24.getWhitelistStatusExt(Number.NIP, nip, account_number)

if whitelist:
    print(whitelist)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')

# Wywołanie metody wyszukującej dane w rejestrze VAT
result = nip24.searchVATRegistryExt(Number.NIP, nip)

if result:
    print(result)
else:
    print('Błąd: ' + nip24.getLastError() + ' (kod: ' + str(nip24.getLastErrorCode()) + ')')
