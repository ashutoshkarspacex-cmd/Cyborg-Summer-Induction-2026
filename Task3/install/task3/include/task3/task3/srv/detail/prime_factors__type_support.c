// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from task3:srv/PrimeFactors.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "task3/srv/detail/prime_factors__rosidl_typesupport_introspection_c.h"
#include "task3/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "task3/srv/detail/prime_factors__functions.h"
#include "task3/srv/detail/prime_factors__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task3__srv__PrimeFactors_Request__init(message_memory);
}

void task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_fini_function(void * message_memory)
{
  task3__srv__PrimeFactors_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task3__srv__PrimeFactors_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_members = {
  "task3__srv",  // message namespace
  "PrimeFactors_Request",  // message name
  1,  // number of fields
  sizeof(task3__srv__PrimeFactors_Request),
  task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_member_array,  // message members
  task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_type_support_handle = {
  0,
  &task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task3
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors_Request)() {
  if (!task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_type_support_handle.typesupport_identifier) {
    task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task3__srv__PrimeFactors_Request__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "task3/srv/detail/prime_factors__rosidl_typesupport_introspection_c.h"
// already included above
// #include "task3/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "task3/srv/detail/prime_factors__functions.h"
// already included above
// #include "task3/srv/detail/prime_factors__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  task3__srv__PrimeFactors_Response__init(message_memory);
}

void task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_fini_function(void * message_memory)
{
  task3__srv__PrimeFactors_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(task3__srv__PrimeFactors_Response, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_members = {
  "task3__srv",  // message namespace
  "PrimeFactors_Response",  // message name
  1,  // number of fields
  sizeof(task3__srv__PrimeFactors_Response),
  task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_member_array,  // message members
  task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_type_support_handle = {
  0,
  &task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task3
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors_Response)() {
  if (!task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_type_support_handle.typesupport_identifier) {
    task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &task3__srv__PrimeFactors_Response__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "task3/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "task3/srv/detail/prime_factors__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_members = {
  "task3__srv",  // service namespace
  "PrimeFactors",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_Request_message_type_support_handle,
  NULL  // response message
  // task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_Response_message_type_support_handle
};

static rosidl_service_type_support_t task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_type_support_handle = {
  0,
  &task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_task3
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors)() {
  if (!task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_type_support_handle.typesupport_identifier) {
    task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, task3, srv, PrimeFactors_Response)()->data;
  }

  return &task3__srv__detail__prime_factors__rosidl_typesupport_introspection_c__PrimeFactors_service_type_support_handle;
}
