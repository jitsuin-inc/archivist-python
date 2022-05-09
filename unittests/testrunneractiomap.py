"""
Test runner actionmap
"""
from logging import getLogger
from os import environ
from unittest import TestCase, mock

from archivist.errors import ArchivistInvalidOperationError

# pylint: disable=missing-docstring
# pylint: disable=protected-access
# pylint: disable=unused-variable

from archivist.archivist import Archivist
from archivist.logger import set_logger
from archivist.runner import _ActionMap, Runner

if "TEST_DEBUG" in environ and environ["TEST_DEBUG"]:
    set_logger(environ["TEST_DEBUG"])

LOGGER = getLogger(__name__)


URL = "https://app.rkvst-dev.io"
AUTH_TOKEN = "auth_token"
ARCHIVIST_CREATE = {
    "url": URL,
    "auth_token": AUTH_TOKEN,
    "client_id": "client_id",
    "client_secret": "client_secret",
    "max_time": 257,
    "verify": False,
}


class TestRunnerActionMap(TestCase):
    """
    Test Archivist Runner
    """

    maxDiff = None

    def setUp(self):
        self.arch = Archivist("url", "authauthauth")
        self.actionmap = _ActionMap(self.arch)
        self.runner = Runner(self.arch)

    def tearDown(self):
        self.arch.close()

    def test_runner_actionmap_action(self):
        """
        Test runner action map
        """
        self.assertEqual(
            self.actionmap.action("ASSETS_CREATE"),
            self.arch.assets.create_from_data,
            msg="Incorrect assets create method",
        )

    def test_runner_actionmap_illegal_action(self):
        """
        Test runner action map
        """
        with self.assertRaises(ArchivistInvalidOperationError):
            _ = self.actionmap.action("ASSETSS_CREATE")

    @mock.patch("archivist.runner.type_helper.Archivist")
    @mock.patch("archivist.runner.time_sleep")
    def test_runner_archivist_create(self, mock_sleep, mock_archivist):
        """
        Test runner operation
        """
        self.runner(
            {
                "steps": [
                    {
                        "step": {
                            "action": "ARCHIVIST_CREATE",
                            "wait_time": 10,
                            "description": "Testing runner assets create",
                            "archivist_label": "Archivist",
                        },
                        **ARCHIVIST_CREATE,
                    },
                ],
            }
        )
        args, kwargs = mock_archivist.call_args

        print("args", args)
        print("kwargs", kwargs)
        self.assertEqual(
            args,
            (URL, AUTH_TOKEN),
            msg="Incorrect args in archivist create",
        )
        self.assertEqual(
            kwargs,
            {},
            msg="Incorrect keywords args",
        )
        mock_sleep.assert_called_once_with(10)
