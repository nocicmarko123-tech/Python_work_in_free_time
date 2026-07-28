import pygame as pg
pg.init()
prozor=pg.display.set_mode((400,400))
prozor.fill(pg.Color("White"))
pg.draw.triangle(prozor, pg.Color("Yellow"), (166,333), (100,166), (233,166))
pg.draw.circle(prozor, pg.Color(204, 222, 227), (166, 150), 33)
pg.draw.circle(prozor, pg.Color(255, 102, 102), (200, 166), 33)
pg.draw.circle(prozor, pg.Color(182, 219, 140), (100, 66), 33)
pg.display.update()
while pg.event.wait().type != pg.quit:
  pass
pg.quit()
