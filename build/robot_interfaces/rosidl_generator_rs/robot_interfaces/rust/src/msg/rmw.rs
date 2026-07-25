#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "robot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__robot_interfaces__msg__EncoderSpeed() -> *const std::ffi::c_void;
}

#[link(name = "robot_interfaces__rosidl_generator_c")]
extern "C" {
    fn robot_interfaces__msg__EncoderSpeed__init(msg: *mut EncoderSpeed) -> bool;
    fn robot_interfaces__msg__EncoderSpeed__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<EncoderSpeed>, size: usize) -> bool;
    fn robot_interfaces__msg__EncoderSpeed__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<EncoderSpeed>);
    fn robot_interfaces__msg__EncoderSpeed__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<EncoderSpeed>, out_seq: *mut rosidl_runtime_rs::Sequence<EncoderSpeed>) -> bool;
}

// Corresponds to robot_interfaces__msg__EncoderSpeed
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EncoderSpeed {

    // This member is not documented.
    #[allow(missing_docs)]
    pub left_speed: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub right_speed: f64,

}



impl Default for EncoderSpeed {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !robot_interfaces__msg__EncoderSpeed__init(&mut msg as *mut _) {
        panic!("Call to robot_interfaces__msg__EncoderSpeed__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for EncoderSpeed {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robot_interfaces__msg__EncoderSpeed__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robot_interfaces__msg__EncoderSpeed__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { robot_interfaces__msg__EncoderSpeed__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for EncoderSpeed {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for EncoderSpeed where Self: Sized {
  const TYPE_NAME: &'static str = "robot_interfaces/msg/EncoderSpeed";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__robot_interfaces__msg__EncoderSpeed() }
  }
}


