from unittest.mock import Mock
from lib.tv import TV

class TestTVWithMocking:
    def setup_method(self):
        self.tv = TV()
        self.mock_remote = Mock()
    
    def test_tv_responds_to_working_remote(self):
        # Configure mock to simulate working remote
        self.mock_remote.press_power_button.return_value = True
        
        # Test TV turning on
        assert self.tv.power_toggle(self.mock_remote) is True
        assert self.tv.is_on is True
        
        # Verify remote button was pressed
        self.mock_remote.press_power_button.assert_called_once()
    
    def test_tv_ignores_dead_remote(self):
        # Configure mock to simulate dead remote
        self.mock_remote.press_power_button.return_value = False
        
        # Test TV response
        assert self.tv.power_toggle(self.mock_remote) is False
        assert self.tv.is_on is False
        
        # Verify remote button was pressed
        self.mock_remote.press_power_button.assert_called_once()