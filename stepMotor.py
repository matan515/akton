from gpiozero import OutputDevice;
from time import sleep;

class stepMotor:

    def __int__(self,IN1_ID,IN2_ID,IN3_ID,IN4_ID):
        self.IN1 = OutputDevice(IN1_ID)
        self.IN2 = OutputDevice(IN2_ID)
        self.IN3 = OutputDevice(IN3_ID)
        self.IN4 = OutputDevice(IN4_ID)

        self.pins = [self.IN1, self.IN2, self.IN3, self.IN4]

        self.step_sequence = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]

        def step_forward(self, steps, delay =0.005):
            for _ in range(steps):
                for step in self.step_sequnence:
                    self._set_pins(step)
                    sleep(delay)

        def step_backward(self, steps, delay =0.005):
                    for _ in range(steps):
                        for step in reversed(self.step_sequence):
                            self._set_pins(step)
                            sleep(delay)


        def stop(self):
             for pin in self.pins:
                  pin.off()