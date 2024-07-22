from src.base import Target

Target(
    name = 'stripped',
    release_name = 'oss-cad-suite',
    top_package = True,
    dependencies = [
        'ghdl',
        'ghdl-yosys-plugin',
        'gtkwave',
        'verilator',
        'iverilog',
        'utils',
        'cocotb'
    ],
    branding = 'OSS CAD Suite',
    readme = 'README',
    resources = [ 'system-resources' ],

)