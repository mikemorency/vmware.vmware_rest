#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: appliance_vmon_service_info
short_description: Returns the state of a service.
description: Returns the state of a service.
options:
    service:
        description:
        - identifier of the service whose state is being queried.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.appliance_vmon_service).
            Required with I(state=['get'])
        type: str
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that runs the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: Get information about a VMON service
  vmware.vmware_rest.appliance_vmon_service_info:
    service: vpxd
  register: result
"""
RETURN = r"""
# content generated by the update_return_section callback# task: Get information about a VMON service
value:
  description: Get information about a VMON service
  returned: On success
  sample:
  - key: analytics
    value:
      description_key: cis.analytics.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.analytics.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: applmgmt
    value:
      description_key: cis.applmgmt.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.applmgmt.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: certificateauthority
    value:
      description_key: cis.certificateauthority.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: certificateathority.health.statuscode
      name_key: cis.certificateauthority.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: certificatemanagement
    value:
      description_key: cis.certificatemanagement.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: certificatemanagement.health.statuscode
      name_key: cis.certificatemanagement.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: cis-license
    value:
      description_key: cis.cis-license.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: The License Service is operational.
        id: cis.license.health.ok
      name_key: cis.cis-license.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: content-library
    value:
      description_key: cis.content-library.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: Database server connection is GREEN.
        id: com.vmware.vdcs.vsphere-cs-lib.db_health_green
      name_key: cis.content-library.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: eam
    value:
      description_key: cis.eam.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: ''
        id: cis.eam.statusOK
      name_key: cis.eam.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: envoy
    value:
      description_key: cis.envoy.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.envoy.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: hvc
    value:
      description_key: cis.hvc.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: hvc.health.statuscode
      name_key: cis.hvc.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: imagebuilder
    value:
      description_key: cis.imagebuilder.ServiceDescription
      name_key: cis.imagebuilder.ServiceName
      startup_type: MANUAL
      state: STOPPED
  - key: infraprofile
    value:
      description_key: cis.infraprofile.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: infraprofile.health.statuscode
      name_key: cis.infraprofile.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: lookupsvc
    value:
      description_key: cis.lookupsvc.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.lookupsvc.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: netdumper
    value:
      description_key: cis.netdumper.ServiceDescription
      name_key: cis.netdumper.ServiceName
      startup_type: MANUAL
      state: STOPPED
  - key: observability-vapi
    value:
      description_key: cis.observability-vapi.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: observability.health.statuscode
      name_key: cis.observability-vapi.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: perfcharts
    value:
      description_key: cis.perfcharts.ServiceDescription
      health: HEALTHY_WITH_WARNINGS
      health_messages:
      - args: []
        default_message: health.statsReoptInitalizer.illegalStateEx
        id: health.statsReoptInitalizer.illegalStateEx
      name_key: cis.perfcharts.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: pschealth
    value:
      description_key: cis.pschealth.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.pschealth.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: rbd
    value:
      description_key: cis.rbd.ServiceDescription
      name_key: cis.rbd.ServiceName
      startup_type: MANUAL
      state: STOPPED
  - key: rhttpproxy
    value:
      description_key: cis.rhttpproxy.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.rhttpproxy.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: sca
    value:
      description_key: cis.sca.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.sca.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: sps
    value:
      description_key: cis.sps.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.sps.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: statsmonitor
    value:
      description_key: cis.statsmonitor.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: Appliance monitoring service is healthy.
        id: com.vmware.applmgmt.mon.health.healthy
      name_key: cis.statsmonitor.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: sts
    value:
      description_key: cis.sts.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.sts.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: topologysvc
    value:
      description_key: cis.topologysvc.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: topologysvc.health.statuscode
      name_key: cis.topologysvc.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: trustmanagement
    value:
      description_key: cis.trustmanagement.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - GREEN
        default_message: Health is GREEN
        id: trustmanagement.health.statuscode
      name_key: cis.trustmanagement.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: updatemgr
    value:
      description_key: cis.updatemgr.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.updatemgr.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vapi-endpoint
    value:
      description_key: cis.vapi-endpoint.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - 2022-11-23T20:10:44UTC
        - 2022-11-23T20:10:46UTC
        default_message: Configuration health status is created between 2022-11-23T20:10:44UTC
          and 2022-11-23T20:10:46UTC.
        id: com.vmware.vapi.endpoint.healthStatusProducedTimes
      name_key: cis.vapi-endpoint.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vcha
    value:
      description_key: cis.vcha.ServiceDescription
      name_key: cis.vcha.ServiceName
      startup_type: DISABLED
      state: STOPPED
  - key: vlcm
    value:
      description_key: cis.vlcm.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.vlcm.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vmcam
    value:
      description_key: cis.vmcam.ServiceDescription
      name_key: cis.vmcam.ServiceName
      startup_type: MANUAL
      state: STOPPED
  - key: vmonapi
    value:
      description_key: cis.vmonapi.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.vmonapi.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vmware-postgres-archiver
    value:
      description_key: cis.vmware-postgres-archiver.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: VMware Archiver service is healthy.
        id: cis.vmware-postgres-archiver.health.healthy
      name_key: cis.vmware-postgres-archiver.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vmware-vpostgres
    value:
      description_key: cis.vmware-vpostgres.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: Service vmware-vpostgres is healthy.
        id: cis.vmware-vpostgres.health.healthy
      name_key: cis.vmware-vpostgres.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vpxd
    value:
      description_key: cis.vpxd.ServiceDescription
      health: HEALTHY
      health_messages:
      - args:
        - vCenter Server
        - GREEN
        default_message: '{0} health is {1}'
        id: vc.health.statuscode
      - args:
        - VirtualCenter Database
        - GREEN
        default_message: '{0} health is {1}'
        id: vc.health.statuscode
      name_key: cis.vpxd.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vpxd-svcs
    value:
      description_key: cis.vpxd-svcs.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: Tagging service is in a healthy state
        id: cis.tagging.health.status
      name_key: cis.vpxd-svcs.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vsan-health
    value:
      description_key: cis.vsan-health.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.vsan-health.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vsm
    value:
      description_key: cis.vsm.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.vsm.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vsphere-ui
    value:
      description_key: cis.vsphere-ui.ServiceDescription
      name_key: cis.vsphere-ui.ServiceName
      startup_type: AUTOMATIC
      state: STOPPED
  - key: vstats
    value:
      description_key: cis.vstats.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.vstats.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: vtsdb
    value:
      description_key: cis.vtsdb.ServiceDescription
      health: HEALTHY
      health_messages:
      - args: []
        default_message: Service vtsdb is healthy.
        id: cis.vtsdb.health.healthy
      name_key: cis.vtsdb.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  - key: wcp
    value:
      description_key: cis.wcp.ServiceDescription
      health: HEALTHY
      health_messages: []
      name_key: cis.wcp.ServiceName
      startup_type: AUTOMATIC
      state: STARTED
  type: list
"""


# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "get": {"query": {}, "body": {}, "path": {"service": "service"}}
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback
import os

if os.getenv("VMWARE_ENABLE_TURBO", False):
    try:
        from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
            EmbeddedModuleFailure,
        )
        from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
            AnsibleTurboModule as AnsibleModule,
        )

        AnsibleModule.collection_name = "vmware.vmware_rest"
    except ImportError:
        from ansible.module_utils.basic import AnsibleModule
else:
    from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    gen_args,
    open_session,
    session_timeout,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["service"] = {"type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: info_no_list_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/rest/appliance/vmon/service").format(
        **params
    )


async def entry_point(module, session):
    return await _info(module.params, session)


async def _info(params, session):
    payload_format = list(PAYLOAD_FORMAT.values())[0]
    _in_query_parameters = payload_format["query"].keys()
    _url = ("https://{vcenter_hostname}" "/rest/appliance/vmon/service").format(
        **params
    ) + gen_args(params, _in_query_parameters)
    async with session.get(_url, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(current_loop)
        current_loop.run_until_complete(main())
    finally:
        current_loop.close()
