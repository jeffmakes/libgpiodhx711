from cffi import FFI
import path

ffibuilder = FFI()

c_path = path.Path("../c").abspath()
c_build_path = c_path.joinpath("build")
hx_lib_path = c_build_path.joinpath("libgpiodhx711.a")
hx_include_path = c_path.joinpath("include")


ffibuilder.set_source(
    "_gpiodhx711",
    """
    #include <gpiodhx711.h>
    """,
    extra_objects=[hx_lib_path],
    include_dirs=[hx_include_path],
)

ffibuilder.cdef("""
typedef struct hx711_handle_t 
{
    struct gpiod_chip *chip;
	struct gpiod_line *pd_sck;
	struct gpiod_line *dout;
    int32_t gain;
	int32_t offset;
	float scale;
} hx711_handle_t;
hx711_handle_t* hx711_init(uint32_t gpio_pd_sck, uint32_t gpio_dout);
void hx711_deinit(hx711_handle_t* hx);
bool hx711_power_init();
void hx711_set_power(bool state);
bool hx711_isready(hx711_handle_t* hx);
int32_t hx711_read_raw(hx711_handle_t* hx);
int32_t hx711_read_average(hx711_handle_t* hx);
float hx711_read_kg(hx711_handle_t* hx);
void hx711_set_gain(hx711_handle_t* hx, uint8_t gain);
void hx711_set_scale(hx711_handle_t* hx, float scale);
void hx711_tare(hx711_handle_t* hx);
""")


