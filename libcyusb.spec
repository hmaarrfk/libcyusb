Name:       libcyusb
Version:    1.0.5
Release:	3%{?dist}
Summary:    CyUSB library for linux

Group:      Development/Libraries
License:    LGPL 2.1
URL:        http://www.cypress.com/
%global owner hmaarrfk
%global commit 07d0eccf26f8e7214b37ad1a97863a8cc36fd5c9
%global gittag v1.0.5-3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Source0:    https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libusb-devel
Requires:       libusb

%description
Cypress Semiconductor Corporation
CyUSB library for linux, version 1.0.5

%package devel
Summary:    CyUSB development libraries for linux
%description devel
Cypress Semiconductor Corporation
Development CyUSB library for linux, version 1.0.5


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake .
%make_build


%install
%make_install


%files
%doc
%{_libdir}/%{name}.so.*
%{_sysconfdir}/*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so



%changelog
* Sun Apr 22 2018 Mark Harfouche <mark.harfouche@gmail.com> - 1.0.5-3
- rebuilt

* Sun Apr 22 2018 Mark Harfouche <mark.harfouche@gmail.com> - 1.0.5-2
- rebuilt

* Sun Apr 22 2018 Mark Harfouche <mark.harfouche@gmail.com> - 1.0.5-1
- First build
