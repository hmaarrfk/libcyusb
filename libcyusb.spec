Name:       libcyusb
Version:    1.0.5
Release:	2%{?dist}
Summary:    CyUSB library for linux

Group:      Development/Libraries
License:    LGPL 2.1
URL:        http://www.cypress.com/
%global owner opticalwavefrontlabs
%global commit 9f5da3b2b19d5ac2f24adf41fd4dd063a9e01c31
%global gittag v1.0.5-2
%global shortcommit %(c=%{commit}; echo ${c:0:12})
Source0:    https://bitbucket.org/%{owner}/%{name}/get/%{gittag}.tar.gz#/%{owner}-%{name}-%{shortcommit}.zip

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
%autosetup -n %{owner}-%{name}-%{shortcommit}


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
* Sun Apr 22 2018 Mark Harfouche <mark.harfouche@gmail.com> - 1.0.5-2
- rebuilt

* Sun Apr 22 2018 Mark Harfouche <mark.harfouche@gmail.com> - 1.0.5-1
- First build


