Name:		orcasayshelloworld
Version:	0.0.1
Release:        1.20250714115854128676.main%{?dist}
Summary:        A simple hello world script
URL:		https://github.com/betulependule/orcasayshelloworld
Source0:        orcasayshelloworld-0.0.1.tar.gz
License:	MIT
Requires:       python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%prep
%autosetup -n orcasayshelloworld-0.0.1

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{name}.py
