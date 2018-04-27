"""This module contains the general information for VnicFcGroupDef ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class VnicFcGroupDefConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"


class VnicFcGroupDef(ManagedObject):
    """This is VnicFcGroupDef class."""

    consts = VnicFcGroupDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicFcGroupDef", "vnicFcGroupDef", "fc-group", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-storage"], [u'storageIniGroup'], [u'faultInst', u'storageConnectionDef', u'vnicIniGrpFc', u'vnicIniGrpFcB'], ["Add", "Get", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "max_data_field_size": MoPropertyMeta("max_data_field_size", "maxDataFieldSize", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["256-2112"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "nw_templ_name": MoPropertyMeta("nw_templ_name", "nwTemplName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_storage_conn_policy_name": MoPropertyMeta("oper_storage_conn_policy_name", "operStorageConnPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "qos_policy_name": MoPropertyMeta("qos_policy_name", "qosPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_conn_policy_name": MoPropertyMeta("storage_conn_policy_name", "storageConnPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "identPoolName": "ident_pool_name", 
        "intId": "int_id", 
        "maxDataFieldSize": "max_data_field_size", 
        "name": "name", 
        "nwTemplName": "nw_templ_name", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operStorageConnPolicyName": "oper_storage_conn_policy_name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qosPolicyName": "qos_policy_name", 
        "rn": "rn", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "storageConnPolicyName": "storage_conn_policy_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_profile_name = None
        self.child_action = None
        self.descr = None
        self.ident_pool_name = None
        self.int_id = None
        self.max_data_field_size = None
        self.name = None
        self.nw_templ_name = None
        self.oper_stats_policy_name = None
        self.oper_storage_conn_policy_name = None
        self.policy_level = None
        self.policy_owner = None
        self.qos_policy_name = None
        self.stats_policy_name = None
        self.status = None
        self.storage_conn_policy_name = None

        ManagedObject.__init__(self, "VnicFcGroupDef", parent_mo_or_dn, **kwargs)

