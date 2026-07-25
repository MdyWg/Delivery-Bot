// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from robot_interfaces:msg/EncoderSpeed.idl
// generated code does not contain a copyright notice

#include "robot_interfaces/msg/detail/encoder_speed__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_robot_interfaces
const rosidl_type_hash_t *
robot_interfaces__msg__EncoderSpeed__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xfc, 0xdc, 0xbb, 0xce, 0x60, 0x1b, 0xf0, 0xab,
      0x90, 0xaa, 0xd8, 0x69, 0x07, 0x11, 0xa8, 0xf9,
      0x5b, 0xad, 0xe7, 0x5f, 0x55, 0xc3, 0xc8, 0x6b,
      0xf0, 0x1d, 0xe3, 0x14, 0x66, 0x89, 0x18, 0x79,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char robot_interfaces__msg__EncoderSpeed__TYPE_NAME[] = "robot_interfaces/msg/EncoderSpeed";

// Define type names, field names, and default values
static char robot_interfaces__msg__EncoderSpeed__FIELD_NAME__left_speed[] = "left_speed";
static char robot_interfaces__msg__EncoderSpeed__FIELD_NAME__right_speed[] = "right_speed";

static rosidl_runtime_c__type_description__Field robot_interfaces__msg__EncoderSpeed__FIELDS[] = {
  {
    {robot_interfaces__msg__EncoderSpeed__FIELD_NAME__left_speed, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {robot_interfaces__msg__EncoderSpeed__FIELD_NAME__right_speed, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
robot_interfaces__msg__EncoderSpeed__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {robot_interfaces__msg__EncoderSpeed__TYPE_NAME, 33, 33},
      {robot_interfaces__msg__EncoderSpeed__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 left_speed\n"
  "float64 right_speed";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
robot_interfaces__msg__EncoderSpeed__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {robot_interfaces__msg__EncoderSpeed__TYPE_NAME, 33, 33},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 38, 38},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
robot_interfaces__msg__EncoderSpeed__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *robot_interfaces__msg__EncoderSpeed__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
