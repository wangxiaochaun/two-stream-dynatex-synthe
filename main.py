import tensorflow as tf
import argparse
from synthesizer import Synthesizer

# set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--batchsize', type=int, default=1, help='input batch size')
parser.add_argument('--iter', type=int, default=6000, help='number of iterations to optimize for')
parser.add_argument('--sfreq', type=int, default=1000, help='number of iterations before saving a snapshot')
parser.add_argument('--noutfreq', type=int, default=100, help='number of iterations before saving synthesized '
                                                              'textures to disk')
parser.add_argument('--lfreq', type=int, default=100, help='number of iterations before logging to disk')
parser.add_argument('--gpu', type=int, default=0, help='which GPU to use')
parser.add_argument('--runid', default='synthesized', help='id assigned to this run')
parser.add_argument('--dynamics_target', default='', help='path to target dynamic texture')
parser.add_argument('--appearance_target', default='', help='path to target static texture')
parser.add_argument('--dynamics_model', default='MSOEnet', help='path to dynamics modeling network')
parser.add_argument('--type', required=True, help='dts -> dynamic texture synthesis |'
                                                  'dst -> dynamics style transfer |'
                                                  'inf -> infinite/endless dynamic texture synthesis |'
                                                  'inc -> incremental dynamic texture synthesis |'
                                                  'sta -> static texture synthesis')

opt = parser.parse_args()
print(opt)

# config
config_proto = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
config_proto.gpu_options.allow_growth = True
my_config = {'batch_size': opt.batchsize, 'iterations': opt.iter, 'snapshot_frequency': opt.sfreq,
             'network_out_frequency': opt.noutfreq, 'log_frequency': opt.lfreq, 'gpu': opt.gpu,
             'run_id': opt.runid, 'dynamics_model': opt.dynamics_model}

if opt.type == 'dts':
    assert opt.dynamics_target != ''
    s = Synthesizer(opt.dynamics_target,
                          config={'tf': config_proto,
                                  'user': my_config})

s.optimize()
