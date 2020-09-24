#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rosdistro
Version  : 0.8.2
Release  : 19
URL      : https://files.pythonhosted.org/packages/88/28/160b8af1f59f8f991a3509b39141142b39b1d3e4aabf31cb7ae2d6597c72/rosdistro-0.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/28/160b8af1f59f8f991a3509b39141142b39b1d3e4aabf31cb7ae2d6597c72/rosdistro-0.8.2.tar.gz
Summary  : A tool to work with rosdistro files
Group    : Development/Tools
License  : MIT
Requires: rosdistro-bin = %{version}-%{release}
Requires: rosdistro-python = %{version}-%{release}
Requires: rosdistro-python3 = %{version}-%{release}
Requires: PyYAML
Requires: catkin_pkg
Requires: rospkg
Requires: setuptools
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : catkin_pkg
BuildRequires : rospkg
BuildRequires : setuptools

%description
rosdistro
=====
Code & tickets
--------------
+----------------------+-----------------------------------------------------------+
| rosdistro            | http://github.com/ros-infrastructure/rosdistro            |
+----------------------+-----------------------------------------------------------+
| Issues               | http://github.com/ros-infrastructure/rosdistro/issues     |
+----------------------+-----------------------------------------------------------+

%package bin
Summary: bin components for the rosdistro package.
Group: Binaries

%description bin
bin components for the rosdistro package.


%package python
Summary: python components for the rosdistro package.
Group: Default
Requires: rosdistro-python3 = %{version}-%{release}

%description python
python components for the rosdistro package.


%package python3
Summary: python3 components for the rosdistro package.
Group: Default
Requires: python3-core
Provides: pypi(rosdistro)
Requires: pypi(catkin_pkg)
Requires: pypi(pyyaml)
Requires: pypi(rospkg)
Requires: pypi(setuptools)

%description python3
python3 components for the rosdistro package.


%prep
%setup -q -n rosdistro-0.8.2
cd %{_builddir}/rosdistro-0.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590680682
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rosdistro_build_cache
/usr/bin/rosdistro_freeze_source
/usr/bin/rosdistro_migrate_to_rep_141
/usr/bin/rosdistro_migrate_to_rep_143
/usr/bin/rosdistro_reformat

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
