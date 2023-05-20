import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import LaserScan
from math import pi

from lidar_interfaces.srv import GetPos
from lidar_interfaces.msg import PolarCoordinate
from lidar_interfaces.msg import Position

class Lidar(Node):

    def __init__(self):
        super().__init__('lidarsub')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            qos_profile_sensor_data) #QoS value must be same as Publisher
        self.subscription  # prevent unused variable warning
        self.angle_ranges = Position()
        self.srv = self.create_service(GetPos, 'get_angle_range', self.service_callbacK)

    def listener_callback(self, msg):
        header = msg.header
        angle_min = msg.angle_min
        angle_max = msg.angle_max
        angle_increment = msg.angle_increment
        time_increment = msg.time_increment
        scan_time = msg.scan_time
        range_min = msg.range_min
        range_max = msg.range_max
        ranges = msg.ranges

        angle_ranges = []
        count = int(scan_time/time_increment)
        for i in range(0,count):
            deg = self.rad2deg(angle_min + angle_increment * i)
            data = PolarCoordinate()
            data.deg = deg
            data.range = ranges[i]
            angle_ranges.append(data)

        self.angle_ranges.ranges = angle_ranges

    def rad2deg(self, rad):
        return (rad * 180)/(pi)
    
    def service_callbacK(self, req, res):
        print("I receive request")
        res.ranges = self.angle_ranges
        return res


def main(args=None):
    rclpy.init(args=args)

    lidar = Lidar()

    rclpy.spin(lidar)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rclpy.shutdown()


if __name__ == '__main__':
    main()