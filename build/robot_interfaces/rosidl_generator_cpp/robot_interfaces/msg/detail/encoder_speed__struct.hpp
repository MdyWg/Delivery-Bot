// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_interfaces:msg/EncoderSpeed.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robot_interfaces/msg/encoder_speed.hpp"


#ifndef ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__STRUCT_HPP_
#define ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robot_interfaces__msg__EncoderSpeed __attribute__((deprecated))
#else
# define DEPRECATED__robot_interfaces__msg__EncoderSpeed __declspec(deprecated)
#endif

namespace robot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct EncoderSpeed_
{
  using Type = EncoderSpeed_<ContainerAllocator>;

  explicit EncoderSpeed_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_speed = 0.0;
      this->right_speed = 0.0;
    }
  }

  explicit EncoderSpeed_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_speed = 0.0;
      this->right_speed = 0.0;
    }
  }

  // field types and members
  using _left_speed_type =
    double;
  _left_speed_type left_speed;
  using _right_speed_type =
    double;
  _right_speed_type right_speed;

  // setters for named parameter idiom
  Type & set__left_speed(
    const double & _arg)
  {
    this->left_speed = _arg;
    return *this;
  }
  Type & set__right_speed(
    const double & _arg)
  {
    this->right_speed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_interfaces::msg::EncoderSpeed_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_interfaces::msg::EncoderSpeed_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_interfaces::msg::EncoderSpeed_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_interfaces::msg::EncoderSpeed_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_interfaces__msg__EncoderSpeed
    std::shared_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_interfaces__msg__EncoderSpeed
    std::shared_ptr<robot_interfaces::msg::EncoderSpeed_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EncoderSpeed_ & other) const
  {
    if (this->left_speed != other.left_speed) {
      return false;
    }
    if (this->right_speed != other.right_speed) {
      return false;
    }
    return true;
  }
  bool operator!=(const EncoderSpeed_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EncoderSpeed_

// alias to use template instance with default allocator
using EncoderSpeed =
  robot_interfaces::msg::EncoderSpeed_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__STRUCT_HPP_
