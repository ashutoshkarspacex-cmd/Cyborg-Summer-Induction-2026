#!/usr/bin/env python3

# Write your server implementation here.

import rclpy
from rclpy.node import Node
from task3.srv import PrimeFactors

class server(Node):
    def __init__(self):
      super().__init__('Prime_factor_server')
      self.srv=self.create_service(PrimeFactors,'Find_prime_factors',self.Prime_finder_callback)
      self.get_logger.info("Prime factorization starting....")
      self.counter=0
    def Prime_finder_callback(self, request, response):  
       num=request.number
       Prime_factors=[]
       for i in range(2,num//2): #first to check whether number is prime or not
          if num%i==0:
             self.counter=1
             break
          i+=1

       if self.counter==0:
          Prime_factors.append(num)      

       for i in range(2,num//2):
          if num%i==0:
             for j in range(2, i):
                if i%j==0 and i//j!=1:
                   self.counter=1
                   break
          if self.counter==0:
             Prime_factors.append(i)
          else:            
             self.counter=0  

       response.factors = factors_list
       self.get_logger().info(f'Returning response factors: {Prime_factors}')
       return response    
def main(args=None):
    rclpy.init(args=args)
    node=server()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
 
    

        



       
             
       
             


       

