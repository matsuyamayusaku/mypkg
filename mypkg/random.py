import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("random")
pub = node.create_publisher(Int16, "num", 10)
n = 0

def cb():
        global n
        msg = Int16()
        msg.data = n
        n = random.randint(1, 100)
        pub.publish(msg)

node.create_timer(0.5, cb)
rclpy.spin(node)
