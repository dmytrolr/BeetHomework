CHANNELS = ["УТ-1", "Місто", "ICTV"]


class TVController():
    def __init__(self, channels):
        self.channels = CHANNELS
        self.current_index = 0  # about 1 chsnnel as defalut

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1  # adaptation for start index 1 (for user)
        return self.channels[self.current_index]

    def change_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_index = n - 1
            return self.channels[self.current_index]
        else:
            return "No"

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, channel):
        if isinstance(channel, int):
            return 1 <= channel <= len(self.channels)
        return channel in self.channels

# controller = TVController(CHANNELS)
#
# print(controller.first_channel())
# print(controller.last_channel())
# print(controller.change_channel(2))
# print(controller.next_channel())
# print(controller.previous_channel())
# print(controller.exists(8))
# print(controller.exists("Місто"))
