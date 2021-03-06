# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mongoengine as me

from st2common import log as logging
from st2common.models.db import MongoDBAccess
from st2common.models.db import stormbase

__all__ = [
    'ActionAliasDB'
]


LOG = logging.getLogger(__name__)

PACK_SEPARATOR = '.'


class ActionAliasDB(stormbase.StormBaseDB):
    """
        Database entity that represent an Alias for an action.
    """
    ref = me.StringField(required=True)
    pack = me.StringField(
        required=True,
        help_text='Name of the content pack.')
    enabled = me.BooleanField(
        required=True, default=True,
        help_text='A flag indicating whether the action alias is enabled.')
    action_ref = me.StringField(
        required=True,
        help_text='Reference of the Action map this alias.')
    formats = me.ListField(
        field=me.StringField(),
        help_text='Possible parameter formats that an alias supports.')

    meta = {
        'indexes': ['name']
    }


# specialized access objects
actionalias_access = MongoDBAccess(ActionAliasDB)

MODELS = [ActionAliasDB]
