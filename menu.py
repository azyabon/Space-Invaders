from pygame import *


class Menu:
    def __init__(self):
        self._option_surface = []
        self._callbacks = []
        self._current_option_index = 0
        self.ARIAL_50 = font.SysFont("arial", 50)

    def append_option(self, option, callback):
        self._option_surface.append(self.ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surface) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 0, 255), option_rect)
            surf.blit(option, option_rect)