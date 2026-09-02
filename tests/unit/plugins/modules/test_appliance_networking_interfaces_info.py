# -*- coding: utf-8 -*-
# Copyright: (c) 2026, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Unit tests for appliance_networking_interfaces_info module.

Tests validate the Info module behavior using the OperationConfig-based
architecture with mocked HTTP clients.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from unittest.mock import MagicMock, patch

from ansible_collections.vmware.vmware_rest.plugins.module_utils._operation_configs import (
    OperationConfig,
)
from ansible_collections.vmware.vmware_rest.plugins.module_utils._info_module import (
    VmwareRestInfoModuleBase,
)
from ansible_collections.vmware.vmware_rest.plugins.module_utils._errors import (
    RequiredPathParameterError,
)

from ...common.utils import CONNECTION_PARAMS, fail_json

LIST_ENDPOINT = "/appliance/networking/interfaces"
ITEM_ENDPOINT = "/appliance/networking/interfaces/{interface_name}"


@pytest.fixture
def mock_module():
    """
    Mock Ansible module object.
    """
    module = MagicMock()
    module.params = CONNECTION_PARAMS.copy()
    module.check_mode = False
    module.fail_json = fail_json
    return module


@pytest.fixture
def info_module(mock_module, mock_client):
    """
    Create info module instance matching appliance_networking_interfaces_info.

    Note: mock_client is provided by conftest.py - do not redefine it.
    """
    get_operation = OperationConfig(
        name="get",
        uri=ITEM_ENDPOINT,
        http_method="GET",
    )

    list_operation = OperationConfig(
        name="list",
        uri=LIST_ENDPOINT,
        http_method="GET",
    )

    with patch(
        "ansible_collections.vmware.vmware_rest.plugins.module_utils._module_base.Client",
        return_value=mock_client,
    ):
        module = VmwareRestInfoModuleBase(
            module=mock_module,
            moid_parameter_hints=["interface_name"],
            get_operation_config=get_operation,
            list_operation_config=list_operation,
        )
        yield module


# ============================================================================
# get_resource_info() Tests - GET by interface_name
# ============================================================================


def test_get_resource_info_by_id(info_module, mock_client):
    """
    Test getting a specific interface by name.
    """
    info_module.params["interface_name"] = "nic0"

    get_response = MagicMock()
    get_response.status = 200
    get_response.json = {
        "name": "nic0",
        "mac": "00:50:56:01:02:03",
        "status": "up",
        "ipv4": {"mode": "DHCP", "address": "10.0.0.5", "prefix": 24},
    }
    mock_client.get.return_value = get_response

    result = info_module.get_resource_info()

    assert "value" in result
    assert result["value"]["name"] == "nic0"
    assert result["value"]["ipv4"]["address"] == "10.0.0.5"
    assert "info" in result
    assert len(result["info"]) == 1


def test_get_resource_info_by_id_uses_item_endpoint(info_module, mock_client):
    """
    Test that fetching by interface_name builds the item endpoint path.
    """
    info_module.params["interface_name"] = "nic0"

    get_response = MagicMock()
    get_response.status = 200
    get_response.json = {"name": "nic0", "status": "up"}
    mock_client.get.return_value = get_response

    info_module.get_resource_info()

    mock_client.get.assert_called_once()
    called_path = mock_client.get.call_args[0][0]
    assert called_path == "/appliance/networking/interfaces/nic0"


def test_get_resource_info_not_found(info_module, mock_client):
    """
    Test getting an interface that doesn't exist (404).
    """
    info_module.params["interface_name"] = "nic-missing"

    get_response = MagicMock()
    get_response.status = 404
    mock_client.get.return_value = get_response

    result = info_module.get_resource_info()

    # Info modules return empty results when resource not found
    assert "info" in result
    assert len(result["info"]) == 0
    assert result["value"] == {}


# ============================================================================
# get_resource_info() Tests - LIST all
# ============================================================================


