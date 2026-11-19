import stepMotor
import camra

motorLeft = stepMotor(0,0,0,0)
motorRight = stepMotor(0,0,0,0)

def forward():
    motorLeft.step_forward(50)
    motorRight.step_forward(50)

def BackWard():
    motorLeft.step_backward(50)
    motorRight.step_backward(50)

def right():
    motorLeft.step_forward(50)
    motorRight.step_backward(50)

def left():
    motorLeft.step_backward(50)
    motorRight.step_forward(50)\

def main():
    forward()
    forward()
    right()
    BackWard()
    BackWard()
    cameraLefr = camra.Camera(0)
    cameraRight = camra.Camera(1)
    cameraLefr.open()
    cameraRight.open()

if __name__ =="__main__":
    main()