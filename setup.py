try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

from Cython.Distutils import build_ext
import pkg_resources

data_dir = pkg_resources.resource_filename("autowrap", "data_files")

ext = Extension("pairdist",
                sources = ['pairdist.pyx',
                           'src/Distance.cpp',
                           'src/ModelFactory.cpp',
                           'src/SiteContainerBuilder.cpp'],
                language="c++",
                include_dirs = [data_dir],
                libraries=['bpp-core', 'bpp-seq', 'bpp-phyl'],
                extra_compile_args=['-std=c++11'],
               )

setup(cmdclass={'build_ext':build_ext},
      name="pairdist",
      author='Kevin Gori',
      author_email='kgori@ebi.ac.uk',
      description='Pairwise distances by maximum likelihood',
      url='https://github.com/kgori/pairdist.git',
      version="0.0.1",
      scripts=['bin/pairdist'],
      ext_modules = [ext],
      install_requires=[
        'autowrap',
        'cython',
      ],
     )