"""This module contains the general information for IppoolBlock ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class IppoolBlockConsts():
    CONFIG_SCOPE_PRIVATE = "private"
    CONFIG_SCOPE_PUBLIC = "public"
    SCOPE_PRIVATE = "private"
    SCOPE_PUBLIC = "public"


class IppoolBlock(ManagedObject):
    """This is IppoolBlock class."""

    consts = IppoolBlockConsts()
    naming_props = set([u'from', u'to'])

    mo_meta = MoMeta("IppoolBlock", "ippoolBlock", "block-[r_from]-[to]", VersionMeta.Version101a, "InputOutput", 0xfff, [], ["admin", "domain-group-management", "ls-network-policy"], [u'ippoolPool'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_scope": MoPropertyMeta("config_scope", "configScope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "def_gw": MoPropertyMeta("def_gw", "defGw", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x2, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x8, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "prim_dns": MoPropertyMeta("prim_dns", "primDns", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x10, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["private", "public"], []), 
        "sec_dns": MoPropertyMeta("sec_dns", "secDns", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x100, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "subnet": MoPropertyMeta("subnet", "subnet", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x400, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "to": MoPropertyMeta("to", "to", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x800, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "configScope": "config_scope", 
        "defGw": "def_gw", 
        "dn": "dn", 
        "from": "r_from", 
        "primDns": "prim_dns", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "scope": "scope", 
        "secDns": "sec_dns", 
        "size": "size", 
        "status": "status", 
        "subnet": "subnet", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.r_from = r_from
        self.to = to
        self.assigned = None
        self.child_action = None
        self.config_scope = None
        self.def_gw = None
        self.prim_dns = None
        self.qualifier = None
        self.scope = None
        self.sec_dns = None
        self.size = None
        self.status = None
        self.subnet = None

        ManagedObject.__init__(self, "IppoolBlock", parent_mo_or_dn, **kwargs)

