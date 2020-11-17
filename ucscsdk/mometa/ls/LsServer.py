"""This module contains the general information for LsServer ManagedObject."""

from ...ucscmo import ManagedObject
from ...ucsccoremeta import UcscVersion, MoPropertyMeta, MoMeta
from ...ucscmeta import VersionMeta


class LsServerConsts():
    ASSIGN_STATE_ASSIGNED = "assigned"
    ASSIGN_STATE_FAILED = "failed"
    ASSIGN_STATE_UNASSIGNED = "unassigned"
    ASSOC_STATE_ASSOCIATED = "associated"
    ASSOC_STATE_ASSOCIATING = "associating"
    ASSOC_STATE_DISASSOCIATING = "disassociating"
    ASSOC_STATE_FAILED = "failed"
    ASSOC_STATE_UNASSOCIATED = "unassociated"
    CONFIG_STATE_APPLIED = "applied"
    CONFIG_STATE_APPLYING = "applying"
    CONFIG_STATE_FAILED_TO_APPLY = "failed-to-apply"
    CONFIG_STATE_NOT_APPLIED = "not-applied"
    EXT_IPSTATE_NONE = "none"
    EXT_IPSTATE_POOLED = "pooled"
    EXT_IPSTATE_STATIC = "static"
    FSM_PREV_CONFIGURE_ANALYZE_IMPACT = "ConfigureAnalyzeImpact"
    FSM_PREV_CONFIGURE_APPLY_CONFIG = "ConfigureApplyConfig"
    FSM_PREV_CONFIGURE_APPLY_RENAME = "ConfigureApplyRename"
    FSM_PREV_CONFIGURE_APPLY_TEMPLATE = "ConfigureApplyTemplate"
    FSM_PREV_CONFIGURE_APPLY_THROTTLE = "ConfigureApplyThrottle"
    FSM_PREV_CONFIGURE_BEGIN = "ConfigureBegin"
    FSM_PREV_CONFIGURE_CONSUMER_VXAN_DEPLOYMENT = "ConfigureConsumerVxanDeployment"
    FSM_PREV_CONFIGURE_DELETE_ID_CONSUMER_MAP = "ConfigureDeleteIdConsumerMap"
    FSM_PREV_CONFIGURE_EVALUATE_ASSOCIATION = "ConfigureEvaluateAssociation"
    FSM_PREV_CONFIGURE_EVALUATE_SERVER_ASSIGN = "ConfigureEvaluateServerAssign"
    FSM_PREV_CONFIGURE_FAIL = "ConfigureFail"
    FSM_PREV_CONFIGURE_PROCESS_ID_CONSUMER_MAP = "ConfigureProcessIdConsumerMap"
    FSM_PREV_CONFIGURE_REPLACE_ID_ACQUIRER = "ConfigureReplaceIdAcquirer"
    FSM_PREV_CONFIGURE_RESOLVE_DOMAIN_GROUP_POLICIES = "ConfigureResolveDomainGroupPolicies"
    FSM_PREV_CONFIGURE_RESOLVE_IDENTIFIERS = "ConfigureResolveIdentifiers"
    FSM_PREV_CONFIGURE_RESOLVE_NETWORK_TEMPLATES = "ConfigureResolveNetworkTemplates"
    FSM_PREV_CONFIGURE_RESOLVE_POLICIES = "ConfigureResolvePolicies"
    FSM_PREV_CONFIGURE_RESOLVE_STATIC_IDENTIFIERS = "ConfigureResolveStaticIdentifiers"
    FSM_PREV_CONFIGURE_SUCCESS = "ConfigureSuccess"
    FSM_PREV_CONFIGURE_THROTTLE_WAIT = "ConfigureThrottleWait"
    FSM_PREV_CONFIGURE_WAIT_FOR_ASSOC_COMPLETION = "ConfigureWaitForAssocCompletion"
    FSM_PREV_CONFIGURE_WAIT_FOR_CONSUMER_RECEIVING_VXAN = "ConfigureWaitForConsumerReceivingVxan"
    FSM_PREV_CONFIGURE_WAIT_FOR_DOMAIN_GROUP_POLICIES = "ConfigureWaitForDomainGroupPolicies"
    FSM_PREV_NOP = "nop"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_CANCELLED = "ERR-DIAG-cancelled"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_FSM_RESTARTED = "ERR-DIAG-fsm-restarted"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_TEST_FAILED = "ERR-DIAG-test-failed"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_AUTHENTICATION_FAILURE = "ERR-DNLD-authentication-failure"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_ERROR = "ERR-DNLD-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_HOSTKEY_MISMATCH = "ERR-DNLD-hostkey-mismatch"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_INVALID_IMAGE = "ERR-DNLD-invalid-image"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_FILE = "ERR-DNLD-no-file"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_SPACE = "ERR-DNLD-no-space"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_DELETE_ERROR = "ERR-DNS-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_GET_ERROR = "ERR-DNS-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_SET_ERROR = "ERR-DNS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_DIGEST_VALIDATION_ERROR = "ERR-Digest-Validation-error"
    FSM_RMT_INV_ERR_CODE_ERR_EXEC_GEN_CERT_ERROR = "ERR-Exec-Gen-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_EXEC_GET_CA_CERT_ERROR = "ERR-Exec-Get-CA-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_FILTER_ILLEGAL_FORMAT = "ERR-FILTER-illegal-format"
    FSM_RMT_INV_ERR_CODE_ERR_FSM_NO_SUCH_STATE = "ERR-FSM-no-such-state"
    FSM_RMT_INV_ERR_CODE_ERR_GET_CA_CERT_ERROR = "ERR-Get-CA-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_GET_CERT_ERROR = "ERR-Get-Cert-error"
    FSM_RMT_INV_ERR_CODE_ERR_GET_OUT_DIGET_MESSAGE_ERROR = "ERR-Get-Out-Diget-Message-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_REQUEST_ERROR = "ERR-HTTP-Request-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_SET_ERROR = "ERR-HTTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTPS_SET_ERROR = "ERR-HTTPS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_IPV6_ADDR_CONFIGURED = "ERR-Ipv6-addr-configured"
    FSM_RMT_INV_ERR_CODE_ERR_MO_CONFIG_CHILD_OBJECT_CANT_BE_CONFIGURED = "ERR-MO-CONFIG-child-object-cant-be-configured"
    FSM_RMT_INV_ERR_CODE_ERR_MO_META_NO_SUCH_OBJECT_CLASS = "ERR-MO-META-no-such-object-class"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_NO_SUCH_PROPERTY = "ERR-MO-PROPERTY-no-such-property"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_VALUE_OUT_OF_RANGE = "ERR-MO-PROPERTY-value-out-of-range"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ACCESS_DENIED = "ERR-MO-access-denied"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DELETION_RULE_VIOLATION = "ERR-MO-deletion-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DUPLICATE_OBJECT = "ERR-MO-duplicate-object"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CONTAINMENT = "ERR-MO-illegal-containment"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CREATION = "ERR-MO-illegal-creation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_ITERATOR_STATE = "ERR-MO-illegal-iterator-state"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_OBJECT_LIFECYCLE_TRANSITION = "ERR-MO-illegal-object-lifecycle-transition"
    FSM_RMT_INV_ERR_CODE_ERR_MO_NAMING_RULE_VIOLATION = "ERR-MO-naming-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_OBJECT_NOT_FOUND = "ERR-MO-object-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_MO_RESOURCE_ALLOCATION = "ERR-MO-resource-allocation"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_DELETE_ERROR = "ERR-NTP-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_GET_ERROR = "ERR-NTP-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_SET_ERROR = "ERR-NTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_POLICY_RESOLUTION_IN_PROGRESS = "ERR-Policy-resolution-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_TOKEN_REQUEST_DENIED = "ERR-TOKEN-request-denied"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_VM_IP_MASK_GATEWAY_ERROR = "ERR-Update-VM-IP-Mask-Gateway-error"
    FSM_RMT_INV_ERR_CODE_ERR_AAA_CONFIG_MODIFY_ERROR = "ERR-aaa-config-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_ACCT_REALM_SET_ERROR = "ERR-acct-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_ADMIN_PASSWD_SET = "ERR-admin-passwd-set"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_REALM_SET_ERROR = "ERR-auth-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHENTICATION = "ERR-authentication"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHORIZATION_REQUIRED = "ERR-authorization-required"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_CHASSISPACK_UNDER_DG = "ERR-create-chassispack-under-dg"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_HFP_UNDER_DG = "ERR-create-hfp-under-dg"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_KEYRING = "ERR-create-keyring"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_LOCALE = "ERR-create-locale"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_ROLE = "ERR-create-role"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_USER = "ERR-create-user"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_LOCALE = "ERR-delete-locale"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_ROLE = "ERR-delete-role"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_SESSION = "ERR-delete-session"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_USER = "ERR-delete-user"
    FSM_RMT_INV_ERR_CODE_ERR_ESTIMATE_IMPACT_ON_RECONNECT = "ERR-estimate-impact-on-reconnect"
    FSM_RMT_INV_ERR_CODE_ERR_GET_MAX_HTTP_USER_SESSIONS = "ERR-get-max-http-user-sessions"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_INITIALIZING = "ERR-http-initializing"
    FSM_RMT_INV_ERR_CODE_ERR_INTERNAL_ERROR = "ERR-internal-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_DELETE_ERROR = "ERR-ldap-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GET_ERROR = "ERR-ldap-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_MODIFY_ERROR = "ERR-ldap-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_SET_ERROR = "ERR-ldap-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_SET_ERROR = "ERR-ldap-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LOCALE_SET_ERROR = "ERR-locale-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_MAX_USERID_SESSIONS_REACHED = "ERR-max-userid-sessions-reached"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_LOCALE = "ERR-modify-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_ROLE = "ERR-modify-role"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER = "ERR-modify-user"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_LOCALE = "ERR-modify-user-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_ROLE = "ERR-modify-user-role"
    FSM_RMT_INV_ERR_CODE_ERR_NFS_DOWN = "ERR-nfs-down"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_MODIFY_ERROR = "ERR-provider-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_SET_ERROR = "ERR-provider-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GLOBAL_SET_ERROR = "ERR-radius-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GROUP_SET_ERROR = "ERR-radius-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_SET_ERROR = "ERR-radius-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_ROLE_SET_ERROR = "ERR-role-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_SERVICE_NOT_READY = "ERR-service-not-ready"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_CACHE_FULL = "ERR-session-cache-full"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_NOT_FOUND = "ERR-session-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_ENABLE_ERROR = "ERR-tacacs-enable-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GLOBAL_SET_ERROR = "ERR-tacacs-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GROUP_SET_ERROR = "ERR-tacacs-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_SET_ERROR = "ERR-tacacs-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TIMEZONE_SET_ERROR = "ERR-timezone-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_USER_ACCOUNT_EXPIRED = "ERR-user-account-expired"
    FSM_RMT_INV_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
    FSM_RMT_INV_ERR_CODE_NONE = "none"
    FSM_STAMP_NEVER = "never"
    FSM_STATUS_CONFIGURE_ANALYZE_IMPACT = "ConfigureAnalyzeImpact"
    FSM_STATUS_CONFIGURE_APPLY_CONFIG = "ConfigureApplyConfig"
    FSM_STATUS_CONFIGURE_APPLY_RENAME = "ConfigureApplyRename"
    FSM_STATUS_CONFIGURE_APPLY_TEMPLATE = "ConfigureApplyTemplate"
    FSM_STATUS_CONFIGURE_APPLY_THROTTLE = "ConfigureApplyThrottle"
    FSM_STATUS_CONFIGURE_BEGIN = "ConfigureBegin"
    FSM_STATUS_CONFIGURE_CONSUMER_VXAN_DEPLOYMENT = "ConfigureConsumerVxanDeployment"
    FSM_STATUS_CONFIGURE_DELETE_ID_CONSUMER_MAP = "ConfigureDeleteIdConsumerMap"
    FSM_STATUS_CONFIGURE_EVALUATE_ASSOCIATION = "ConfigureEvaluateAssociation"
    FSM_STATUS_CONFIGURE_EVALUATE_SERVER_ASSIGN = "ConfigureEvaluateServerAssign"
    FSM_STATUS_CONFIGURE_FAIL = "ConfigureFail"
    FSM_STATUS_CONFIGURE_PROCESS_ID_CONSUMER_MAP = "ConfigureProcessIdConsumerMap"
    FSM_STATUS_CONFIGURE_REPLACE_ID_ACQUIRER = "ConfigureReplaceIdAcquirer"
    FSM_STATUS_CONFIGURE_RESOLVE_DOMAIN_GROUP_POLICIES = "ConfigureResolveDomainGroupPolicies"
    FSM_STATUS_CONFIGURE_RESOLVE_IDENTIFIERS = "ConfigureResolveIdentifiers"
    FSM_STATUS_CONFIGURE_RESOLVE_NETWORK_TEMPLATES = "ConfigureResolveNetworkTemplates"
    FSM_STATUS_CONFIGURE_RESOLVE_POLICIES = "ConfigureResolvePolicies"
    FSM_STATUS_CONFIGURE_RESOLVE_STATIC_IDENTIFIERS = "ConfigureResolveStaticIdentifiers"
    FSM_STATUS_CONFIGURE_SUCCESS = "ConfigureSuccess"
    FSM_STATUS_CONFIGURE_THROTTLE_WAIT = "ConfigureThrottleWait"
    FSM_STATUS_CONFIGURE_WAIT_FOR_ASSOC_COMPLETION = "ConfigureWaitForAssocCompletion"
    FSM_STATUS_CONFIGURE_WAIT_FOR_CONSUMER_RECEIVING_VXAN = "ConfigureWaitForConsumerReceivingVxan"
    FSM_STATUS_CONFIGURE_WAIT_FOR_DOMAIN_GROUP_POLICIES = "ConfigureWaitForDomainGroupPolicies"
    FSM_STATUS_NOP = "nop"
    INT_ID_NONE = "none"
    OPER_STATE_BIOS_RESTORE = "bios-restore"
    OPER_STATE_CMOS_RESET = "cmos-reset"
    OPER_STATE_COMPUTE_FAILED = "compute-failed"
    OPER_STATE_COMPUTE_MISMATCH = "compute-mismatch"
    OPER_STATE_CONFIG = "config"
    OPER_STATE_CONFIG_FAILURE = "config-failure"
    OPER_STATE_DECOMISSIONING = "decomissioning"
    OPER_STATE_DEGRADED = "degraded"
    OPER_STATE_DIAGNOSTICS = "diagnostics"
    OPER_STATE_DIAGNOSTICS_FAILED = "diagnostics-failed"
    OPER_STATE_DISABLED = "disabled"
    OPER_STATE_DISCOVERY = "discovery"
    OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    OPER_STATE_INACCESSIBLE = "inaccessible"
    OPER_STATE_INDETERMINATE = "indeterminate"
    OPER_STATE_INOPERABLE = "inoperable"
    OPER_STATE_MAINTENANCE = "maintenance"
    OPER_STATE_MAINTENANCE_FAILED = "maintenance-failed"
    OPER_STATE_OK = "ok"
    OPER_STATE_PENDING_REASSOCIATION = "pending-reassociation"
    OPER_STATE_PENDING_REBOOT = "pending-reboot"
    OPER_STATE_POWER_OFF = "power-off"
    OPER_STATE_POWER_PROBLEM = "power-problem"
    OPER_STATE_REMOVED = "removed"
    OPER_STATE_RESTART = "restart"
    OPER_STATE_TEST = "test"
    OPER_STATE_TEST_FAILED = "test-failed"
    OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    OPER_STATE_UNASSOCIATED = "unassociated"
    OPER_STATE_UNCONFIG = "unconfig"
    OPER_STATE_UNCONFIG_FAILED = "unconfig-failed"
    OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    OWNER_MANAGEMENT = "management"
    OWNER_PHYSICAL_DEFAULT_CONFIG = "physical-default-config"
    OWNER_PHYSICAL_INHERIT = "physical-inherit"
    OWNER_POLICY = "policy"
    OWNER_SYSTEM = "system"
    OWNER_TIER = "tier"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    TYPE_INITIAL_TEMPLATE = "initial-template"
    TYPE_INSTANCE = "instance"
    TYPE_UPDATING_TEMPLATE = "updating-template"
    UUID_DERIVED = "derived"


