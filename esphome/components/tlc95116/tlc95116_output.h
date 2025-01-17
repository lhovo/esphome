#pragma once

#include "esphome/core/component.h"
#include "esphome/core/helpers.h"
#include "esphome/components/output/float_output.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace tlc95116 {

// 0*: Group dimming, 1: Group blinking
extern const uint8_t TLC95116_MODE2_DMBLNK;
// 0*: Output change on Stop command, 1: Output change on ACK
extern const uint8_t TLC95116_MODE2_OCH;

class TLC95116Output;

class TLC95116Channel : public output::FloatOutput, public Parented<TLC95116Output> {
 public:
  void set_channel(uint8_t channel) { channel_ = channel; }

 protected:
  friend class TLC95116Output;

  void write_state(float state) override;

  uint8_t channel_;
};

/// TLC95116 float output component.
class TLC95116Output : public Component, public i2c::I2CDevice {
 public:
  TLC95116Output(uint8_t mode = TLC95116_MODE2_OCH) : mode_(mode) {}

  void register_channel(TLC95116Channel *channel);

  void setup() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::HARDWARE; }
  void loop() override;

 protected:
  friend TLC95116Channel;

  void set_channel_value_(uint8_t channel, uint8_t value) {
    if (this->pwm_amounts_[channel] != value)
      this->update_ = true;
    this->pwm_amounts_[channel] = value;
  }

  uint8_t mode_;

  uint8_t min_channel_{0xFF};
  uint8_t max_channel_{0x00};
  uint8_t pwm_amounts_[256] = {
      0,
  };
  bool update_{true};
};

}  // namespace tlc95116
}  // namespace esphome
