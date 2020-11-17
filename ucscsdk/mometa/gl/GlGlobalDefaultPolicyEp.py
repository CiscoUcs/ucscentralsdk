"""This module contains the general information for GlGlobalDefaultPolicyEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlGlobalDefaultPolicyEpConsts():
    pass


class GlGlobalDefaultPolicyEp(ManagedObject):
    """This is GlGlobalDefaultPolicyEp class."""

    consts = GlGlobalDefaultPolicyEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlGlobalDefaultPolicyEp", "glGlobalDefaultPolicyEp", "gdpep", VersionMeta.Version201a, "InputOutput", 0xf, [], ["read-only"], [u'glPolicyResolutionEp'], [u'glPolicyResOp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "num_of_conflicts": MoPropertyMeta("num_of_conflicts", "numOfConflicts", "uint", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "numOfConflicts": "num_of_conflicts", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.index = None
        self.num_of_conflicts = None
        self.status = None

        ManagedObject.__init__(self, "GlGlobalDefaultPolicyEp", parent_mo_or_dn, **kwargs)

