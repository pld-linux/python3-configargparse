%define		module ConfigArgParse
Summary:	A Python module with support for argparse, config files, and env variables
Summary(pl.UTF-8):	Moduł Pythona wspomagający korzystanie z argparse, plików konfiguracyjnych i zmiennych środowiskowych
Name:		python3-configargparse
Version:	1.7
Release:	1
License:	MIT
Source0:	https://pypi.python.org/packages/source/C/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	ecc19145e5461a02b84963e76b21ae76
Group:		Libraries/Python
URL:		https://github.com/bw2/ConfigArgParse
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
BuildRequires:	python3-setuptools
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
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/configargparse.py
%{py3_sitescriptdir}/%{module}*.egg-info
%{py3_sitescriptdir}/__pycache__/configargparse*
