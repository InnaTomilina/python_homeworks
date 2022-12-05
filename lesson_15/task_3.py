CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_number = 0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, number: int):
        self.current_channel_number = number - 1

        return self.current_channel()

    def next_channel(self):
        self.current_channel_number += 1

        if self.current_channel_number >= len(self.channels):
            self.current_channel_number = 0

        return self.current_channel()

    def previous_channel(self):
        self.current_channel_number -= 1

        if self.current_channel_number > 0:
            self.current_channel_number = len(self.channels)

        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_number]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return 'Yes' if 0 < channel < len(self.channels) - 1 else 'No'

        return 'Yes' if channel in self.channels else 'No'


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
