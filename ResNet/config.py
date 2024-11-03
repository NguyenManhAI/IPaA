config_resNet18 = {
    'conv1': {
        'kernel_size': 7,
        'in_channels': 3,
        'out_channels': 64,
        'stride': 2,
        'padding': 3
    },
    'maxpool': {
        'kernel_size': 3,
        'stride': 2,
        'padding': 1
    },
    'conv2_x': {
        'in_channels_layer': 64,
        'out_channels_block': [64,64],
        'kernel_sizes': [3,3],
        'num_blocks': 2,
        'paddings': [1,1]
    },
    'conv3_x': {
        'in_channels_layer': 64,
        'out_channels_block': [128,128],
        'kernel_sizes': [3,3],
        'num_blocks': 2,
        'paddings': [1,1]
    },
    'conv4_x': {
        'in_channels_layer': 128,
        'out_channels_block': [256,256],
        'kernel_sizes': [3,3],
        'num_blocks': 2,
        'paddings': [1,1]
    },
    'conv5_x': {
        'in_channels_layer': 256,
        'out_channels_block': [512,512],
        'kernel_sizes': [3,3],
        'num_blocks': 2,
        'paddings': [1,1]
    },
    '1000-d fc': {
        'in_features': 512,
        'out_features': 1000
    }
}
config_resNet34 = {
    'conv1': {
        'kernel_size': 7,
        'in_channels': 3,
        'out_channels': 64,
        'stride': 2,
        'padding': 3
    },
    'maxpool': {
        'kernel_size': 3,
        'stride': 2,
        'padding': 1
    },
    'conv2_x': {
        'in_channels_layer': 64,
        'out_channels_block': [64,64],
        'kernel_sizes': [3,3],
        'num_blocks': 3,
        'paddings': [1,1]
    },
    'conv3_x': {
        'in_channels_layer': 64,
        'out_channels_block': [128,128],
        'kernel_sizes': [3,3],
        'num_blocks': 4,
        'paddings': [1,1]
    },
    'conv4_x': {
        'in_channels_layer': 128,
        'out_channels_block': [256,256],
        'kernel_sizes': [3,3],
        'num_blocks': 6,
        'paddings': [1,1]
    },
    'conv5_x': {
        'in_channels_layer': 256,
        'out_channels_block': [512,512],
        'kernel_sizes': [3,3],
        'num_blocks': 3,
        'paddings': [1,1]
    },
    '1000-d fc': {
        'in_features': 512,
        'out_features': 1000
    }
}
config_resNet50 = {
    'conv1': {
        'kernel_size': 7,
        'in_channels': 3,
        'out_channels': 64,
        'stride': 2,
        'padding': 3
    },
    'maxpool': {
        'kernel_size': 3,
        'stride': 2,
        'padding': 1
    },
    'conv2_x': {
        'in_channels_layer': 64,
        'out_channels_block': [64,64,256],
        'kernel_sizes': [1,3,1],
        'num_blocks': 3,
        'paddings': [0,1,0]
    },
    'conv3_x': {
        'in_channels_layer': 256,
        'out_channels_block': [128,128,512],
        'kernel_sizes': [1,3,1],
        'num_blocks': 4,
        'paddings': [0,1,0]
    },
    'conv4_x': {
        'in_channels_layer': 512,
        'out_channels_block': [256,256,1024],
        'kernel_sizes': [1,3,1],
        'num_blocks': 6,
        'paddings': [0,1,0]
    },
    'conv5_x': {
        'in_channels_layer': 1024,
        'out_channels_block': [512,512,2048],
        'kernel_sizes': [1,3,1],
        'num_blocks': 3,
        'paddings': [0,1,0]
    },
    '1000-d fc': {
        'in_features': 2048,
        'out_features': 1000
    }
}
config_resNet101 = {
    'conv1': {
        'kernel_size': 7,
        'in_channels': 3,
        'out_channels': 64,
        'stride': 2,
        'padding': 3
    },
    'maxpool': {
        'kernel_size': 3,
        'stride': 2,
        'padding': 1
    },
    'conv2_x': {
        'in_channels_layer': 64,
        'out_channels_block': [64,64,256],
        'kernel_sizes': [1,3,1],
        'num_blocks': 3,
        'paddings': [0,1,0]
    },
    'conv3_x': {
        'in_channels_layer': 256,
        'out_channels_block': [128,128,512],
        'kernel_sizes': [1,3,1],
        'num_blocks': 4,
        'paddings': [0,1,0]
    },
    'conv4_x': {
        'in_channels_layer': 512,
        'out_channels_block': [256,256,1024],
        'kernel_sizes': [1,3,1],
        'num_blocks': 23,
        'paddings': [0,1,0]
    },
    'conv5_x': {
        'in_channels_layer': 1024,
        'out_channels_block': [512,512,2048],
        'kernel_sizes': [1,3,1],
        'num_blocks': 3,
        'paddings': [0,1,0]
    },
    '1000-d fc': {
        'in_features': 2048,
        'out_features': 1000
    }
}
config_resNet152 = {
    'conv1': {
        'kernel_size': 7,
        'in_channels': 3,
        'out_channels': 64,
        'stride': 2,
        'padding': 3
    },
    'maxpool': {
        'kernel_size': 3,
        'stride': 2,
        'padding': 1
    },
    'conv2_x': {
        'in_channels_layer': 64,
        'out_channels_block': [64,64,256],
        'kernel_sizes': [1,3,1],
        'num_blocks': 3,
        'paddings': [0,1,0]
    },
    'conv3_x': {
        'in_channels_layer': 256,
        'out_channels_block': [128,128,512],
        'kernel_sizes': [1,3,1],
        'num_blocks': 8,
        'paddings': [0,1,0]
    },
    'conv4_x': {
        'in_channels_layer': 512,
        'out_channels_block': [256,256,1024],
        'kernel_sizes': [1,3,1],
        'num_blocks': 36,
        'paddings': [0,1,0]
    },
    'conv5_x': {
        'in_channels_layer': 1024,
        'out_channels_block': [512,512,2048],
        'kernel_sizes': [1,3,1],
        'num_blocks': 3,
        'paddings': [0,1,0]
    },
    '1000-d fc': {
        'in_features': 2048,
        'out_features': 1000
    }
}
