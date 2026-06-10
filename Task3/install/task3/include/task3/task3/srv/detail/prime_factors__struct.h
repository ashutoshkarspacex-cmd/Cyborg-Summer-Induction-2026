// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from task3:srv/PrimeFactors.idl
// generated code does not contain a copyright notice

#ifndef TASK3__SRV__DETAIL__PRIME_FACTORS__STRUCT_H_
#define TASK3__SRV__DETAIL__PRIME_FACTORS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/PrimeFactors in the package task3.
typedef struct task3__srv__PrimeFactors_Request
{
  uint8_t structure_needs_at_least_one_member;
} task3__srv__PrimeFactors_Request;

// Struct for a sequence of task3__srv__PrimeFactors_Request.
typedef struct task3__srv__PrimeFactors_Request__Sequence
{
  task3__srv__PrimeFactors_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task3__srv__PrimeFactors_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/PrimeFactors in the package task3.
typedef struct task3__srv__PrimeFactors_Response
{
  uint8_t structure_needs_at_least_one_member;
} task3__srv__PrimeFactors_Response;

// Struct for a sequence of task3__srv__PrimeFactors_Response.
typedef struct task3__srv__PrimeFactors_Response__Sequence
{
  task3__srv__PrimeFactors_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} task3__srv__PrimeFactors_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TASK3__SRV__DETAIL__PRIME_FACTORS__STRUCT_H_
