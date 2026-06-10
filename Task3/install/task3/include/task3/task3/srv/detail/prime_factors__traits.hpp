// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from task3:srv/PrimeFactors.idl
// generated code does not contain a copyright notice

#ifndef TASK3__SRV__DETAIL__PRIME_FACTORS__TRAITS_HPP_
#define TASK3__SRV__DETAIL__PRIME_FACTORS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "task3/srv/detail/prime_factors__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace task3
{

namespace srv
{

inline void to_flow_style_yaml(
  const PrimeFactors_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PrimeFactors_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PrimeFactors_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace task3

namespace rosidl_generator_traits
{

[[deprecated("use task3::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task3::srv::PrimeFactors_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  task3::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task3::srv::to_yaml() instead")]]
inline std::string to_yaml(const task3::srv::PrimeFactors_Request & msg)
{
  return task3::srv::to_yaml(msg);
}

template<>
inline const char * data_type<task3::srv::PrimeFactors_Request>()
{
  return "task3::srv::PrimeFactors_Request";
}

template<>
inline const char * name<task3::srv::PrimeFactors_Request>()
{
  return "task3/srv/PrimeFactors_Request";
}

template<>
struct has_fixed_size<task3::srv::PrimeFactors_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<task3::srv::PrimeFactors_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<task3::srv::PrimeFactors_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace task3
{

namespace srv
{

inline void to_flow_style_yaml(
  const PrimeFactors_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PrimeFactors_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PrimeFactors_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace task3

namespace rosidl_generator_traits
{

[[deprecated("use task3::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const task3::srv::PrimeFactors_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  task3::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use task3::srv::to_yaml() instead")]]
inline std::string to_yaml(const task3::srv::PrimeFactors_Response & msg)
{
  return task3::srv::to_yaml(msg);
}

template<>
inline const char * data_type<task3::srv::PrimeFactors_Response>()
{
  return "task3::srv::PrimeFactors_Response";
}

template<>
inline const char * name<task3::srv::PrimeFactors_Response>()
{
  return "task3/srv/PrimeFactors_Response";
}

template<>
struct has_fixed_size<task3::srv::PrimeFactors_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<task3::srv::PrimeFactors_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<task3::srv::PrimeFactors_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<task3::srv::PrimeFactors>()
{
  return "task3::srv::PrimeFactors";
}

template<>
inline const char * name<task3::srv::PrimeFactors>()
{
  return "task3/srv/PrimeFactors";
}

template<>
struct has_fixed_size<task3::srv::PrimeFactors>
  : std::integral_constant<
    bool,
    has_fixed_size<task3::srv::PrimeFactors_Request>::value &&
    has_fixed_size<task3::srv::PrimeFactors_Response>::value
  >
{
};

template<>
struct has_bounded_size<task3::srv::PrimeFactors>
  : std::integral_constant<
    bool,
    has_bounded_size<task3::srv::PrimeFactors_Request>::value &&
    has_bounded_size<task3::srv::PrimeFactors_Response>::value
  >
{
};

template<>
struct is_service<task3::srv::PrimeFactors>
  : std::true_type
{
};

template<>
struct is_service_request<task3::srv::PrimeFactors_Request>
  : std::true_type
{
};

template<>
struct is_service_response<task3::srv::PrimeFactors_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TASK3__SRV__DETAIL__PRIME_FACTORS__TRAITS_HPP_
