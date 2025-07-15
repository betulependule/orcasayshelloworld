Name:		orcasayshelloworld
Version:	v0.1
Release:        1.20250715113101167490.main.1.g3de845c%{?dist}
Summary:        A simple hello world script
URL:		https://github.com/betulependule/orcasayshelloworld
Source0:        orcasayshelloworld-v0.1.tar.gz
License:	MIT
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
hello world, what did you expect?

%prep
%autosetup -n orcasayshelloworld-v0.1

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/orcasayshelloworld
%{python3_sitelib}/*

%changelog
* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715113101167490.main.1.g3de845c
- Fix some issues, try to trigger copr build (Alzbeta Kucerova)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715113029639994.main.1.g3de845c
- Fix some issues, try to trigger copr build (Alzbeta Kucerova)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715104822851960.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715104339348003.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715104322865413.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715104012991271.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715103839885414.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715103123658538.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715102303497009.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715101950446837.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715101701019001.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715094222726088.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715093617770073.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715093506374067.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715093113371739.main.0.g08c7dca
- Development snapshot (08c7dca4)

* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - 0.0.1
- test release: 0.0.1
* Tue Jul 15 2025 Alzbeta Kucerova <akucerov@redhat.com> - v0.1-1.20250715092754650028.main.0.g08c7dca
- Development snapshot (08c7dca4)
