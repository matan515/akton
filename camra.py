import cv2

class Camra:

    def __int__(self,camra_id):
        self.camara = cv2.VideoCapture(camra_id)

    def open(self):

        if not self.camera.isOpened():
            print("camra error 1")
            return

        while True:
            ret,frame = self.camera.read()

            if not ret:
                print("camera error 2")
                break

            cv2.imshow("myCamra", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        self.close()

    def close(self):
        self.camera.release()
        cv2.destroyAllWindows()