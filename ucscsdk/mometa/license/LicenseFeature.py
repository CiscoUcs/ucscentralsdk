"""This module contains the general information for LicenseFeature ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LicenseFeatureConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    TYPE_BOOLEAN = "boolean"
    TYPE_COUNTED = "counted"


class LicenseFeature(ManagedObject):
    """This is LicenseFeature class."""

    consts = LicenseFeatureConsts()
    naming_props = set([u'name', u'vendor', u'version'])

    mo_meta = MoMeta("LicenseFeature", "licenseFeature", "feature-[name]-[vendor]-[version]", VersionMeta.Version111a, "InputOutput", 0xff, [], ["admin"], [u'licenseEp'], [u'licenseInstance'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "grace_period": MoPropertyMeta("grace_period", "gracePeriod", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,64}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boolean", "counted"], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x80, 1, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "gracePeriod": "grace_period", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "vendor": "vendor", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, name, vendor, version, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.vendor = vendor
        self.version = version
        self.child_action = None
        self.descr = None
        self.grace_period = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LicenseFeature", parent_mo_or_dn, **kwargs)
