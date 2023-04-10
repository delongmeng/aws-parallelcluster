# Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.
import pytest

from pcluster.config.cluster_config import CloudWatchLogs, LogRotation, Logs
from pcluster.validators.monitoring_validators import DetailedMonitoringValidator, LogRotationValidator
from tests.pcluster.validators.utils import assert_failure_messages


@pytest.mark.parametrize(
    "logs, expected_message",
    [
        (Logs(cloud_watch=CloudWatchLogs(enabled=True), rotation=LogRotation(enabled=True)), None),
        (Logs(cloud_watch=CloudWatchLogs(enabled=False), rotation=LogRotation(enabled=False)), None),
        (Logs(rotation=LogRotation(enabled=False)), None),
        (Logs(rotation=LogRotation(enabled=True)), None),
        (
            Logs(cloud_watch=CloudWatchLogs(enabled=False), rotation=LogRotation(enabled=True)),
            "Cloudwatch Logging is disabled but Log Rotation is enabled. Logs will be rotated and removed from the "
            "cluster once they reach a certain size. If you want to keep logs locally within the cluster, please "
            "set `Monitoring / Logs / Rotation / Enabled` to false.",
        ),
    ],
)
def test_compute_console_logging_validator(logs, expected_message):
    actual_failures = LogRotationValidator().execute(logs)
    assert_failure_messages(actual_failures, expected_message)


@pytest.mark.parametrize(
    "is_detailed_monitoring_enabled, expected_message",
    [
        (False, None),
        (
            True,
            "Detailed Monitoring is enabled for EC2 instances in your compute fleet. The Amazon EC2 console will "
            "display monitoring graphs with a 1-minute period for these instances. Note that this will increase "
            "the cost. If you want to avoid this and use basic monitoring instead, please set "
            "`Monitoring / EnableDetailedMonitoring` to false.",
        ),
    ],
)
def test_detailed_monitoring_validator(is_detailed_monitoring_enabled, expected_message):
    actual_failures = DetailedMonitoringValidator().execute(is_detailed_monitoring_enabled)
    assert_failure_messages(actual_failures, expected_message)
