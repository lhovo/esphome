import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_CHANNEL, CONF_ID
from . import TLC95116Output, tlc95116_ns

DEPENDENCIES = ["tlc95116"]

TLC95116Channel = tlc95116_ns.class_("TLC95116Channel", output.FloatOutput)
CONF_TLC95116_ID = "tlc95116_id"

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.Required(CONF_ID): cv.declare_id(TLC95116Channel),
        cv.GenerateID(CONF_TLC95116_ID): cv.use_id(TLC95116Output),
        cv.Required(CONF_CHANNEL): cv.int_range(min=0, max=15),
    }
)


async def to_code(config):
    paren = await cg.get_variable(config[CONF_TLC95116_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_channel(config[CONF_CHANNEL]))
    cg.add(paren.register_channel(var))
    await output.register_output(var, config)
