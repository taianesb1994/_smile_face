# https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade

import arcade

# Definir constantes para o tamanho da tela.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Abre a janela. Defina o título e as dimensões da janela (largura e altura).
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Smile Face")

# Defina a cor de fundo como branco.
arcade.set_background_color(arcade.color.WHITE)

# Inicie o processo de renderização. Isso deve ser feito antes de qualquer comando de desenho.
arcade.start_render()

# Desenhe o rosto.
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.PINK)

# Desenhe o olho direito.
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Desenhe o olho esquerdo.
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Desenhe o sorriso.
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# Conclua o desenho e exiba o resultado até o usuário clicar no botão 'Fechar'.
arcade.finish_render()
arcade.run()