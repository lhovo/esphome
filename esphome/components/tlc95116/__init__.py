# this component is for the "TLC95116 16-Channel, 8-Bit PWM LED Driver" [https://www.ti.com/lit/ds/symlink/tlc59116.pdf],
# The code is based on the components tlc59208f.

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c"]
MULTI_CONF = True

tlc95116_ns = cg.esphome_ns.namespace("tlc95116")
TLC95116Output = tlc95116_ns.class_("TLC95116Output", cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(TLC95116Output),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x20))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
