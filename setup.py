# encoding=UTF-8
import platform

from setuptools.extension import Extension
from setuptools import setup
import Cython.Build
import numpy


# Read in requirements.txt and populate the python readme with the
# non-comment, non-environment-specifier contents.
_REQUIREMENTS = [req.split(';')[0].split('#')[0].strip() for req in
                 open('requirements.txt').readlines()
                 if (not req.startswith(('#', 'hg+', 'git+'))
                     and len(req.strip()) > 0)]
README = open('README.md').read().format(
    requirements='\n'.join(['    ' + r for r in _REQUIREMENTS]))

# Since OSX Mavericks, the stdlib has been renamed.  So if we're on OSX, we
# need to be sure to define which standard c++ library to use.  I don't have
# access to a pre-Mavericks mac, so hopefully this won't break on someone's
# older system.  Tested and it works on Mac OSX Catalina.
compiler_and_linker_args = []
if platform.system() == 'Darwin':
    compiler_and_linker_args = ['-stdlib=libc++']

setup(
    name='natcap.invest.community.ndr_plus',
    description="InVEST NDR+",
    long_description=README,
    maintainer='James Douglass',
    maintainer_email='jdouglass@stanford.edu',
    url='http://github.com/phargogh/natcap-community-ndr-plus',
    namespace_packages=['natcap.invest.community'],
    packages=[
        'natcap',
        'natcap.invest',
        'natcap.invest.community',
        'natcap.invest.community.ndr_plus',
    ],
    package_dir={
        'natcap': 'src/natcap'
    },
    use_scm_version={'version_scheme': 'post-release',
                     'local_scheme': 'node-and-date'},
    include_package_data=True,
    install_requires=_REQUIREMENTS,
    setup_requires=['setuptools_scm', 'numpy', 'cython'],
    license='BSD',
    long_description_content_type='text/x-md',
    zip_safe=False,
    keywords='gis invest',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Cython',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    ext_modules=[
        Extension(
            name="natcap.invest.community.ndr_plus.ndr_plus_cython",
            sources=['src/natcap/invest/ndr/ndr_plus_cython.pyx'],
            include_dirs=[numpy.get_include()],
            extra_compile_args=compiler_and_linker_args,
            extra_link_args=compiler_and_linker_args,
            language="c++"),
    ],
    cmdclass={'build_ext': Cython.Build.build_ext},
)
