#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2023 Yusaku Matsuyama
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    qua = msg.data
    for i in range(qua):
        print("あんぱん", end = '')
    print()

rclpy.init()
node = Node("anpan")
pub = node.create_subscription(Int16, "num", cb, 10)
rclpy.spin(node)
