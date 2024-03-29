#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xC5B4EE931A9F9DFD (codesign@isc.org)
#
Name     : dhcp
Version  : 4.4.3.p1
Release  : 46
URL      : https://downloads.isc.org/isc/dhcp/4.4.3-P1/dhcp-4.4.3-P1.tar.gz
Source0  : https://downloads.isc.org/isc/dhcp/4.4.3-P1/dhcp-4.4.3-P1.tar.gz
Source1  : dhcp.tmpfiles
Source2  : dhcp4.service
Source3  : https://downloads.isc.org/isc/dhcp/4.4.3-P1/dhcp-4.4.3-P1.tar.gz.asc
Summary  : The Internet Systems Consortium (ISC) DHCP server
Group    : Development/Tools
License  : MPL-2.0
Requires: dhcp-bin = %{version}-%{release}
Requires: dhcp-config = %{version}-%{release}
Requires: dhcp-libexec = %{version}-%{release}
Requires: dhcp-license = %{version}-%{release}
Requires: dhcp-man = %{version}-%{release}
Requires: dhcp-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : iproute2
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Dhcp includes the DHCP server which is used for dynamically configuring
hosts on a network.  Host configuration items such as IP address, name
servers, domain name, etc. can all be retrieved from the DHCP server by
a DHCP client.  This eases the burden of network wide configuration by
putting all of the configuration into one place.

%package bin
Summary: bin components for the dhcp package.
Group: Binaries
Requires: dhcp-libexec = %{version}-%{release}
Requires: dhcp-config = %{version}-%{release}
Requires: dhcp-license = %{version}-%{release}
Requires: dhcp-services = %{version}-%{release}

%description bin
bin components for the dhcp package.


%package config
Summary: config components for the dhcp package.
Group: Default

%description config
config components for the dhcp package.


%package dev
Summary: dev components for the dhcp package.
Group: Development
Requires: dhcp-bin = %{version}-%{release}
Provides: dhcp-devel = %{version}-%{release}
Requires: dhcp = %{version}-%{release}

%description dev
dev components for the dhcp package.


%package libexec
Summary: libexec components for the dhcp package.
Group: Default
Requires: dhcp-config = %{version}-%{release}
Requires: dhcp-license = %{version}-%{release}

%description libexec
libexec components for the dhcp package.


%package license
Summary: license components for the dhcp package.
Group: Default

%description license
license components for the dhcp package.


%package man
Summary: man components for the dhcp package.
Group: Default

%description man
man components for the dhcp package.


%package services
Summary: services components for the dhcp package.
Group: Systemd services
Requires: systemd

%description services
services components for the dhcp package.


%prep
%setup -q -n dhcp-4.4.3-P1
cd %{_builddir}/dhcp-4.4.3-P1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690914739
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check

%install
export SOURCE_DATE_EPOCH=1690914739
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dhcp
cp %{_builddir}/dhcp-4.4.3-P1/LICENSE %{buildroot}/usr/share/package-licenses/dhcp/63d12e221cdfb67f6aa4a9216494896cab0d356a || :
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/dhcp4.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/dhcp.conf
## install_append content
mkdir -p %{buildroot}/usr/libexec/
mv %{buildroot}/usr/bin/dhclient %{buildroot}/usr/libexec/dhclient
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dhcpd
/usr/bin/dhcrelay
/usr/bin/omshell

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/dhcp.conf

%files dev
%defattr(-,root,root,-)
/usr/include/dhcpctl/dhcpctl.h
/usr/include/omapip/alloc.h
/usr/include/omapip/buffer.h
/usr/include/omapip/convert.h
/usr/include/omapip/hash.h
/usr/include/omapip/isclib.h
/usr/include/omapip/omapip.h
/usr/include/omapip/omapip_p.h
/usr/include/omapip/result.h
/usr/include/omapip/trace.h
/usr/share/man/man3/dhcpctl.3
/usr/share/man/man3/omapi.3

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dhclient

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dhcp/63d12e221cdfb67f6aa4a9216494896cab0d356a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/omshell.1
/usr/share/man/man5/dhclient.conf.5
/usr/share/man/man5/dhclient.leases.5
/usr/share/man/man5/dhcp-eval.5
/usr/share/man/man5/dhcp-options.5
/usr/share/man/man5/dhcpd.conf.5
/usr/share/man/man5/dhcpd.leases.5
/usr/share/man/man8/dhclient-script.8
/usr/share/man/man8/dhclient.8
/usr/share/man/man8/dhcpd.8
/usr/share/man/man8/dhcrelay.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/dhcp4.service
