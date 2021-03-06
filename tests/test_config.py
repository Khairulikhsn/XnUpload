import unittest
from unittest.mock import patch, mock_open

from xnup.config import default_config, CONFIG_FILE


class TestDefaultConfig(unittest.TestCase):
    @patch('xnup.config.os.path.lexists', return_value=True)
    def test_exists(self, m):
        self.assertEqual(default_config(), CONFIG_FILE)
        self.assertEqual(m.call_count, 1)

    @patch('builtins.open', mock_open())
    @patch('xnup.config.os')
    @patch('xnup.config.click')
    @patch('xnup.config.json')
    def test_create(self, m_json, m_click, m_os):
        m_os.path.lexists.return_value = False
        m_click.prompt.side_effect = ['api_id', 'api_hash']
        self.assertEqual(default_config(), CONFIG_FILE)
        self.assertEqual(m_json.dump.call_count, 1)
        self.assertEqual(m_json.dump.call_args[0][0], {'api_id': 'api_id', 'api_hash': 'api_hash'})
