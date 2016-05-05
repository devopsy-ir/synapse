# -*- coding: utf-8 -*-
# Copyright 2014-2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from httppusher import HttpPusher

import logging
logger = logging.getLogger(__name__)


def create_pusher(hs, pusherdict):
    logger.info("trying to create_pusher for %r", pusherdict)

    PUSHER_TYPES = {
        "http": HttpPusher,
    }

    logger.info("email enable notifs: %r", hs.config.email_enable_notifs)
    if hs.config.email_enable_notifs:
        from synapse.push.emailpusher import EmailPusher
        PUSHER_TYPES["email"] = EmailPusher
        logger.info("defined email pusher type")

    if pusherdict['kind'] in PUSHER_TYPES:
        logger.info("found pusher")
        return PUSHER_TYPES[pusherdict['kind']](hs, pusherdict)
