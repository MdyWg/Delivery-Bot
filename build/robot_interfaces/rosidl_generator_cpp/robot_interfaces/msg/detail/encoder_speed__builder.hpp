// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:msg/EncoderSpeed.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robot_interfaces/msg/encoder_speed.hpp"


#ifndef ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__BUILDER_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/msg/detail/encoder_speed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace msg
{

namespace builder
{

class Init_EncoderSpeed_right_speed
{
public:
  explicit Init_EncoderSpeed_right_speed(::robot_interfaces::msg::EncoderSpeed & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::msg::EncoderSpeed right_speed(::robot_interfaces::msg::EncoderSpeed::_right_speed_type arg)
  {
    msg_.right_speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::msg::EncoderSpeed msg_;
};

class Init_EncoderSpeed_left_speed
{
public:
  Init_EncoderSpeed_left_speed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EncoderSpeed_right_speed left_speed(::robot_interfaces::msg::EncoderSpeed::_left_speed_type arg)
  {
    msg_.left_speed = std::move(arg);
    return Init_EncoderSpeed_right_speed(msg_);
  }

private:
  ::robot_interfaces::msg::EncoderSpeed msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::msg::EncoderSpeed>()
{
  return robot_interfaces::msg::builder::Init_EncoderSpeed_left_speed();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__BUILDER_HPP_
