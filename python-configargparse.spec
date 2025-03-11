#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module ConfigArgParse
Summary:	A Python module with support for argparse, config files, and env variables
Name:		python-configargparse
Version:	0.13.0
Release:	8
License:	MIT
Source0:	https://pypi.python.org/packages/source/C/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	6d3427dce78a17fb48222538f579bdb8
Group:		Libraries/Python
URL:		https://github.com/bw2/ConfigArgParse
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applications with more than a handful of user-settable options are
best configured through a combination of command line args, config
files, hard coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very
limited support for config files and environment variables, so this
module extends argparse to add these features.

%package -n python3-configargparse
Summary:	A Python module with support for argparse, config files, and env variables
Group:		Libraries/Python

%description -n python3-configargparse
Applications with more than a handful of user-settable options are
best configured through a combination of command line args, config
files, hard coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very
limited support for config files and environment variables, so this
module extends argparse to add these features.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif
%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/configargparse.py[co]
%{py_sitescriptdir}/%{module}*.egg-info
%endif

%if %{with python3}
%files -n python3-configargparse
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/configargparse.py
%{py3_sitescriptdir}/%{module}*.egg-info
%{py3_sitescriptdir}/__pycache__/configargparse*
%endif
