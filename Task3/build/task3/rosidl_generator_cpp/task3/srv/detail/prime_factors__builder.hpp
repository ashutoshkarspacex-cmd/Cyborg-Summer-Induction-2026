// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from task3:srv/PrimeFactors.idl
// generated code does not contain a copyright notice

#ifndef TASK3__SRV__DETAIL__PRIME_FACTORS__BUILDER_HPP_
#define TASK3__SRV__DETAIL__PRIME_FACTORS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "task3/srv/detail/prime_factors__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace task3
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::task3::srv::PrimeFactors_Request>()
{
  return ::task3::srv::PrimeFactors_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace task3


namespace task3
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::task3::srv::PrimeFactors_Response>()
{
  return ::task3::srv::PrimeFactors_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace task3

#endif  // TASK3__SRV__DETAIL__PRIME_FACTORS__BUILDER_HPP_