def test_get_resource_info_list_all(info_module, mock_client):
    """
    Test listing all interfaces when interface_name is not provided.
    """
    list_response = MagicMock()
    list_response.status = 200
    list_response.json = [
        {"name": "nic0", "status": "up", "mac": "00:50:56:01:02:03"},
        {"name": "nic1", "status": "down", "mac": "00:50:56:01:02:04"},
        {"name": "nic2", "status": "up", "mac": "00:50:56:01:02:05"},
    ]
    mock_client.get.return_value = list_response

    result = info_module.get_resource_info()

    assert "info" in result
    assert len(result["info"]) == 3
    assert result["info"][0]["name"] == "nic0"
    assert result["info"][1]["name"] == "nic1"
    assert result["info"][2]["name"] == "nic2"
    # List results are only fetched from the collection endpoint
    mock_client.get.assert_called_once()
    assert mock_client.get.call_args[0][0] == "/appliance/networking/interfaces"


def test_get_resource_info_list_empty(info_module, mock_client):
    """
    Test listing when no interfaces exist.
    """
    list_response = MagicMock()
    list_response.status = 200
    list_response.json = []
    mock_client.get.return_value = list_response

    result = info_module.get_resource_info()

    assert "info" in result
    assert len(result["info"]) == 0


def test_get_resource_info_list_single_resource(info_module, mock_client):
    """
    Test listing when only one interface exists.
    """
    list_response = MagicMock()
    list_response.status = 200
    list_response.json = [
        {"name": "nic0", "status": "up"},
    ]
    mock_client.get.return_value = list_response

    result = info_module.get_resource_info()

    assert "info" in result
    assert len(result["info"]) == 1
    assert result["info"][0]["name"] == "nic0"


def test_get_resource_info_list_on_404(info_module, mock_client):
    """
    Test listing when the collection endpoint returns 404.
    """
    list_response = MagicMock()
    list_response.status = 404
    mock_client.get.return_value = list_response

    result = info_module.get_resource_info()

    assert "info" in result
    assert len(result["info"]) == 0


# ============================================================================
# normalize_info_results() Tests
# ============================================================================


def test_normalize_info_results_single_resource_with_moid(info_module):
    """
    Test normalize_info_results with a single resource that carries a MOID.
    """
    resource = {
        "interface_name": "nic0",
        "name": "nic0",
        "status": "up",
    }

    result = info_module.normalize_info_results(
        query_results=[resource], single_resource=True
    )

    assert result["id"] == "nic0"
    assert "value" in result
    assert result["value"]["name"] == "nic0"
    assert "info" in result
    assert len(result["info"]) == 1


def test_normalize_info_results_single_resource_without_moid(info_module):
    """
    Test normalize_info_results with a single resource missing a MOID attribute.
    """
    resource = {"name": "nic0", "status": "up"}

    result = info_module.normalize_info_results(
        query_results=[resource], single_resource=True
    )

    # No recognizable MOID attribute means no id key
    assert "id" not in result
    assert result["value"]["name"] == "nic0"
    assert len(result["info"]) == 1


def test_normalize_info_results_multiple_resources(info_module):
    """
    Test normalize_info_results with multiple resources.
    """
    resources = [
        {"name": "nic0", "status": "up"},
        {"name": "nic1", "status": "down"},
    ]

    result = info_module.normalize_info_results(
        query_results=resources, single_resource=False
    )

    assert "info" in result
    assert len(result["info"]) == 2
    # For listings, value preserves the list shape and there is no single id
    assert result["value"] == resources
    assert "id" not in result


def test_normalize_info_results_empty_list(info_module):
    """
    Test normalize_info_results with an empty list.
    """
    result = info_module.normalize_info_results(query_results=[], single_resource=True)

    assert "info" in result
    assert len(result["info"]) == 0
    assert result["value"] == {}


# ============================================================================
# Check Mode Tests
# ============================================================================


