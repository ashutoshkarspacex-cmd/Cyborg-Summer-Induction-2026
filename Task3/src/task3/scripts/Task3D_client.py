#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from task3.srv import PrimeFactors
from functools import partial

class client(Node):
    def __init__(self):
      super().__init__('Prime_factor_client')
      self.client= self.create_client(PrimeFactors,'Find_prime_factors')

      while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for service....')
      self.num(65)      

    def num(self,num):
      request=PrimeFactors.Request()
      request.number=self.num
      future = client.call_async(request)
      future.add_done_callback(partial(self.callback_prime_factors))
    def callback_prime_factors(self,future):
        try:
            response=future.result()
        except Exception as e:
            self.get_logger().error(f"Service call not processed {e}") 
def main(args=None):
    rclpy.init(args=args)
    node=client()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()

            

   
