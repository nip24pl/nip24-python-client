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


class VATPerson:
    """
    VAT registry person
    """

    def __init__(self):
        self.companyName = None
        self.firstName = None
        self.lastName = None
        self.nip = None

    def __str__(self):
        return 'VATPerson: [companyName = ' + str(self.companyName) \
            + ', firstName = ' + str(self.firstName) \
            + ', lastName = ' + str(self.lastName) \
            + ', nip = ' + str(self.nip) \
            + ']'
