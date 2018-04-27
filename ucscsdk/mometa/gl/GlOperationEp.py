"""This module contains the general information for GlOperationEp ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class GlOperationEpConsts():
    pass


class GlOperationEp(ManagedObject):
    """This is GlOperationEp class."""

    consts = GlOperationEpConsts()
    naming_props = set([])

    mo_meta = MoMeta("GlOperationEp", "glOperationEp", "opep", VersionMeta.Version201b, "InputOutput", 0xf, [], ["read-only"], [u'glLsp', u'glPolicy', u'glPool', u'glRequest', u'glServiceProfile', u'glVnicTemplate'], [u'glIdentCtxEp', u'glPolicyEp', u'glPoolEp', u'glTemplateEp', u'glVxanEp'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201b, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201b, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201b, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "GlOperationEp", parent_mo_or_dn, **kwargs)

