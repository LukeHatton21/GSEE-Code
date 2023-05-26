from gsee.climatedata_interface.interface import run_interface

run_interface(
    ghi_data=('SWGDN_2022.nc','global_horizontal'),
    outfile = 'gsee_output.nc',
    params=dict(tilt=35, azim=180, tracking=0, capacity=1000),
    frequency='H',
    temp_data=('T2M_2022.nc', 'temperature'),
    pdfs_file=None,
)