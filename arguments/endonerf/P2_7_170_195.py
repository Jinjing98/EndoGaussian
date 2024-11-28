ModelParams = dict(
    extra_mark = 'stereomis',
    camera_extent = 10,

    tool_mask = 'inverse',#'nouse',#'use', #'inverse'

)

OptimizationParams = dict(
    coarse_iterations = 1000,
    deformation_lr_init = 0.00016,
    deformation_lr_final = 0.0000016,
    deformation_lr_delay_mult = 0.01,
    grid_lr_init = 0.0016,
    grid_lr_final = 0.000016,
    iterations = 3000,
    percent_dense = 0.01,
    opacity_reset_interval = 3000,
    position_lr_max_steps = 4000,
    prune_interval = 3000
)

ModelHiddenParams = dict(
    kplanes_config = {
     'grid_dimensions': 2,
     'input_coordinate_dim': 4,
     'output_coordinate_dim': 64,
     'resolution': [64, 64, 64, 100]
    },
    multires = [1, 2, 4, 8],
    defor_depth = 0,
    net_width = 32,
    plane_tv_weight = 0,
    time_smoothness_weight = 0,
    l1_time_planes =  0,
    weight_decay_iteration=0,
)

# ModelParams = dict(
#     dataset_type='endonerf',
#     depth_scale=100.0,
#     frame_nums=26,
#     test_id=[1, 9, 17, 25],
#     is_mask=True,
#     depth_initial=True,
#     accurate_mask=True,
#     is_depth=True,

#     #jj
#     tool_mask = 'use',#'inverse',#'nouse',#'use'
# )

# OptimizationParams = dict(
#     iterations=40_000,
# )