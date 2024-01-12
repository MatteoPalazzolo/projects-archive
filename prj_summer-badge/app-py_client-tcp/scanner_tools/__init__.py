from scanner_tools.get_user_info import get_user_info
from scanner_tools.read_QR import read_QR
from scanner_tools.save_image import save_image
from scanner_tools.save_authorization import save_authorization
from scanner_tools.update_entries import update_entries
from scanner_tools.speak import play_phrase
from scanner_tools.send_json import send_json
from scanner_tools.image_tools import image_to_bytes, manage_image

#IP = "10.200.60.15"
IP = "192.168.1.11"
PORT = 8080
IMAGE_NAME = 'onetotem.jpg'
ACTIVITIES = ['Altro - free time al Moro', 'Arduino', 'Attualità', 'Boxe', 'Chitarra',
'Difesa personale', 'Film in inglese', 'Flag football', 'Fotografia', 'Fumetto - manga',
'Giochi da tavolo', 'Giornalismo', 'Manutenzioni', 'Murales', 'Music fitness', 'Musica al Moro',
'Riprese ed editing video', 'Robotica', 'Scacchi', 'Spazio di confronto', 'Staff', 'Teatro al moro',
'Teatro improvvisazione', 'Torneo basket', 'Torneo calcio balilla', 'Torneo pallavolo', 'Torneo ping pong']