class LsServer(ManagedObject):
    """This is LsServer class."""

    consts = LsServerConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LsServer", "lsServer", "ls-[name]", VersionMeta.Version101a, "InputOutput", 0x3fffffff, [], ["admin", "ls-compute", "ls-config", "ls-server"], [u'computeTemplate', u'orgOrg'], [u'cimcvmediaMountConfigDef', u'computeEnvFeatMask', u'computeNetworkFeatMask', u'computePowerSyncDef', u'computeServerFeatMask', u'computeStorageFeatMask', u'eventInst', u'fabricVCon', u'faultInst', u'identRequestEp', u'lsBinding', u'lsFcLocale', u'lsIdentityInfo', u'lsIssues', u'lsPower', u'lsRequirement', u'lsSPMeta', u'lsServerAssocCtx', u'lsServerExtension', u'lsServerFsm', u'lsServerFsmTask', u'lsServerOperation', u'lsVConAssign', u'lsbootDef', u'lsmaintAck', u'lstorageProfileBinding', u'lstorageProfileDef', u'mgmtInterface', u'storageIniGroup', u'storageIpV4PooledAddr', u'storageIpV4StaticAddr', u'storageLocalDiskConfigDef', u'storageScsiLunInstRef', u'storageVirtualDriveRef', u'vnicConnDef', u'vnicDefBeh', u'vnicDynamicCon', u'vnicEther', u'vnicFc', u'vnicFcNode', u'vnicIScsi', u'vnicIScsiBootParams', u'vnicIScsiLCP', u'vnicIScsiNode', u'vnicIniGrpFc', u'vnicIniGrpFcB', u'vnicIpV4MgmtPooledAddr', u'vnicIpV4PooledAddr', u'vnicIpV4StaticAddr', u'vnicLstorageIScsi', u'vnicMgmt', u'vnicMonSesFc'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "agent_policy_name": MoPropertyMeta("agent_policy_name", "agentPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "assign_state": MoPropertyMeta("assign_state", "assignState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["assigned", "failed", "unassigned"], []), 
        "assoc_state": MoPropertyMeta("assoc_state", "assocState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["associated", "associating", "disassociating", "failed", "unassociated"], []), 
        "bios_profile_name": MoPropertyMeta("bios_profile_name", "biosProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "boot_policy_name": MoPropertyMeta("boot_policy_name", "bootPolicyName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_qualifier": MoPropertyMeta("config_qualifier", "configQualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic),){0,65}(defaultValue|not-applicable|boot-order-pxe|wwnn-derivation-from-vhba|migration|incompat-bios-for-sriov-vnics|iscsi-initiator-ip-address|remote-policy|wwnn-assignment|processor-requirement|physical-requirement|hostimg-policy-invalid|vif-resources-overprovisioned|pinning-invalid|incompatible-number-of-local-disks|mac-derivation-virtualized-port|switch-virtual-if-capacity|invalid-wwn|missing-raid-key|board-controller-update-unsupported|insufficient-resources|compute-undiscovered|boot-configuration-invalid|incompatible-bios-image|iscsi-config|storage-path-configuration-error|resource-ownership-conflict|system-uuid-assignment|server-position-requirement|destructive-local-disk-config|imgsec-policy-invalid|pinning-vlan-mismatch|non-interrupt-fsm-running|vnic-capacity|adaptor-requirement|mac-address-assignment|qos-policy-invalid|insufficient-power-budget|boot-order-iscsi|vnic-vcon-provisioning-change|adaptor-protected-eth-capability|connection-placement|incompatible-disk-types|vnic-not-ha-ready|zone-capacity|adaptor-out-of-vifs|duplicate-address-conflict|vhba-capacity|boot-order-san-image-path|compute-unavailable|power-group-requirement|provsrv-policy-invalid|vnic-vlan-assignment-error|missing-firmware-image|wwpn-assignment|memory-requirement|vlan-port-capacity|bootip-policy-invalid|vfc-vnic-pvlan-conflict|named-vlan-inaccessible|adaptor-fcoe-capability|wwpn-derivation-virtualized-port|incompatible-raid-level|missing-primary-vlan|fcoe-capacity|dynamic-vf-vnic){0,1}""", [], []), 
        "config_state": MoPropertyMeta("config_state", "configState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["applied", "applying", "failed-to-apply", "not-applied"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "domain_dn": MoPropertyMeta("domain_dn", "domainDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "domain_group": MoPropertyMeta("domain_group", "domainGroup", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "domain_group_dn": MoPropertyMeta("domain_group_dn", "domainGroupDn", "string", VersionMeta.Version131a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dynamic_con_policy_name": MoPropertyMeta("dynamic_con_policy_name", "dynamicConPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ext_ip_pool_name": MoPropertyMeta("ext_ip_pool_name", "extIPPoolName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "ext_ip_state": MoPropertyMeta("ext_ip_state", "extIPState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["none", "pooled", "static"], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_flags": MoPropertyMeta("fsm_flags", "fsmFlags", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ConfigureAnalyzeImpact", "ConfigureApplyConfig", "ConfigureApplyRename", "ConfigureApplyTemplate", "ConfigureApplyThrottle", "ConfigureBegin", "ConfigureConsumerVxanDeployment", "ConfigureDeleteIdConsumerMap", "ConfigureEvaluateAssociation", "ConfigureEvaluateServerAssign", "ConfigureFail", "ConfigureProcessIdConsumerMap", "ConfigureReplaceIdAcquirer", "ConfigureResolveDomainGroupPolicies", "ConfigureResolveIdentifiers", "ConfigureResolveNetworkTemplates", "ConfigureResolvePolicies", "ConfigureResolveStaticIdentifiers", "ConfigureSuccess", "ConfigureThrottleWait", "ConfigureWaitForAssocCompletion", "ConfigureWaitForConsumerReceivingVxan", "ConfigureWaitForDomainGroupPolicies", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-error", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Digest-Validation-error", "ERR-Exec-Gen-Cert-error", "ERR-Exec-Get-CA-Cert-error", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-Get-CA-Cert-error", "ERR-Get-Cert-error", "ERR-Get-Out-Diget-Message-error", "ERR-HTTP-Request-error", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-Ipv6-addr-configured", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-Policy-resolution-in-progress", "ERR-TOKEN-request-denied", "ERR-Update-VM-IP-Mask-Gateway-error", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-create-chassispack-under-dg", "ERR-create-hfp-under-dg", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-estimate-impact-on-reconnect", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-nfs-down", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-role-set-error", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-password-strength-check", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-set-error", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["ConfigureAnalyzeImpact", "ConfigureApplyConfig", "ConfigureApplyRename", "ConfigureApplyTemplate", "ConfigureApplyThrottle", "ConfigureBegin", "ConfigureConsumerVxanDeployment", "ConfigureDeleteIdConsumerMap", "ConfigureEvaluateAssociation", "ConfigureEvaluateServerAssign", "ConfigureFail", "ConfigureProcessIdConsumerMap", "ConfigureReplaceIdAcquirer", "ConfigureResolveDomainGroupPolicies", "ConfigureResolveIdentifiers", "ConfigureResolveNetworkTemplates", "ConfigureResolvePolicies", "ConfigureResolveStaticIdentifiers", "ConfigureSuccess", "ConfigureThrottleWait", "ConfigureWaitForAssocCompletion", "ConfigureWaitForConsumerReceivingVxan", "ConfigureWaitForDomainGroupPolicies", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "graphics_card_policy_name": MoPropertyMeta("graphics_card_policy_name", "graphicsCardPolicyName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "host_fw_policy_name": MoPropertyMeta("host_fw_policy_name", "hostFwPolicyName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ident_pool_name": MoPropertyMeta("ident_pool_name", "identPoolName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x800, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "kvm_mgmt_policy_name": MoPropertyMeta("kvm_mgmt_policy_name", "kvmMgmtPolicyName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "local_disk_policy_name": MoPropertyMeta("local_disk_policy_name", "localDiskPolicyName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "ls_dn": MoPropertyMeta("ls_dn", "lsDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "maint_policy_name": MoPropertyMeta("maint_policy_name", "maintPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x2000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "mgmt_access_policy_name": MoPropertyMeta("mgmt_access_policy_name", "mgmtAccessPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x4000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "mgmt_fw_policy_name": MoPropertyMeta("mgmt_fw_policy_name", "mgmtFwPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x10000, None, None, r"""[\-\.:_a-zA-Z0-9]{2,32}""", [], []), 
        "oper_bios_profile_name": MoPropertyMeta("oper_bios_profile_name", "operBiosProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_boot_policy_name": MoPropertyMeta("oper_boot_policy_name", "operBootPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_dynamic_con_policy_name": MoPropertyMeta("oper_dynamic_con_policy_name", "operDynamicConPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_ext_ip_pool_name": MoPropertyMeta("oper_ext_ip_pool_name", "operExtIPPoolName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_graphics_card_policy_name": MoPropertyMeta("oper_graphics_card_policy_name", "operGraphicsCardPolicyName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_host_fw_policy_name": MoPropertyMeta("oper_host_fw_policy_name", "operHostFwPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_ident_pool_name": MoPropertyMeta("oper_ident_pool_name", "operIdentPoolName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_kvm_mgmt_policy_name": MoPropertyMeta("oper_kvm_mgmt_policy_name", "operKvmMgmtPolicyName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_local_disk_policy_name": MoPropertyMeta("oper_local_disk_policy_name", "operLocalDiskPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_maint_policy_name": MoPropertyMeta("oper_maint_policy_name", "operMaintPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_mgmt_access_policy_name": MoPropertyMeta("oper_mgmt_access_policy_name", "operMgmtAccessPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_mgmt_fw_policy_name": MoPropertyMeta("oper_mgmt_fw_policy_name", "operMgmtFwPolicyName", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_power_policy_name": MoPropertyMeta("oper_power_policy_name", "operPowerPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_power_sync_policy_name": MoPropertyMeta("oper_power_sync_policy_name", "operPowerSyncPolicyName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_scrub_policy_name": MoPropertyMeta("oper_scrub_policy_name", "operScrubPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_sol_policy_name": MoPropertyMeta("oper_sol_policy_name", "operSolPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_src_templ_name": MoPropertyMeta("oper_src_templ_name", "operSrcTemplName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bios-restore", "cmos-reset", "compute-failed", "compute-mismatch", "config", "config-failure", "decomissioning", "degraded", "diagnostics", "diagnostics-failed", "disabled", "discovery", "discovery-failed", "inaccessible", "indeterminate", "inoperable", "maintenance", "maintenance-failed", "ok", "pending-reassociation", "pending-reboot", "power-off", "power-problem", "removed", "restart", "test", "test-failed", "thermal-problem", "unassociated", "unconfig", "unconfig-failed", "voltage-problem"], []), 
        "oper_stats_policy_name": MoPropertyMeta("oper_stats_policy_name", "operStatsPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vcon_profile_name": MoPropertyMeta("oper_vcon_profile_name", "operVconProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_vmedia_policy_name": MoPropertyMeta("oper_vmedia_policy_name", "operVmediaPolicyName", "string", VersionMeta.Version121e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "owner": MoPropertyMeta("owner", "owner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["management", "physical-default-config", "physical-inherit", "policy", "system", "tier"], []), 
        "pn_dn": MoPropertyMeta("pn_dn", "pnDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "power_policy_name": MoPropertyMeta("power_policy_name", "powerPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "power_sync_policy_name": MoPropertyMeta("power_sync_policy_name", "powerSyncPolicyName", "string", VersionMeta.Version201a, MoPropertyMeta.READ_WRITE, 0x40000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x80000, 0, 256, None, [], []), 
        "scrub_policy_name": MoPropertyMeta("scrub_policy_name", "scrubPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x100000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "sol_policy_name": MoPropertyMeta("sol_policy_name", "solPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x200000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "src_templ_name": MoPropertyMeta("src_templ_name", "srcTemplName", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x400000, None, None, None, [], []), 
        "stats_policy_name": MoPropertyMeta("stats_policy_name", "statsPolicyName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x800000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x1000000, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.CREATE_ONLY, 0x2000000, None, None, None, ["initial-template", "instance", "updating-template"], []), 
        "usr_lbl": MoPropertyMeta("usr_lbl", "usrLbl", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x4000000, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,32}""", [], []), 
        "uuid": MoPropertyMeta("uuid", "uuid", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x8000000, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", ["derived"], []), 
        "uuid_suffix": MoPropertyMeta("uuid_suffix", "uuidSuffix", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], []), 
        "vcon_profile_name": MoPropertyMeta("vcon_profile_name", "vconProfileName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x10000000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "vmedia_policy_name": MoPropertyMeta("vmedia_policy_name", "vmediaPolicyName", "string", VersionMeta.Version121e, MoPropertyMeta.READ_WRITE, 0x20000000, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "agentPolicyName": "agent_policy_name", 
        "assignState": "assign_state", 
        "assocState": "assoc_state", 
        "biosProfileName": "bios_profile_name", 
        "bootPolicyName": "boot_policy_name", 
        "childAction": "child_action", 
        "configQualifier": "config_qualifier", 
        "configState": "config_state", 
        "descr": "descr", 
        "dn": "dn", 
        "domain": "domain", 
        "domainDn": "domain_dn", 
        "domainGroup": "domain_group", 
        "domainGroupDn": "domain_group_dn", 
        "dynamicConPolicyName": "dynamic_con_policy_name", 
        "extIPPoolName": "ext_ip_pool_name", 
        "extIPState": "ext_ip_state", 
        "fltAggr": "flt_aggr", 
        "fsmDescr": "fsm_descr", 
        "fsmFlags": "fsm_flags", 
        "fsmPrev": "fsm_prev", 
        "fsmProgr": "fsm_progr", 
        "fsmRmtInvErrCode": "fsm_rmt_inv_err_code", 
        "fsmRmtInvErrDescr": "fsm_rmt_inv_err_descr", 
        "fsmRmtInvRslt": "fsm_rmt_inv_rslt", 
        "fsmStageDescr": "fsm_stage_descr", 
        "fsmStamp": "fsm_stamp", 
        "fsmStatus": "fsm_status", 
        "fsmTry": "fsm_try", 
        "graphicsCardPolicyName": "graphics_card_policy_name", 
        "hostFwPolicyName": "host_fw_policy_name", 
        "identPoolName": "ident_pool_name", 
        "intId": "int_id", 
        "kvmMgmtPolicyName": "kvm_mgmt_policy_name", 
        "localDiskPolicyName": "local_disk_policy_name", 
        "lsDn": "ls_dn", 
        "maintPolicyName": "maint_policy_name", 
        "mgmtAccessPolicyName": "mgmt_access_policy_name", 
        "mgmtFwPolicyName": "mgmt_fw_policy_name", 
        "name": "name", 
        "operBiosProfileName": "oper_bios_profile_name", 
        "operBootPolicyName": "oper_boot_policy_name", 
        "operDynamicConPolicyName": "oper_dynamic_con_policy_name", 
        "operExtIPPoolName": "oper_ext_ip_pool_name", 
        "operGraphicsCardPolicyName": "oper_graphics_card_policy_name", 
        "operHostFwPolicyName": "oper_host_fw_policy_name", 
        "operIdentPoolName": "oper_ident_pool_name", 
        "operKvmMgmtPolicyName": "oper_kvm_mgmt_policy_name", 
        "operLocalDiskPolicyName": "oper_local_disk_policy_name", 
        "operMaintPolicyName": "oper_maint_policy_name", 
        "operMgmtAccessPolicyName": "oper_mgmt_access_policy_name", 
        "operMgmtFwPolicyName": "oper_mgmt_fw_policy_name", 
        "operPowerPolicyName": "oper_power_policy_name", 
        "operPowerSyncPolicyName": "oper_power_sync_policy_name", 
        "operScrubPolicyName": "oper_scrub_policy_name", 
        "operSolPolicyName": "oper_sol_policy_name", 
        "operSrcTemplName": "oper_src_templ_name", 
        "operState": "oper_state", 
        "operStatsPolicyName": "oper_stats_policy_name", 
        "operVconProfileName": "oper_vcon_profile_name", 
        "operVmediaPolicyName": "oper_vmedia_policy_name", 
        "owner": "owner", 
        "pnDn": "pn_dn", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "powerPolicyName": "power_policy_name", 
        "powerSyncPolicyName": "power_sync_policy_name", 
        "rn": "rn", 
        "scrubPolicyName": "scrub_policy_name", 
        "solPolicyName": "sol_policy_name", 
        "srcTemplName": "src_templ_name", 
        "statsPolicyName": "stats_policy_name", 
        "status": "status", 
        "type": "type", 
        "usrLbl": "usr_lbl", 
        "uuid": "uuid", 
        "uuidSuffix": "uuid_suffix", 
        "vconProfileName": "vcon_profile_name", 
        "vmediaPolicyName": "vmedia_policy_name", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.agent_policy_name = None
        self.assign_state = None
        self.assoc_state = None
        self.bios_profile_name = None
        self.boot_policy_name = None
        self.child_action = None
        self.config_qualifier = None
        self.config_state = None
        self.descr = None
        self.domain = None
        self.domain_dn = None
        self.domain_group = None
        self.domain_group_dn = None
        self.dynamic_con_policy_name = None
        self.ext_ip_pool_name = None
        self.ext_ip_state = None
        self.flt_aggr = None
        self.fsm_descr = None
        self.fsm_flags = None
        self.fsm_prev = None
        self.fsm_progr = None
        self.fsm_rmt_inv_err_code = None
        self.fsm_rmt_inv_err_descr = None
        self.fsm_rmt_inv_rslt = None
        self.fsm_stage_descr = None
        self.fsm_stamp = None
        self.fsm_status = None
        self.fsm_try = None
        self.graphics_card_policy_name = None
        self.host_fw_policy_name = None
        self.ident_pool_name = None
        self.int_id = None
        self.kvm_mgmt_policy_name = None
        self.local_disk_policy_name = None
        self.ls_dn = None
        self.maint_policy_name = None
        self.mgmt_access_policy_name = None
        self.mgmt_fw_policy_name = None
        self.oper_bios_profile_name = None
        self.oper_boot_policy_name = None
        self.oper_dynamic_con_policy_name = None
        self.oper_ext_ip_pool_name = None
        self.oper_graphics_card_policy_name = None
        self.oper_host_fw_policy_name = None
        self.oper_ident_pool_name = None
        self.oper_kvm_mgmt_policy_name = None
        self.oper_local_disk_policy_name = None
        self.oper_maint_policy_name = None
        self.oper_mgmt_access_policy_name = None
        self.oper_mgmt_fw_policy_name = None
        self.oper_power_policy_name = None
        self.oper_power_sync_policy_name = None
        self.oper_scrub_policy_name = None
        self.oper_sol_policy_name = None
        self.oper_src_templ_name = None
        self.oper_state = None
        self.oper_stats_policy_name = None
        self.oper_vcon_profile_name = None
        self.oper_vmedia_policy_name = None
        self.owner = None
        self.pn_dn = None
        self.policy_level = None
        self.policy_owner = None
        self.power_policy_name = None
        self.power_sync_policy_name = None
        self.scrub_policy_name = None
        self.sol_policy_name = None
        self.src_templ_name = None
        self.stats_policy_name = None
        self.status = None
        self.type = None
        self.usr_lbl = None
        self.uuid = None
        self.uuid_suffix = None
        self.vcon_profile_name = None
        self.vmedia_policy_name = None

        ManagedObject.__init__(self, "LsServer", parent_mo_or_dn, **kwargs)

