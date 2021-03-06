import os
import unittest
from ._compat import patch

from click.testing import CliRunner

from xnup.management import upload, download

directory = os.path.dirname(os.path.abspath(__file__))


class TestUpload(unittest.TestCase):

    @patch('xnup.management.default_config')
    @patch('xnup.management.Client')
    def test_upload(self, m1, m2):
        test_file = os.path.join(directory, 'test_management.py')
        runner = CliRunner()
        result = runner.invoke(upload, [test_file])
        self.assertEqual(result.exit_code, 0)
        m1.assert_called_once()
        m1.return_value.send_files.assert_called_once()

    @patch('xnup.management.default_config')
    @patch('xnup.management.Client')
    def test_exclusive(self, m1, m2):
        runner = CliRunner()
        result = runner.invoke(upload, ['missing_file.txt', '--thumbnail-file', 'cara128.png', '--no-thumbnail'])
        self.assertEqual(result.exit_code, 2)
        m1.return_value.send_files.assert_not_called()


class TestDownload(unittest.TestCase):
    @patch('xnup.management.default_config')
    @patch('xnup.management.Client')
    def test_download(self, m1, m2):
        runner = CliRunner()
        result = runner.invoke(download, [])
        self.assertEqual(result.exit_code, 0)
        m1.assert_called_once()
        m1.return_value.download_files.assert_called_once()
