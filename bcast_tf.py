import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

class DynTF(Node):
    def __init__(self):
        super().__init__('dyn_tf_broadcaster')
        self.tb = TransformBroadcaster(self)
        self.timer = self.create_timer(0.02, self.on_timer)  # 50 Hz
        self.parent = 'base_link'
        self.child = 'laser_frame'
        self.tx = -0.075
        self.ty = 0.0
        self.tz = 0.215

    def on_timer(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.parent
        t.child_frame_id = self.child
        t.transform.translation.x = self.tx
        t.transform.translation.y = self.ty
        t.transform.translation.z = self.tz
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        self.tb.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = DynTF()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
