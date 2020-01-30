from collections import namedtuple
from niworkflows.utils.spaces import SpatialReferences, Space
from smriprep.workflows.base import init_single_subject_wf
BIDSLayout = namedtuple('BIDSLayout', ['root'])
wf = init_single_subject_wf(
    debug=False,
    freesurfer=True,
    hires=True,
    layout=BIDSLayout('.'),
    longitudinal=False,
    low_mem=False,
    name='single_subject_wf',
    omp_nthreads=1,
    output_dir='.',
    reportlets_dir='.',
    skull_strip_fixed_seed=False,
    skull_strip_template=Space.from_string('OASIS30ANTs')[0],
    spaces=SpatialReferences(['MNI152NLin2009cAsym', 'fsaverage5']),
    subject_id='test',
)