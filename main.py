"Daniel Bronevitsky 404"

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"
COLOR_LIST = [arcade.color.WHITE, arcade.color.GOLD, arcade.color.GREEN, arcade.color.GRAPE, arcade.color.BALL_BLUE]


class Rectangle:
    """Classe pour faire les rectangle, contient tout les atributs des rectangle"""

    def __init__(self, x, y) -> None:
        self.width = random.randrange(10, 60)
        self.height = random.randrange(10, 60)
        self.angle = random.randrange(0, 360)
        self.color = random.choice(COLOR_LIST)
        self.change_x = random.randrange(-5, 5)
        self.change_y = random.randrange(-5, 5)
        if self.change_x == 0:
            self.change_x = 1

        if self.change_y == 0:
            self.change_y = 1

        self.pos_x = x
        self.pos_y = y

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color, self.angle)

    def update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y
        if self.pos_x > SCREEN_WIDTH - self.width:
            self.change_x *= -1

        if self.pos_x < 0 + self.width:
            self.change_x *= -1

        if self.pos_y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1

        if self.pos_y < 0 + self.height:
            self.change_y *= -1


class Circle:
    """Classe pour faire les cercle, contient tout les atributs des cercle"""

    def __init__(self, x, y) -> None:
        self.rayon = random.randrange(10, 30)
        self.color = random.choice(COLOR_LIST)
        self.change_x = random.randrange(-5, 5)
        self.change_y = random.randrange(-5, 5)
        self.pos_x = x
        self.pos_y = y

        if self.change_x == 0:
            self.change_x = 1

        if self.change_y == 0:
            self.change_y = 1

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rayon, self.color)

    def update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y
        if self.pos_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.pos_x < 0 + self.rayon:
            self.change_x *= -1

        if self.pos_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1

        if self.pos_y < 0 + self.rayon:
            self.change_y *= -1


class MyGame(arcade.Window, ):
    """
  La classe principale de l'application

  NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
  Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
  """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.ball_list = []
        self.rectangle_list = []

    def setup(self):
        pass

    def on_draw(self):
        """
      C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
      de votre jeu à l'écran.
      """
        arcade.start_render()
        for self.cercle in self.ball_list:
            self.cercle.draw()

        for self.rectangle in self.rectangle_list:
            self.rectangle.draw()

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".

    def on_update(self, delta_time):
        """
      Toute la logique pour déplacer les objets de votre jeu et de
      simuler sa logique vont ici. Normalement, c'est ici que
      vous allez invoquer la méthode "update()" sur vos listes de sprites.
      Paramètre:
          - delta_time : le nombre de milliseconde depuis le dernier update.
      """
        for self.cercle in self.ball_list:
            self.cercle.update()

        for self.rectangle in self.rectangle_list:
            self.rectangle.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.cercle = Circle(x, y)
            self.ball_list.append(self.cercle)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.rectangle = Rectangle(x, y)
            self.rectangle_list.append(self.rectangle)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
