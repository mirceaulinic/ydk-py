#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------


#  ----------------------------------------------------------------
#  bgp_codec.py Sample program illustrating use of codec service for
#  ydk.models.bgp.bgp.py which in turn is derived from the
#  open-config bgp yang module.
#

from ydk.models.bgp import bgp
from ydk.models.routing.routing_policy import RoutingPolicy

from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

def _get_bgp_config():
    bgp_cfg = bgp.Bgp()

    bgp_cfg.global_.config.as_ = 65001

    ipv4_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    ipv4_afsf.afi_safi_name = 'ipv4-unicast'
    ipv4_afsf.config.afi_safi_name = 'ipv4-unicast'
    ipv4_afsf.config.enabled = True

    ipv6_afsf = bgp_cfg.global_.afi_safis.AfiSafi()
    ipv6_afsf.afi_safi_name = 'ipv6-unicast'
    ipv6_afsf.config.afi_safi_name = 'ipv6-unicast'
    ipv6_afsf.config.enabled = True

    bgp_cfg.global_.afi_safis.afi_safi.append(ipv4_afsf)
    bgp_cfg.global_.afi_safis.afi_safi.append(ipv6_afsf)
    # Global config done

    # IPv4 Neighbor instance config
    nbr_ipv4 = bgp_cfg.neighbors.Neighbor()
    nbr_ipv4.neighbor_address = '192.168.1.1'
    nbr_ipv4.config.neighbor_address = '192.168.1.1'
    nbr_ipv4.config.peer_as = 65002

    nbr_ipv4_afsf = nbr_ipv4.afi_safis.AfiSafi()
    nbr_ipv4_afsf.afi_safi_name = 'ipv4-unicast'
    nbr_ipv4_afsf.config.peer_as = 65002
    nbr_ipv4_afsf.config.afi_safi_name = 'ipv4-unicast'
    nbr_ipv4_afsf.config.enabled = True

    # Create afi-safi policy instances
    nbr_ipv4.afi_safis.afi_safi.append(nbr_ipv4_afsf)

    bgp_cfg.neighbors.neighbor.append(nbr_ipv4)
    nbr_ipv4.parent = bgp_cfg.neighbors

    return bgp_cfg


def _get_routing_cfg():
    routing_policy = RoutingPolicy()

    pass_all_policy_defn = RoutingPolicy.PolicyDefinitions.PolicyDefinition()
    pass_all_policy_defn.name = 'PASS-ALL'

    routing_policy.policy_definitions.policy_definition.append(pass_all_policy_defn)
    pass_all_policy_defn._parent = routing_policy.policy_definitions

    comm_set = RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet()
    comm_set.community_set_name = 'testing'
    comm_set.community_member.append("testing123")
    comm_set.community_member.append("testing456")
    routing_policy.defined_sets.bgp_defined_sets.community_sets.community_set.append(comm_set)
    return routing_policy


def _get_bgp_routing_multiple_object():
    bgp_cfg = _get_bgp_config()
    routing_policy = _get_routing_cfg()
    return {'bgp':bgp_cfg, 'routing-policy':routing_policy}
    

def bgp_run(codec_service, provider):
    bgp_cfg = _get_bgp_config()
    bgp_payload = codec_service.encode(provider, bgp_cfg)
    bgp_entity = codec_service.decode(provider, bgp_payload)
#     print 'Encoded payload:\n', bgp_payload, \
#             '\nRe-encode the decoded payload:\n', codec_service.encode(provider, bgp_entity)
    assert bgp_payload == codec_service.encode(provider, bgp_entity)


def run_routing(codec_service, provider):
    routing_policy = _get_routing_cfg()
    routing_payload = codec_service.encode(provider, routing_policy)
    print routing_payload
    routing_entity = codec_service.decode(provider, routing_payload)
#     print 'Encoded payload:\n', routing_payload, \
#             '\nRe-encode the decoded payload:\n', codec_service.encode(provider, routing_entity)
    assert routing_payload == codec_service.encode(provider, routing_entity)


def run_multiple_routing_bgp(codec_service, provider):
    multi_cfg = _get_bgp_routing_multiple_object()
    multi_payload = codec_service.encode(provider, multi_cfg)
    # print routing_payload
    multi_entity = codec_service.decode(provider, multi_payload)
#     print 'Encoded payload:\n', multi_payload, \
#             '\nRe-encode the decoded payload:\n', codec_service.encode(provider, multi_entity)
    assert multi_payload == codec_service.encode(provider, multi_entity)


def init_logging():
    import logging
    logger = logging.getLogger("ydk")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                  "%(levelname)s - %(message)s"))
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == "__main__":
    init_logging()
    provider = CodecServiceProvider(type='xml')
    codec_service = CodecService()
    bgp_run(codec_service, provider)
    run_routing(codec_service, provider)
    run_multiple_routing_bgp(codec_service, provider)
    exit()
