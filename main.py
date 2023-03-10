import pyxel
from random import randint


class App:
    def __init__(self):
        self.points = 0
        self.life = 50
        self.buttons = []
        self.text = ''
        self.game_state = 0
        self.start_frame = 0

        pyxel.init(72, 132, 'Kill the keys', display_scale=3)
        pyxel.load('assets.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        pos_on_press = 0
        life_sum = 0

        if self.game_state == 0 and pyxel.btnp(pyxel.KEY_RETURN):
            self.game_state = 1
            self.start_frame = pyxel.frame_count
            self.add_button()
            self.points = 0
        elif self.game_state == 1:
            if (pyxel.frame_count - self.start_frame) % 15 == 0:
                self.add_button()

            if self.buttons[0]['posy'] >= 120:
                self.buttons = self.buttons[1:]
                self.text = 'MISS'
                life_sum = -4

            for btn in self.buttons:
                if btn['posy'] >= 104 and btn['posy'] < 120:
                    if (
                        pyxel.btn(pyxel.KEY_A) and btn['sprite'] == 1 or
                        pyxel.btn(pyxel.KEY_S) and btn['sprite'] == 2 or
                        pyxel.btn(pyxel.KEY_D) and btn['sprite'] == 3 or
                        pyxel.btn(pyxel.KEY_F) and btn['sprite'] == 4
                    ):
                        pos_on_press = btn['posy']
                        self.buttons = self.buttons[1:]

            if pos_on_press >= 0:
                if pos_on_press >= 111 and pos_on_press <= 113:
                    self.text = 'PERFECT'
                    life_sum = 4
                    self.points += 20
                elif (
                    (pos_on_press < 111 and pos_on_press >= 109) or
                    (pos_on_press > 113 and pos_on_press <= 115)
                ):
                    self.text = 'GREAT'
                    life_sum = 2
                    self.points += 10
                elif (
                    (pos_on_press < 109 and pos_on_press >= 107) or
                    (pos_on_press > 115 and pos_on_press <= 117)
                ):
                    self.text = 'GOOD'
                    life_sum = -2
                    self.points += 5

                pos_on_press = 0
                if self.life < 100:
                    self.life += life_sum

                if self.life <= 0:
                    self.game_state = 2

        elif self.game_state == 2 and pyxel.btnp(pyxel.KEY_RETURN):
            self.game_state = 0

    def draw(self):
        pyxel.cls(0)

        if self.game_state == 0:
            pyxel.text(10, 32, 'KILL THE KEYS', 3)
            pyxel.text(8, 44, '1 HOUR VERSION', 3)
            pyxel.text(14, 64, 'PRESS ENTER', 7)
        elif self.game_state == 1:
            pyxel.bltm(0, 0, 0, 0, 0, 72, 132)
            pyxel.text(8, 8, self.text, 1)

            for btn in self.buttons:
                pyxel.blt(
                    (16 * btn['sprite']) - 8,
                    btn['posy'],
                    0,
                    btn['sprite'] * 8,
                    8,
                    8,
                    8,
                    0
                )
                btn['posy'] += 2

            pyxel.text(11, 120, 'A', 7)
            pyxel.text(27, 120, 'S', 7)
            pyxel.text(43, 120, 'D', 7)
            pyxel.text(59, 120, 'F', 7)

            life_bar_size = int((32 * self.life) / 100)
            pyxel.rect(32, 8, life_bar_size, 4, 11)
            pyxel.rectb(32, 8, 32, 4, 3)
        elif self.game_state == 2:
            pyxel.text(18, 32, 'GAME OVER', 8)
            pyxel.text(24, 44, str(self.points), 8)

    def add_button(self):
        sprite = randint(1, 4)
        self.buttons.append({
            'sprite': sprite,
            'posy': -32
        })


App()
