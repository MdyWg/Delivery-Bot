// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:msg/EncoderSpeed.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robot_interfaces/msg/encoder_speed.h"


#ifndef ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__STRUCT_H_
#define ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/EncoderSpeed in the package robot_interfaces.
typedef struct robot_interfaces__msg__EncoderSpeed
{
  double left_speed;
  double right_speed;
} robot_interfaces__msg__EncoderSpeed;

// Struct for a sequence of robot_interfaces__msg__EncoderSpeed.
typedef struct robot_interfaces__msg__EncoderSpeed__Sequence
{
  robot_interfaces__msg__EncoderSpeed * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__msg__EncoderSpeed__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__MSG__DETAIL__ENCODER_SPEED__STRUCT_H_