def test_get_resource_info_check_mode_get(info_module, mock_client):
    """
    Test getting an interface in check mode (read-only, executes normally).
    """
    info_module.params["interface_name"] = "nic0"
    info_module.module.check_mode = True

    get_response = MagicMock()
    get_response.status = 200
    get_response.json = {"name": "nic0", "status": "up"}
    mock_client.get.return_value = get_response

    result = info_module.get_resource_info()

    assert result["value"]["name"] == "nic0"
    mock_client.get.assert_called_once()


def test_get_resource_info_check_mode_list(info_module, mock_client):
    """
    Test listing interfaces in check mode (read-only, executes normally).
    """
    info_module.module.check_mode = True

    list_response = MagicMock()
    list_response.status = 200
    list_response.json = [
        {"name": "nic0", "status": "up"},
        {"name": "nic1", "status": "down"},
    ]
    mock_client.get.return_value = list_response

    result = info_module.get_resource_info()

    assert len(result["info"]) == 2
    mock_client.get.assert_called_once()


# ============================================================================
# OperationConfig Tests
# ============================================================================


def test_operation_config_build_path_for_get():
    """
    Test that the GET OperationConfig builds the item path with the identifier.
    """
    config = OperationConfig(
        name="get",
        uri=ITEM_ENDPOINT,
        http_method="GET",
    )

    path = config.build_path({"interface_name": "nic0"})

    assert path == "/appliance/networking/interfaces/nic0"


def test_operation_config_build_path_for_get_missing_param():
    """
    Test that the GET OperationConfig raises when the identifier is missing.
    """
    config = OperationConfig(
        name="get",
        uri=ITEM_ENDPOINT,
        http_method="GET",
    )

    with pytest.raises(RequiredPathParameterError):
        config.build_path({})


def test_operation_config_build_path_for_list():
    """
    Test that the LIST OperationConfig returns the static collection path.
    """
    config = OperationConfig(
        name="list",
        uri=LIST_ENDPOINT,
        http_method="GET",
    )

    assert config.build_path({}) == "/appliance/networking/interfaces"


def test_operation_config_build_query_no_spec():
    """
    Test that operations without a query spec build no query parameters.
    """
    config = OperationConfig(
        name="list",
        uri=LIST_ENDPOINT,
        http_method="GET",
    )

    assert config.build_query({"interface_name": "nic0"}) is None


# ============================================================================
# _perform_get_operation() / _perform_list_operation() Tests
# ============================================================================


def test_perform_get_operation(info_module, mock_client):
    """
    Test the base _perform_get_operation method.
    """
    info_module.params["interface_name"] = "nic0"

    get_response = MagicMock()
    get_response.status = 200
    get_response.json = {"name": "nic0", "status": "up"}
    mock_client.get.return_value = get_response

    result = info_module._perform_get_operation()

    assert result is not None
    assert result["name"] == "nic0"


def test_perform_get_operation_not_found(info_module, mock_client):
    """
    Test _perform_get_operation when the interface doesn't exist.
    """
    info_module.params["interface_name"] = "nic-missing"

    get_response = MagicMock()
    get_response.status = 404
    mock_client.get.return_value = get_response

    result = info_module._perform_get_operation()

    assert result is None


def test_perform_get_operation_missing_identifier_raises(info_module):
    """
    Test _perform_get_operation raises when the path identifier is missing.
    """
    with pytest.raises(RequiredPathParameterError):
        info_module._perform_get_operation()


def test_perform_list_operation(info_module, mock_client):
    """
    Test the base _perform_list_operation method.
    """
    list_response = MagicMock()
    list_response.status = 200
    list_response.json = [
        {"name": "nic0", "status": "up"},
        {"name": "nic1", "status": "down"},
    ]
    mock_client.get.return_value = list_response

    result = info_module._perform_list_operation()

    assert len(result) == 2
    assert result[0]["name"] == "nic0"


def test_perform_list_operation_404(info_module, mock_client):
    """
    Test _perform_list_operation returns an empty list on 404.
    """
    list_response = MagicMock()
    list_response.status = 404
    mock_client.get.return_value = list_response

    result = info_module._perform_list_operation()

    assert result == []
