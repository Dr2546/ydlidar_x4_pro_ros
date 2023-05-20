from lidar_interfaces.srv import GetPos       # CHANGE
import sys
import rclpy
from rclpy.node import Node


class LidarClientAsync(Node):

    def __init__(self):
        super().__init__('lidar_client_async')
        self.cli = self.create_client(GetPos, 'get_angle_range')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetPos.Request()                                   # CHANGE

    def send_request(self):
        self.req.req = sys.argv[1]                # CHANGE
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    lidar_client = LidarClientAsync()
    lidar_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(lidar_client)
        if lidar_client.future.done():
            try:
                response = lidar_client.future.result()
            except Exception as e:
                print(e)
            else:
                result = response.ranges
                for polar in result.ranges:
                    print(polar.deg,polar.range)
            break

    lidar_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
