import rclpy
from rclpy.node import Node
from serial_motor_demo_msgs.msg import EncoderVals, MotorCommand
import serial
import time

class SerialMotorDriver(Node):
    def __init__(self):
        super().__init__('serial_motor_driver')
        
        # Настройки (ПРОВЕРЬ ПОРТ!)
        self.declare_parameter('serial_port', '/dev/ttyUSB0')
        self.declare_parameter('baud_rate', 115200)
        
        port = self.get_parameter('serial_port').value
        baud = self.get_parameter('baud_rate').value
        
        try:
            self.conn = serial.Serial(port, baud, timeout=1.0)
            self.get_logger().info(f"Connected to Arduino on {port}")
        except Exception as e:
            self.get_logger().error(f"Failed to connect: {e}")
            self.conn = None

        # Публикуем энкодеры
        self.enc_pub = self.create_publisher(EncoderVals, 'encoder_vals', 10)
        
        # Слушаем команды моторов
        self.create_subscription(MotorCommand, 'motor_command', self.motor_command_callback, 10)
        
        # Таймер чтения данных (20 Гц)
        self.timer = self.create_timer(0.05, self.read_encoders)

    def motor_command_callback(self, msg):
        if not self.conn: return
        # Превращаем радианы в условные единицы PWM/Скорости для Arduino
        # Подбери коэффициент scale экспериментально, если едет слишком быстро/медленно
        scale = 50.0 
        left_cmd = int(msg.mot_1_req_rad_sec * scale)
        right_cmd = int(msg.mot_2_req_rad_sec * scale)
        command = f"m {left_cmd} {right_cmd}\r"
        self.conn.write(command.encode())

    def read_encoders(self):
        if not self.conn: return
        try:
            self.conn.write(b'e\r')
            line = self.conn.readline().decode().strip()
            parts = line.split()
            if len(parts) == 2:
                msg = EncoderVals()
                msg.mot_1_enc_val = int(parts[0])
                msg.mot_2_enc_val = int(parts[1])
                self.enc_pub.publish(msg)
        except:
            pass

def main():
    rclpy.init()
    node = SerialMotorDriver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()