from lib.remote_control import *
from lib.tv import *

class TestTVWithoutMocking:
    def setup_method(self):
        self.tv = TV()
    
    def test_tv_turns_on(self):
        working_remote = RemoteControl(100)
        assert self.tv.power_toggle(working_remote) is True
        assert self.tv.is_on is True
    
    # This test will fail when RemoteControl.press_power_button logic changes!
    def test_tv_wont_turn_on(self):
        dead_remote = RemoteControl(5)
        assert self.tv.power_toggle(dead_remote) is False
        assert self.tv.is_on is False