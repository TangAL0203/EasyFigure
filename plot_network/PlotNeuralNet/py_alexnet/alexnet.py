#-*-coding:utf-8-*-
import sys
sys.path.append('..')
from pycore.tikzeng import *
# defined your arch

arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 55, 96, offset="(0,0,0)", to="(0,0,0)", height=30, depth=30, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=28, depth=28, width=1),
    to_Conv("conv2", 27, 256, offset="(1.3,0,0)", to="(pool1-east)", height=15, depth=15, width=5 ), # offset=(1,0,0) 在x轴正向有偏移(可为小数)
    to_connection("pool1", "conv2"),  #  在feature map之间画箭头
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=13, depth=13, width=1),
    to_Conv("conv3", 13, 384, offset="(1.3,0,0)", to="(pool2-east)", height=8, depth=8, width=8 ),
    to_connection("pool2", "conv3"),  #  在feature map之间画箭头
    to_Pool("pool3", offset="(0,0,0)", to="(conv3-east)", height=7, depth=7, width=1),
    to_Conv("conv4", 13, 384, offset="(1.3,0,0)", to="(pool3-east)", height=8, depth=8, width=8 ),
    to_connection("pool3", "conv4"),  #  在feature map之间画箭头
    to_Pool("pool4", offset="(0,0,0)", to="(conv4-east)", height=7, depth=7, width=1),
    to_Conv("conv5", 13, 256, offset="(1.3,0,0)", to="(pool4-east)", height=8, depth=8, width=5 ),
    to_connection("pool4", "conv5"),  #  在feature map之间画箭头
    to_Pool("pool5", offset="(0,0,0)", to="(conv5-east)", height=7, depth=7, width=1),
    to_SoftMax("fc1", 4096 ,"(1.5,0,0)", "(pool5-east)", caption="fc1"),
    to_connection("pool5", "fc1"),
    to_SoftMax("fc2", 4096 ,"(1.5,0,0)", "(fc1-east)", caption="fc2"),
    to_connection("fc1", "fc2"),
    to_SoftMax("soft1", 256 ,"(1.5,0,0)", "(fc2-east)", caption="softmax"),
    to_connection("fc2", "soft1"),
    to_end()
    ]
def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )
if __name__ == '__main__':
    main()