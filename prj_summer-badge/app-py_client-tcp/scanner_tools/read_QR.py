################# IMPORT #################
import cv2
from pyzbar.pyzbar import decode

################# DEF #################
def read_QR() -> str:
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        frame = cap.read()[1]
        for code in decode(frame):
            code_data = code.data.decode("utf-8")
            return code_data

################# CODE #################
if __name__ ==  "__main__":
    print(read_QR())
