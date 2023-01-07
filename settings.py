WIDTH = 1280
HEIGHT = 720
FPS = 30
TILESIZE = 64

HITBOX_OFFSET = {
    'player':-26,
    'object':-40,
    'grass': -10,
    'invisible':0
}


BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graficos/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

weapon_data = {
    'sword':{'cooldown':100, 'damage':15, 'graphic': 'graficos/armas/sword/full.png'},
    'lance':{'cooldown':400, 'damage':30, 'graphic': 'graficos/armas/lance/full.png'},
    'axe':{'cooldown':300, 'damage':20, 'graphic': 'graficos/armas/axe/full.png'},
    'rapier':{'cooldown':50, 'damage':8, 'graphic': 'graficos/armas/rapier/full.png'},
    'sai':{'cooldown':80, 'damage':10, 'graphic': 'graficos/armas/sai/full.png'},
}

magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'graficos/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'graficos/particles/heal/heal.png'}
    }

monster_data = {
    'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'slime': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'ghost': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}