// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robot_interfaces:msg/EncoderSpeed.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robot_interfaces/msg/detail/encoder_speed__functions.h"
#include "robot_interfaces/msg/detail/encoder_speed__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace robot_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void EncoderSpeed_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robot_interfaces::msg::EncoderSpeed(_init);
}

void EncoderSpeed_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robot_interfaces::msg::EncoderSpeed *>(message_memory);
  typed_message->~EncoderSpeed();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember EncoderSpeed_message_member_array[2] = {
  {
    "left_speed",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interfaces::msg::EncoderSpeed, left_speed),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "right_speed",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interfaces::msg::EncoderSpeed, right_speed),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers EncoderSpeed_message_members = {
  "robot_interfaces::msg",  // message namespace
  "EncoderSpeed",  // message name
  2,  // number of fields
  sizeof(robot_interfaces::msg::EncoderSpeed),
  false,  // has_any_key_member_
  EncoderSpeed_message_member_array,  // message members
  EncoderSpeed_init_function,  // function to initialize message memory (memory has to be allocated)
  EncoderSpeed_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t EncoderSpeed_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &EncoderSpeed_message_members,
  get_message_typesupport_handle_function,
  &robot_interfaces__msg__EncoderSpeed__get_type_hash,
  &robot_interfaces__msg__EncoderSpeed__get_type_description,
  &robot_interfaces__msg__EncoderSpeed__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace robot_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_interfaces::msg::EncoderSpeed>()
{
  return &::robot_interfaces::msg::rosidl_typesupport_introspection_cpp::EncoderSpeed_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_interfaces, msg, EncoderSpeed)() {
  return &::robot_interfaces::msg::rosidl_typesupport_introspection_cpp::EncoderSpeed_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
