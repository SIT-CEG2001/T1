#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class OpenLoopSquare(Node):
    def __init__(self):
        super().__init__('open_loop_square')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def move_straight(self, speed, duration):
        msg = Twist()
        msg.linear.x = speed
        end_time = time.time() + duration
        while time.time() < end_time:
            self.publisher_.publish(msg)
            time.sleep(0.1)  # 10 Hz publish rate

    def rotate(self, angular_speed, duration):
        msg = Twist()
        msg.angular.z = angular_speed
        end_time = time.time() + duration
        while time.time() < end_time:
            self.publisher_.publish(msg)
            time.sleep(0.1)

    def run_square(self):
        for _ in range(4):
            self.move_straight(1.0, 2.0)   # 2 s at 1 m/s ≈ 2 m
            self.rotate(1.57, 1.0)         # 1 s at 1.57 rad/s ≈ 90°
        # send a zero‑velocity message to stop
        self.publisher_.publish(Twist())

def main(args=None):
    rclpy.init(args=args)
    node = OpenLoopSquare()
    node.run_square()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
