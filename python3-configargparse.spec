#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module ConfigArgParse
Summary:	A Python module with support for argparse, config files, and env variables
Summary(pl.UTF-8):	Moduł Pythona wspomagający korzystanie z argparse, plików konfiguracyjnych i zmiennych środowiskowych
Name:		python3-configargparse
Version:	1.7.1
Release:	1
License:	MIT
#Source0Download: https://pypi.org/simple/configargparse/
Source0:	https://files.pythonhosted.org/packages/source/C/ConfigArgParse/configargparse-%{version}.tar.gz
# Source0-md5:	00ef613e320702f0b3eb95e0619ded5f
Group:		Libraries/Python
URL:		https://github.com/bw2/ConfigArgParse
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applications with more than a handful of user-settable options are
best configured through a combination of command line args, config
files, hard coded defaults, and in some cases, environment variables.

Python's command line parsing modules such as argparse have very
limited support for config files and environment variables, so this
module extends argparse to add these features.

%description -l pl.UTF-8
Aplikacje z więcej niż kilkoma opcjami ustawianymi przez użytkownika
najlepiej się konfiguruje połączeniem argumentów wiersza poleceń,
plików konfiguracyjnych, zakodowanych opcji domyślnych oraz, w
niektórych przypadkach, zmiennych środowiskowych.

Moduły Pythona do analizy wiersza poleceń, takie jak argparse, mają
bardzo ograniczoną obsługę plików konfiguracyjnych i zmiennych
środowiskowych, więc ten moduł rozszerza argparse o tę funkcjonalność.

%prep
%setup -q -n configargparse-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/configargparse.py
%{py3_sitescriptdir}/__pycache__/configargparse.cpython-*.py[co]
%{py3_sitescriptdir}/ConfigArgParse-%{version}-py*.egg-info
