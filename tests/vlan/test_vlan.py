import pytest
import logging

logger = logging.getLogger(__name__)

pytestmark = [
    pytest.mark.topology('t0')
]

def test_vlan_tc3_send_invalid_vid(
    duthosts,
    rand_one_dut_hostname):

    duthost = duthosts[rand_one_dut_hostname]

    config_facts = duthost.config_facts(
        host=duthost.hostname,
        source="running"
    )['ansible_facts']
    
    print("*" * 1000)

    print(config_facts.get("VLAN", {}))
    print(config_facts.get("VLAN_MEMBER", {}))
    print(config_facts.get("PORT", {}))

    assert "VLAN" in config_facts