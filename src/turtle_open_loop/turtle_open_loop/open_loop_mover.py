import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class OpenLoopMover(Node):
    def __init__(self):
        super().__init__('open_loop_mover')
        # Publisher sends Twist messages on the cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        # Set constant velocities; students can adjust these numbers
        self.linear_speed = 2.0
        self.angular_speed = 0.0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.linear_speed
        msg.angular.z = self.angular_speed
        self.publisher_.publish(msg)
        # Optional: print to console so you know it’s running
        self.get_logger().info(f'Publishing linear {msg.linear.x} angular {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = OpenLoopMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
