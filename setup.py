#
# -*- coding: utf-8 -*-
#
# Copyright 2015-2024 NETCAT (www.netcat.pl)
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
# @copyright 2015-2024 NETCAT (www.netcat.pl)
# @license http://www.apache.org/licenses/LICENSE-2.0
#

from setuptools import setup

setup(name='nip24',
      version='1.4.1',
      description='NIP24 Service Client',
      url='https://www.nip24.pl',
      author='nip24.pl',
      author_email='kontakt@nip24.pl',
      license='nip24.pl',
      packages=['nip24'],
      zip_safe=False,
      install_requires=['lxml', 'python-dateutil'])