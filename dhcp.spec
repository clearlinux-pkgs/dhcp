#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dhcp
Version  : 4.3.3
Release  : 1
URL      : https://ftp.isc.org/isc/dhcp/4.3.3/dhcp-4.3.3.tar.gz
Source0  : https://ftp.isc.org/isc/dhcp/4.3.3/dhcp-4.3.3.tar.gz
Summary  : The Internet Systems Consortium (ISC) DHCP server
Group    : Development/Tools
License  : BSD-3-Clause ISC
Requires: dhcp-bin
Requires: dhcp-lib
Requires: dhcp-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bind-utils-dev
BuildRequires : bind-utils-lib
BuildRequires : gettext-bin
BuildRequires : iproute2
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: 0001-Allow-use-of-external-bind.patch
Patch2: 0002-Use-libtool-to-build-dynamic-libraries.patch

%description
Dhcp includes the DHCP server which is used for dynamically configuring
hosts on a network.  Host configuration items such as IP address, name
servers, domain name, etc. can all be retrieved from the DHCP server by
a DHCP client.  This eases the burden of network wide configuration by
putting all of the configuration into one place.

%package bin
Summary: bin components for the dhcp package.
Group: Binaries

%description bin
bin components for the dhcp package.


%package dev
Summary: dev components for the dhcp package.
Group: Development
Requires: dhcp-lib
Requires: dhcp-bin
Provides: dhcp-devel

%description dev
dev components for the dhcp package.


%package doc
Summary: doc components for the dhcp package.
Group: Documentation

%description doc
doc components for the dhcp package.


%package lib
Summary: lib components for the dhcp package.
Group: Libraries

%description lib
lib components for the dhcp package.


%prep
%setup -q -n dhcp-4.3.3
%patch1 -p1
%patch2 -p1

%build
%reconfigure --disable-static --with-libbind-libs=%{_libdir} \
--with-libbind=%{_includedir}/bind9
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dhclient
/usr/bin/dhcpd
/usr/bin/dhcrelay
/usr/bin/omshell

%files dev
%defattr(-,root,root,-)
/usr/include/dhcpctl/dhcpctl.h
/usr/include/isc-dhcp/dst.h
/usr/include/omapip/alloc.h
/usr/include/omapip/buffer.h
/usr/include/omapip/convert.h
/usr/include/omapip/hash.h
/usr/include/omapip/isclib.h
/usr/include/omapip/omapip.h
/usr/include/omapip/omapip_p.h
/usr/include/omapip/result.h
/usr/include/omapip/trace.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
