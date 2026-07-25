#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to robot_interfaces__msg__EncoderSpeed

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::EncoderSpeed::default())
  }
}

impl rosidl_runtime_rs::Message for EncoderSpeed {
  type RmwMsg = super::msg::rmw::EncoderSpeed;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        left_speed: msg.left_speed,
        right_speed: msg.right_speed,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      left_speed: msg.left_speed,
      right_speed: msg.right_speed,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      left_speed: msg.left_speed,
      right_speed: msg.right_speed,
    }
  }
}


