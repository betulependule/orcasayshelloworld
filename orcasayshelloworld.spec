Name:		orcasayshelloword
Version:	0.0.1
Release:        1%{?dist}
Summary:        A simple hello world script
URL:		https://github.com/betulependule/orcasayshelloworld
Source0:        orcasayshelloworld-%{version}.tar.gz
Requires:       python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{name}.py
